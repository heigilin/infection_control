import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '漂白水' in line or '0.1%' in line or '1000 ppm' in line or '600 ppm' in line:
        print(f"Line {i+1}: {line.strip()[:100]}")
