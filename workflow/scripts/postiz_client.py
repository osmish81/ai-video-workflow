# workflow/scripts/postiz_client.py

import os
import requests

# Paths
VIDEOS_DIR = "../../data/videos/"
SUMMARIES_DIR = "../../data/summaries/"
HASHTAGS_DIR = "../../data/hashtags/"

# Postiz API endpoint (replace with your self-hosted URL)
POSTIZ_API_URL = "http://YOUR_POSTIZ_SERVER_IP:5000/api/post_video"

# Proxy (optional)
PROXIES = {
    "http": "http://your_proxy_here:port",
    "https": "http://your_proxy_here:port"
}

# Post each video
for filename in os.listdir(VIDEOS_DIR):
    if filename.endswith(".mp4"):
        video_path = os.path.join(VIDEOS_DIR, filename)
        summary_path = os.path.join(SUMMARIES_DIR, filename.replace(".mp4", ".txt"))
        hashtags_path = os.path.join(HASHTAGS_DIR, filename.replace(".mp4", ".txt"))

        # Read title/summary
        with open(summary_path, "r", encoding="utf-8") as f:
            title = f.read()

        # Read hashtags
        with open(hashtags_path, "r", encoding="utf-8") as f:
            hashtags = f.read()

        data = {
            "title": title,
            "hashtags": hashtags
        }

        files = {
            "video": open(video_path, "rb")
        }

        try:
            print(f"Posting {filename} to Postiz...")
            response = requests.post(POSTIZ_API_URL, data=data, files=files, proxies=PROXIES)
            if response.status_code == 200:
                print(f"Successfully posted {filename}")
            else:
                print(f"Failed to post {filename}: {response.status_code} {response.text}")
        except Exception as e:
            print(f"Error posting {filename}: {e}")
