import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '手部衛生' in line or '濕洗手' in line or 'learn-card' in line and i < 2000:
        if any(k in line for k in ['章節 04', '手部衛生', 'HH', '乾洗手', '濕洗手']):
            print(f"Line {i+1}: {line.strip()[:100]}")
