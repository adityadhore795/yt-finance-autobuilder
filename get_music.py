import requests, random

# Example list of public domain tracks
TRACKS = [
    "https://freepd.com/music/Local%20Forecast%20-%20Elevator.mp3",
    "https://freepd.com/music/Local%20Forecast%20-%20Slower.mp3",
    "https://freepd.com/music/Local%20Forecast%20-%20Stings.mp3",
    "https://freepd.com/music/Monkeys%20Spinning%20Monkeys.mp3",
    "https://freepd.com/music/Scheming%20Weasel.mp3",
    "https://freepd.com/music/Sneaky%20Snitch.mp3"
]

track_url = random.choice(TRACKS)
music_file = "background.mp3"

print(f"🎵 Downloading music from: {track_url}")
r = requests.get(track_url)

with open(music_file, "wb") as f:
    f.write(r.content)

print(f"✅ Music saved as {music_file}")
