import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all occurrences of .addEventListener
pattern = r'([a-zA-Z0-9_\.\[\]\(\)\'\"]+)\.addEventListener\('
matches = re.finditer(pattern, text)

for m in matches:
    caller = m.group(1)
    # find line number
    pos = m.start()
    line_no = text[:pos].count('\n') + 1
    # print line
    line = text.split('\n')[line_no - 1].strip()
    print(f"Line {line_no}: {caller} -> {line[:80]}")
