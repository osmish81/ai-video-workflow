# workflow/scripts/transcriber.py

import os
from moviepy.editor import VideoFileClip
import whisper

# Paths
VIDEOS_DIR = "../../data/videos/"
AUDIO_DIR = "../../data/audio/"
TRANSCRIPTS_DIR = "../../data/transcripts/"

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)

# Load Whisper model (CPU-friendly small model)
model = whisper.load_model("tiny")

# Process each video
for filename in os.listdir(VIDEOS_DIR):
    if filename.endswith(".mp4"):
        video_path = os.path.join(VIDEOS_DIR, filename)
        audio_path = os.path.join(AUDIO_DIR, filename.replace(".mp4", ".mp3"))
        transcript_path = os.path.join(TRANSCRIPTS_DIR, filename.replace(".mp4", ".txt"))
        
        # Extract audio
        print(f"Extracting audio from {filename}")
        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(audio_path, logger=None)
        clip.close()
        
        # Transcribe audio
        print(f"Transcribing {filename}")
        result = model.transcribe(audio_path)
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(result["text"])
