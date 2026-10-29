with open('感控不踩雷網站/presentation.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id: 4' in line or 'Ch 04' in line or '手部衛生' in line:
        print(f"Line {i+1}: {line.strip()[:100]}")
