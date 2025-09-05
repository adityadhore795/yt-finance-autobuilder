import requests, random, os

# Get your Pixabay API key from GitHub Secrets
API_KEY = os.getenv("PIXABAY_API_KEY")
if not API_KEY:
    raise Exception("❌ PIXABAY_API_KEY not found. Did you set the GitHub secret?")
QUERY = "ambient"

url = f"https://pixabay.com/api/music/?key={API_KEY}&q={QUERY}&per_page=50"
resp = requests.get(url).json()

if "hits" in resp and resp["hits"]:
    track = random.choice(resp["hits"])
    music_url = track["audio"]
    music_file = "background.mp3"
    r = requests.get(music_url)

    with open(music_file, "wb") as f:
        f.write(r.content)

    print(f"Downloaded music: {track['name']}")
else:
    raise Exception("No music found from Pixabay API")
