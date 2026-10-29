import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Destination directories
dest_dirs = [
    '感控不踩雷網站/assets',
    'assets'
]

for d in dest_dirs:
    os.makedirs(os.path.join(d, 'videos'), exist_ok=True)
    os.makedirs(os.path.join(d, 'images', 'hand_hygiene'), exist_ok=True)

# 1. Copy video
video_src = r'E:\影片成品\溼洗手.mp4'
if os.path.exists(video_src):
    print("Copying video:", video_src)
    for d in dest_dirs:
        dest_video = os.path.join(d, 'videos', '溼洗手.mp4')
        if not os.path.exists(dest_video) or os.path.getsize(dest_video) != os.path.getsize(video_src):
            shutil.copy2(video_src, dest_video)
            print(f"  -> Copied to {dest_video} ({os.path.getsize(dest_video)} bytes)")
        else:
            print(f"  -> Already exists at {dest_video}")
else:
    print("Video source not found:", video_src)

# 2. Copy photos from E:\HH影片
hh_src_dir = r'E:\HH影片'
if os.path.exists(hh_src_dir):
    print("Copying HH images from:", hh_src_dir)
    for f in sorted(os.listdir(hh_src_dir)):
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            src_f = os.path.join(hh_src_dir, f)
            for d in dest_dirs:
                dest_f = os.path.join(d, 'images', 'hand_hygiene', f)
                if not os.path.exists(dest_f) or os.path.getsize(dest_f) != os.path.getsize(src_f):
                    shutil.copy2(src_f, dest_f)
            print(f"  -> Copied {f}")
else:
    print("HH dir not found:", hh_src_dir)

print("Copy completed!")
