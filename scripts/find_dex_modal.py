import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'id=[\'\"]dexModal[\'\"]', text)]
for idx in matches:
    print("Found dexModal around char:", idx)
    start = max(0, idx - 100)
    end = min(len(text), idx + 200)
    print(text[start:end])
