import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.findall(r'.{0,50}(?:render3D|canvas|3D|particle).{0,50}', content, re.IGNORECASE)
for line in m[:25]:
    print('-', line.strip())

# Also check arenaEl / renderDuel
m2 = re.search(r'function renderDuel[\s\S]*?function', content)
if m2:
    print('\n=== renderDuel ===\n', m2.group(0)[:1500])
