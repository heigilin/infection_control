import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<header' in line or 'class="header' in line or 'class="brand' in line:
        print(f"Line {i+1}: {line.strip()[:100]}")
    if i < 200 and 'header' in line:
        print(f"CSS Line {i+1}: {line.strip()[:100]}")
