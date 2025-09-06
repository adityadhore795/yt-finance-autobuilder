import requests

# Example free CC0 stock video (Pixabay, finance-themed)
url = "https://cdn.pixabay.com/video/2018/07/05/16969-274611938_large.mp4"

resp = requests.get(url)
with open("stock.mp4", "wb") as f:
    f.write(resp.content)

print("✅ stock.mp4 downloaded")
