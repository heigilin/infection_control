import sys
from PIL import Image
import os

sys.stdout.reconfigure(encoding='utf-8')

img_dir = '感控不踩雷網站/assets/images/hand_hygiene'
for f in sorted(os.listdir(img_dir)):
    p = os.path.join(img_dir, f)
    try:
        with Image.open(p) as im:
            print(f"{f}: {im.size}, format={im.format}")
    except Exception as e:
        print(f"{f}: error {e}")
