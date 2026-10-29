import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'const duels = \[[\s\S]*?\];', content)
if m:
    print(m.group(0))
