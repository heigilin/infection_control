import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'function saveRecord[\s\S]*?function', content)
if m:
    print('=== saveRecord ===\n', m.group(0))

m2 = re.search(r'function renderResult[\s\S]*?function', content)
if m2:
    print('=== renderResult ===\n', m2.group(0)[:1500])

m3 = re.search(r'<div id="results"[\s\S]*?</section>', content)
if m3:
    print('=== results DOM ===\n', m3.group(0)[:1500])
