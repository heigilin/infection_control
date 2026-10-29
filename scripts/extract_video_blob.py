import subprocess
import shutil

p = subprocess.run(['git', 'cat-file', '-p', 'hh_repo/main:handwashing_training_web.mp4'], capture_output=True)
data = p.stdout

print(f"Read {len(data)} bytes from git cat-file.")

for target in ['assets/videos/handwashing_training_web.mp4', '感控不踩雷網站/assets/videos/handwashing_training_web.mp4']:
    with open(target, 'wb') as f:
        f.write(data)
    print(f"Wrote {target} ({len(data)} bytes).")
