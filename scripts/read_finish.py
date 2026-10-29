import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(2185, min(len(lines), 2370)):
    print(f"{i+1}: {lines[i]}", end='')
