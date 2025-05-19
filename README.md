# 🎵 Spotify Voice-Controlled Music Player 🎧

A futuristic **voice-controlled music player** that integrates with **Spotify**, enabling real-time voice commands and personalized EQ settings based on the user’s Spotify profile.

Built using **Python**, **Spotipy (Spotify API)**, **Vosk (speech recognition)**, and **SoundDevice**.

---

## 🧠 Key Features

- 🎙️ **Real-time voice control**:
  - `play`, `pause`, `next`, `previous`
  - `play [song name]` (e.g., “play Believer”)
- 🔐 **Spotify OAuth login** & profile integration
- 📋 Auto-fetches user info: Name, Email, DOB, Age, Gender
- 📊 Applies **dynamic EQ** settings based on age group
- 🌐 Launches Spotify Web Player in the browser
- 🧠 Voice recognition via **Vosk**
- 🔁 Runs in background using multithreading

---

## 📁 Project Structure

```
Spotify_clone/
├── main.py                # Main Python application
├── requirements.txt       # Python dependencies
├── user_profile.json      # Stores Spotify user profile data
├── README.md              # Project documentation
├── .cache/                # Spotify token cache (auto-generated)
└── vosk-model-small-en-us-0.15/  # Vosk speech model directory
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Spotify_clone.git
cd Spotify_clone
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
**Dependencies:**
- `spotipy`
- `vosk`
- `sounddevice`
- `numpy`
- `requests`

> ⚠️ On **Windows**, download the Vosk model manually (see next step).

### 3. Download Vosk Speech Model

🔗 [Download English Model (vosk-model-small-en-us-0.15)](https://alphacephei.com/vosk/models)

Extract into the project folder:
```
Spotify_clone/
└── vosk-model-small-en-us-0.15/
```

### 4. Spotify Developer Setup

- Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- Create an app → get:
  - **Client ID**
  - **Client Secret**
- Set the **Redirect URI** to:
  ```
  http://127.0.0.1:8000/callback
  ```
- Update the following in `main.py`:
```python
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
REDIRECT_URI = 'http://127.0.0.1:8000/callback'
```

---

## 🚀 Running the App

```bash
python main.py
```

✔️ Logs into Spotify  
✔️ Applies EQ settings based on age  
✔️ Opens Spotify Web  
✔️ Listens for voice commands continuously

---

## 🗣️ Voice Commands You Can Use

| Command        | Description             |
|----------------|-------------------------|
| `play`         | Resume playback         |
| `pause`        | Pause playback          |
| `next`         | Next track              |
| `previous`     | Previous track          |
| `play [song]`  | Play specific song      |

Example:  
- “play Shape of You”  
- “pause”

---

## 🎚️ EQ Settings Based on Age

| Age Range | Bass | Treble |
|-----------|------|--------|
| < 20      | 7    | 5      |
| 20 - 40   | 5    | 5      |
| > 40      | 3    | 7      |

---

## 📦 Future Enhancements

- 🎛️ GUI interface using PyQt5
- 📈 Real-time waveform visualizations
- 🧠 Voice profile storage & personalization
- 📂 Playlist & album control
- ⚖️ Gender-based EQ presets

---

## 📃 License

This project is for educational use only. Not affiliated with Spotify.

---

## 🙌 Author

**Onkar Chaugule**  
🔗 [LinkedIn](https://linkedin.com/in/onkar-chaugule) • [GitHub](https://github.com/starboyonkar)
