import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="stepRole"' in line or '選擇您的臨床職別身分' in line:
        for j in range(max(0, i-3), min(len(lines), i+10)):
            print(f"{j+1}: {lines[j]}", end='')
