import requests

# Example free CC0 stock video (short clip, safe for reuse)
url = "https://cdn.pixabay.com/video/2019/05/06/22715-338231996_tiny.mp4"

resp = requests.get(url)
with open("stock.mp4", "wb") as f:
    f.write(resp.content)

print("✅ stock.mp4 downloaded")
