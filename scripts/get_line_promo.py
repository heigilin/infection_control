import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/presentation.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<section class="line-promo-section"[\s\S]*?</section>', text)
if m:
    print(m.group(0))
else:
    print("Not found")
