import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
print('=== THEAD in admin.html ===')
m = re.search(r'<thead>[\s\S]*?</thead>', content)
if m:
    print(m.group(0))

print('=== renderTable in admin.html ===')
m2 = re.search(r'function renderTable[\s\S]*?function', content)
if m2:
    print(m2.group(0)[:1500])

print('=== CSV EXPORT in admin.html ===')
m3 = re.search(r'btnExportCSV[\s\S]*?\}\);', content)
if m3:
    print(m3.group(0)[:1500])

print('=== SAMPLE DATA in admin.html ===')
m4 = re.search(r'function initSampleData[\s\S]*?function', content)
if m4:
    print(m4.group(0)[:1000])
