import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('=== STEP ROLE FULL ===')
m = re.search(r'<div id="stepRole"[\s\S]*?</div>\s*</div>\s*</div>', content)
if m:
    print(m.group(0))

print('\n=== RECORD SAVING & CERTIFICATE ===')
m2 = re.search(r'function showResults[\s\S]*?function', content)
if m2:
    print(m2.group(0)[:1500])

print('\n=== RECORD STORAGE KEYS ===')
matches = re.findall(r'localStorage\.[a-zA-Z]+\([^\)]+\)', content)
for match in matches:
    print(match)
