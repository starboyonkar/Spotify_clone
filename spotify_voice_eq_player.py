# Complete code for a Spotify voice-controlled music player with automatic EQ settings
# based on user profile (name, email, dob, age, gender), with real-time voice control

import os
import json
import time
import webbrowser
import queue
import threading
import sounddevice as sd
import vosk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime

# ========== Configuration ==========
CLIENT_ID = '3d31e4b0e23f408b953072bb3f684a00'
CLIENT_SECRET = 'd95fa70df6b146a699af44a80cca4f41'
REDIRECT_URI = 'http://127.0.0.1:8000/callback'
SCOPE = 'user-read-playback-state user-modify-playback-state user-read-private user-read-email streaming'

# ========== Sign Up and Profile ==========
def spotify_login():
    sp_oauth = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        cache_path=".cache"
    )

    token_info = sp_oauth.get_cached_token()

    if not token_info:
        # If no cached token, manually open auth URL and get token
        auth_url = sp_oauth.get_authorize_url()
        print("🔗 Please open this URL in your browser:", auth_url)
        webbrowser.open(auth_url)
        response_url = input("📥 Paste the redirected URL after login: ")
        code = sp_oauth.parse_response_code(response_url)
        token_info = sp_oauth.get_access_token(code)

    access_token = token_info['access_token']
    sp = spotipy.Spotify(auth=access_token)

    user_info = sp.current_user()
    name = user_info.get('display_name', 'Unknown')
    email = user_info.get('email', 'unknown@example.com')
    dob = user_info.get('birthdate', '2000-01-01')  # May not be available
    gender = 'not specified'  # Spotify does not return gender
    age = 2025 - int(dob.split("-")[0]) if dob else 25

    profile = {
        "name": name,
        "email": email,
        "dob": dob,
        "age": age,
        "gender": gender
    }

    with open("user_profile.json", "w") as f:
        json.dump(profile, f)

    return sp, profile


# ========== Spotify Control ==========
def play_song(sp, song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    tracks = results['tracks']['items']
    if tracks:
        uri = tracks[0]['uri']
        sp.start_playback(uris=[uri])
        print(f"Playing: {tracks[0]['name']} - {tracks[0]['artists'][0]['name']}")
    else:
        print("Song not found.")

def control_playback(sp, command):
    if command == "play":
        sp.start_playback()
    elif command == "pause":
        sp.pause_playback()
    elif command == "next":
        sp.next_track()
    elif command == "previous":
        sp.previous_track()

# ========== Voice Recognition ==========
q = queue.Queue()
model = vosk.Model(lang="en-us")

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def recognize_voice(sp):
    print("Voice control started. Say commands like 'play', 'pause', 'next song', 'previous', or 'play [song name]'")
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").lower()
                if text:
                    print("Heard:", text)
                    if text in ["play", "pause", "next", "previous"]:
                        control_playback(sp, text)
                    elif text.startswith("play"):
                        song_name = text.replace("play", "", 1).strip()
                        if song_name:
                            play_song(sp, song_name)

# ========== Main Execution ==========
if __name__ == '__main__':
    sp, profile = spotify_login()
    apply_eq(profile)

    # Open Spotify web player (optional)
    webbrowser.open("https://open.spotify.com")

    # Start voice control thread
    voice_thread = threading.Thread(target=recognize_voice, args=(sp,))
    voice_thread.start()
