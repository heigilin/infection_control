import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect video properties
import subprocess
try:
    result = subprocess.run([
        'ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',
        '感控不踩雷網站/assets/videos/溼洗手.mp4'
    ], capture_output=True, text=True)
    print("Video duration (seconds):", result.stdout.strip())
except Exception as e:
    print("ffprobe error or not found:", e)
