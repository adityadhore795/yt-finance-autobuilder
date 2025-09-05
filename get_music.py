import requests, random, os

API_KEY = os.getenv("PIXABAY_API_KEY")
QUERY = "ambient"

if not API_KEY:
    raise Exception("❌ PIXABAY_API_KEY not found. Did you set the GitHub secret?")

url = f"https://pixabay.com/api/music/?key={API_KEY}&q={QUERY}&per_page=50"
resp = requests.get(url)

print("🔎 Debug: Pixabay response status =", resp.status_code)
print("🔎 Debug: Pixabay response text =", resp.text[:200])  # print first 200 chars

try:
    data = resp.json()
except Exception as e:
    raise Exception(f"❌ Could not decode JSON. Response was: {resp.text}") from e

if "hits" in data and data["hits"]:
    track = random.choice(data["hits"])
    music_url = track["audio"]
    music_file = "background.mp3"
    r = requests.get(music_url)

    with open(music_file, "wb") as f:
        f.write(r.content)

    print(f"✅ Downloaded music: {track['name']}")
else:
    raise Exception("❌ No music found in Pixabay API response")
