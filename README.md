Here’s a professional and detailed README.md file for your Spotify Clone voice-controlled music player project:

markdown
Copy
Edit
# 🎵 Spotify Voice-Controlled Music Player 🎧

This project is a **voice-controlled music player** that integrates with Spotify, allowing users to control playback through **real-time voice commands**. It also applies **automatic EQ settings** based on the user's **Spotify profile** (name, email, DOB, age, gender). Built using Python, Spotipy (Spotify API), Vosk (speech recognition), and SoundDevice.

---

## 🧠 Key Features

- 🎙️ Real-time voice control for:
  - `play`, `pause`, `next`, `previous`
  - `play [song name]`
- 🔒 Spotify OAuth login
- 📋 Automatically fetches user profile (Name, Email, DOB)
- 📊 Applies dynamic EQ based on **age group** to apply Eq parameters
- 🌐 Opens Spotify Web Player in browser
- 🧠 Voice recognition powered by **Vosk**
- 🔄 Runs continuously in the background via multithreading

---

## 📁 Project Structure

Spotify_clone/ ├── user_profile.json # Stores fetched user data ├── main.py # Main Python application ├── README.md # Project Documentation ├── requirements.txt # All required dependencies └── .cache/ # Spotify token cache (auto-generated)

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Spotify_clone.git
cd Spotify_clone
2. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
requirements.txt includes:
spotipy

vosk

sounddevice

numpy

requests

For Windows, install Vosk model separately.

3. Download Vosk Speech Recognition Model
🔗 Download English Model (vosk-model-small-en-us-0.15)

Extract and place the folder inside the project directory:

Copy
Edit
Spotify_clone/
└── vosk-model-small-en-us-0.15/
4. Spotify Developer Setup
Go to Spotify Developer Dashboard

Create an app and get:

Client ID

Client Secret

Set REDIRECT_URI as: http://127.0.0.1:8000/callback

Update these in main.py:

python
Copy
Edit
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
REDIRECT_URI = 'http://127.0.0.1:8000/callback'
🚀 Running the App
bash
Copy
Edit
python main.py
Logs into Spotify

Applies EQ settings based on age

Opens browser to Spotify Web

Starts always-on voice recognition to control music

🧠 Voice Commands You Can Use

Command	Description
play	Resumes playback
pause	Pauses playback
next	Plays next track
previous	Plays previous track
play [song]	Searches & plays a specific song
Example:
➡️ “play Believer”
➡️ “pause”

⚙️ EQ Settings Based on Age

Age Range	Bass	Treble
< 20	7	5
20 - 40	5	5
> 40	3	7
📦 Future Enhancements
GUI with PyQt5

Real-time waveform visualizations

Voice profile storage

Playlist control

Gender-based EQ adjustments

## 🎧 Feature-1: Added project enhancement



📃 License
This project is for educational purposes. Not affiliated with Spotify.

🙌 Author
Onkar Chaugule
LinkedIn | GitHub

