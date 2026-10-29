import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1950, 2030):
    print(f"{i+1}: {lines[i]}", end='')
