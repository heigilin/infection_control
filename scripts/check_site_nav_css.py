import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '.site-nav' in line or '.nav-inner' in line or '.nav-brand' in line or '.nav-links' in line:
        print(f"Line {i+1}: {line.strip()[:100]}")
