import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '手部衛生' in line and ('04' in line or '章節' in line or '卡片' in line or '核心' in line):
        for j in range(max(0, i-2), min(len(lines), i+20)):
            print(f"{j+1}: {lines[j]}", end='')
        print('\n-------------------')
