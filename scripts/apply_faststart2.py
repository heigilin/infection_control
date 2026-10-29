import os
import shutil
import time

fast = '感控不踩雷網站/assets/videos/溼洗手_faststart.mp4'

for t in ['assets/videos/wet_handwash.mp4', 'assets/videos/溼洗手.mp4']:
    if os.path.exists(t):
        try:
            os.remove(t)
            print(f"Removed {t}")
        except Exception as e:
            print(f"Cannot remove {t}: {e}")

time.sleep(0.5)

for t in ['assets/videos/溼洗手.mp4', 'assets/videos/wet_handwash.mp4']:
    shutil.copy2(fast, t)
    print(f"Copied {fast} -> {t}")

if os.path.exists(fast):
    os.remove(fast)
    print("Cleaned temp faststart.")
