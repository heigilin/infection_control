import os

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for f in files:
        fp = os.path.join(root, f)
        try:
            sz = os.path.getsize(fp)
            if sz > 20 * 1024 * 1024:
                print(f"Large file: {fp} ({sz / 1024 / 1024:.2f} MB)")
        except Exception:
            pass
