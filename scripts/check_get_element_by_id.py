import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all getElementById in script tags
scripts = re.findall(r'<script.*?</script>', text, re.DOTALL)
script_text = '\n'.join(scripts)

ids = re.findall(r"document\.getElementById\(['\"]([^'\"]+)['\"]\)", script_text)
ids = sorted(list(set(ids)))

missing = []
found = []
for el_id in ids:
    # check if id="el_id" or id='el_id' is in html
    pattern = rf'id=[\'"]{re.escape(el_id)}[\'"]'
    if re.search(pattern, text):
        found.append(el_id)
    else:
        missing.append(el_id)

print(f"Total IDs in getElementById: {len(ids)}")
print(f"Found: {len(found)}")
print(f"Missing ({len(missing)}):")
for m in missing:
    print(f"  - {m}")
