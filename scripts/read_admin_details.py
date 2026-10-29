import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(925, min(len(lines), 1125)):
    print(f"{i+1}: {lines[i]}", end='')
