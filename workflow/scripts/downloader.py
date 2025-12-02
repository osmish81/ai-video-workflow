# workflow/scripts/downloader.py

import os
from pytube import YouTube, Channel

# Paths
VIDEOS_DIR = "../../data/videos/"
os.makedirs(VIDEOS_DIR, exist_ok=True)

# Your YouTube channel
CHANNEL_URL = "https://www.youtube.com/@fresh2movies"

# Get all videos
channel = Channel(CHANNEL_URL)
video_list = list(channel.videos)

# Reverse the list to start from video #147 -> oldest
video_list = list(reversed(video_list))

print(f"Total videos found: {len(video_list)}")

# Download videos starting from 147th
for index, video in enumerate(video_list, start=1):
    print(f"Downloading video {index}: {video.title}")
    try:
        video.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first().download(VIDEOS_DIR)
    except Exception as e:
        print(f"Failed to download {video.title}: {e}")
