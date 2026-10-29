import os
import shutil

fast = '感控不踩雷網站/assets/videos/溼洗手_faststart.mp4'

targets = [
    '感控不踩雷網站/assets/videos/溼洗手.mp4',
    '感控不踩雷網站/assets/videos/wet_handwash.mp4',
    'assets/videos/溼洗手.mp4',
    'assets/videos/wet_handwash.mp4'
]

for t in targets:
    shutil.copy2(fast, t)
    print(f"Updated {t} ({os.path.getsize(t)} bytes)")

os.remove(fast)
print("Removed temp faststart file.")
