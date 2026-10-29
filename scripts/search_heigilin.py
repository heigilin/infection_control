import os

for root, dirs, files in os.walk('D:/'):
    # limit depth
    if root.count(os.sep) > 5:
        continue
    for f in files:
        if 'heigilin' in f.lower() or 'heigilin' in root.lower() or f == 'CNAME' or 'HH' in f:
            print(f"Found: {os.path.join(root, f)}")
