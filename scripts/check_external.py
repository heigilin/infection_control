import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

scripts = re.findall(r'<script[^>]*src=[\'"][^\'"]+[\'"]', content)
links = re.findall(r'<link[^>]*href=[\'"][^\'"]+[\'"]', content)

print('Scripts:', scripts)
print('Links:', links)
