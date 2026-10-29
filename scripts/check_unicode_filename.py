import os

for path in ['E:/影片成品', '感控不踩雷網站/assets/videos', 'assets/videos']:
    if os.path.exists(path):
        files = os.listdir(path)
        for f in files:
            chars = [f"{c} (U+{ord(c):04X})" for c in f]
            print(f"{path} -> {f} -> {' '.join(chars)}")
