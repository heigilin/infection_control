import re

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()

for i, line in enumerate(lines):
    if 'canvas' in line.lower() and 'world' in line.lower():
        print(f"Line {i+1}: {line}")
    if 'function initworld' in line.lower() or 'initbackground' in line.lower():
        print(f"Line {i+1}: {line}")
