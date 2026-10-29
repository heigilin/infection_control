import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

for p in ['感控不踩雷網站/assets/videos/溼洗手.mp4', 'E:/影片成品/溼洗手.mp4']:
    try:
        with open(p, 'rb') as f:
            head = f.read(64)
            print(f"{p}: size={os.path.getsize(p)}, head={head[:16]}")
    except Exception as e:
        print(f"Error {p}: {e}")
