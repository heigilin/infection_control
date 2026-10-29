import os
import shutil

for vdir in ['感控不踩雷網站/assets/videos', 'assets/videos']:
    src = os.path.join(vdir, '溼洗手.mp4')
    dst = os.path.join(vdir, 'wet_handwash.mp4')
    if os.path.exists(src):
        if not os.path.exists(dst):
            try:
                os.link(src, dst)
                print(f"Created hardlink {dst}")
            except Exception:
                shutil.copy2(src, dst)
                print(f"Copied {dst}")
        else:
            print(f"{dst} already exists.")
