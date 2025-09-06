import subprocess
import os

# Inputs
narration = "voice.mp3"
music = "background.mp3"
stock_clip = "stock.mp4"
mixed_audio = "mixed_audio.aac"
output = "output.mp4"

# Step 1: Merge narration + background music into one audio track
subprocess.run([
    "ffmpeg", "-y",
    "-i", narration,
    "-i", music,
    "-filter_complex", "[1:a]volume=0.2[a1];[0:a][a1]amix=inputs=2:duration=first:dropout_transition=2",
    "-c:a", "aac",
    mixed_audio
])

# Step 2: Loop stock video until narration ends
subprocess.run([
    "ffmpeg", "-y",
    "-stream_loop", "-1",   # loop infinitely
    "-i", stock_clip,
    "-i", mixed_audio,
    "-c:v", "libx264", "-preset", "fast",
    "-tune", "stillimage",
    "-c:a", "aac",
    "-shortest",
    output
])

print(f"Video created: {output}")

if os.path.exists(output):
    print("✅ Video successfully created: output.mp4")
else:
    print("❌ No output.mp4 found. Check ffmpeg logs above.")
