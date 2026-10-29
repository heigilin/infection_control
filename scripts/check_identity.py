import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('=== PROFILE SECTION ===')
m = re.search(r'<aside class="profile panel"[\s\S]*?</aside>', content)
if m:
    print(m.group(0))

print('\n=== STEP ROLE SECTION ===')
m2 = re.search(r'<div id="stepRole"[\s\S]*?</div>\s*</div>', content)
if m2:
    print(m2.group(0))

print('\n=== STATE & START ADVENTURE ===')
m3 = re.search(r'const state = \{[\s\S]*?\};', content)
if m3:
    print(m3.group(0))

m4 = re.search(r'function startAdventure[\s\S]*?function', content)
if m4:
    print(m4.group(0)[:1500])
