import subprocess
import os

# Run get_music.py first to fetch background music
os.system("python scripts/get_music.py")

# Input files (later Make.com will provide these)
narration_file = "narration.mp3"    # voiceover
music_file = "background.mp3"       # fetched automatically
video_file = "final_video.mp4"      # output

# Step 1: Mix narration + background music
mixed_audio = "mixed_audio.mp3"
subprocess.run([
    "ffmpeg", "-y",
    "-i", narration_file,
    "-i", music_file,
    "-filter_complex", "[1:a]volume=0.15[a1];[0:a][a1]amix=inputs=2:duration=first:dropout_transition=3",
    "-c:a", "mp3",
    mixed_audio
])

# Step 2: Use placeholder stock video (later we’ll automate stock fetch)
placeholder_video = "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4"
if not os.path.exists("clip.mp4"):
    subprocess.run(["curl", "-L", "-o", "clip.mp4", placeholder_video])

# Step 3: Merge video + audio
subprocess.run([
    "ffmpeg", "-y",
    "-i", "clip.mp4",
    "-i", mixed_audio,
    "-c:v", "copy",
    "-c:a", "aac",
    video_file
])

print("✅ Final video created:", video_file)
