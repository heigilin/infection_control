import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/presentation.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'tag:\s*"章節 04[^\"]*"[\s\S]*?points:\s*`[\s\S]*?`', text)
if m:
    print(m.group(0))
