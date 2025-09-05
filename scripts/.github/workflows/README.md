# Finance Automation Video Builder

This repo automatically builds finance YouTube videos using:

- Google Gemini (for script generation, added later in Make.com)
- TTS (for narration, added later in Make.com)
- Pixabay API (for background music)
- FFmpeg (for mixing narration + music + video)

GitHub Actions runs `scripts/make_video.py` daily and produces `final_video.mp4`.
