# workflow/scripts/nlp.py

import os
from transformers import pipeline

# Paths
TRANSCRIPTS_DIR = "../../data/transcripts/"
SUMMARIES_DIR = "../../data/summaries/"
HASHTAGS_DIR = "../../data/hashtags/"

os.makedirs(SUMMARIES_DIR, exist_ok=True)
os.makedirs(HASHTAGS_DIR, exist_ok=True)

# Load summarization pipeline
summarizer = pipeline("summarization")

# Example hashtags generator (simple version)
def generate_hashtags(summary):
    # Very simple placeholder logic
    words = summary.lower().split()
    hashtags = set()
    for word in words:
        if word.isalpha() and len(hashtags) < 5:
            hashtags.add(f"#{word}")
    return list(hashtags)

# Process each transcript
for filename in os.listdir(TRANSCRIPTS_DIR):
    if filename.endswith(".txt"):
        transcript_path = os.path.join(TRANSCRIPTS_DIR, filename)
        with open(transcript_path, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Summarize transcript
        print(f"Summarizing {filename}")
        summary = summarizer(text, max_length=60, min_length=20, do_sample=False)[0]['summary_text']
        summary_path = os.path.join(SUMMARIES_DIR, filename)
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary)
        
        # Generate hashtags
        hashtags = generate_hashtags(summary)
        hashtags_path = os.path.join(HASHTAGS_DIR, filename)
        with open(hashtags_path, "w", encoding="utf-8") as f:
            f.write(", ".join(hashtags))
