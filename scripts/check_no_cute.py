import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

found = 0
for fpath in ['感控不踩雷網站/index.html', '感控不踩雷網站/presentation.html', 'index.html', 'presentation.html', 'learning.html', 'admin.html']:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    c = content.count('可愛')
    if c > 0:
        print(f"ERROR: {fpath} has {c} occurrences of '可愛'")
        found += c

if found == 0:
    print("SUCCESS: 0 occurrences of '可愛' found in all active HTML files!")
