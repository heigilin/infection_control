import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'playerNickInput' in line:
        for j in range(max(0, i-2), min(len(lines), i+8)):
            print(f"{j+1}: {lines[j]}", end='')
