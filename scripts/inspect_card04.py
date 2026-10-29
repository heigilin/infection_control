import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<!-- 卡片 04[\s\S]*?</article>', text)
if m:
    print(m.group(0))
