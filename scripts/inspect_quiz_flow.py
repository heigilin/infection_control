with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'btnStartAdventure' in line and 'addEventListener' in line:
        for j in range(max(0, i-5), min(len(lines), i+35)):
            print(f"{j+1}: {repr(lines[j].strip())}")
        break
