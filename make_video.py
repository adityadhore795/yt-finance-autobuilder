import subprocess

# Inputs
narration = "voice.mp3"
music = "background.mp3"
stock_clip = "stock.mp4"  # placeholder for now
output = "output.mp4"

# Merge narration + background music into one audio track
mixed_audio = "mixed_audio.mp3"
subprocess.run([
    "ffmpeg", "-y",
    "-i", narration,
    "-i", music,
    "-filter_complex", "[1:a]volume=0.2[a1];[0:a][a1]amix=inputs=2:duration=first:dropout_transition=2",
    "-c:a", "mp3",
    mixed_audio
])

# Combine stock video + mixed audio
subprocess.run([
    "ffmpeg", "-y",
    "-i", stock_clip,
    "-i", mixed_audio,
    "-c:v", "libx264", "-preset", "fast",
    "-c:a", "aac", "-shortest",
    output
])

print(f"Video created: {output}")
