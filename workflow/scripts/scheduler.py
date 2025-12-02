# workflow/scripts/scheduler.py

import os
import time
from postiz_client import POSTIZ_API_URL, PROXIES, os as postiz_os

VIDEOS_DIR = "../../data/videos/"
POSTED_LOG = "../../logs/workflow.log"

# Load list of videos
videos = [f for f in os.listdir(VIDEOS_DIR) if f.endswith(".mp4")]
videos.sort(reverse=True)  # 147th → oldest

# Read posted videos log
if os.path.exists(POSTED_LOG):
    with open(POSTED_LOG, "r") as f:
        posted = [line.strip() for line in f.readlines()]
else:
    posted = []

# Filter videos that haven't been posted yet
to_post = [v for v in videos if v not in posted]

# Post 10 videos/day
POSTS_PER_DAY = 10
count = 0

for video in to_post:
    if count >= POSTS_PER_DAY:
        print(f"Posted {POSTS_PER_DAY} videos today. Stopping until tomorrow.")
        break
    
    # Call the Postiz client for this video
    os.system(f"python postiz_client.py {video}")
    
    # Log the posted video
    with open(POSTED_LOG, "a") as f:
        f.write(video + "\n")
    
    count += 1
    print(f"Posted {video} ({count}/{POSTS_PER_DAY})")
    
    # Optional: delay between posts (e.g., 5 minutes)
    time.sleep(300)
