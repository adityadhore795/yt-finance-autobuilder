from gtts import gTTS

# Read generated script
with open("script.txt", "r") as f:
    text = f.read()

# Convert to speech
tts = gTTS(text=text, lang="en", slow=False)
tts.save("voice.mp3")

print("✅ voice.mp3 created")
