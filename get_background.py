import requests

# Example CC0 background music (Pixabay direct link)
url = "https://cdn.pixabay.com/download/audio/2022/03/15/audio_27a23d3490.mp3?filename=calm-ambient-11157.mp3"

resp = requests.get(url)
with open("background.mp3", "wb") as f:
    f.write(resp.content)

print("✅ background.mp3 downloaded")
