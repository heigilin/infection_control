import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'arena' in line.lower() or 'duel' in line.lower() or 'monster' in line.lower():
        print(f"Line {i+1}: {line.strip()[:100]}")
