import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'renderTable' in line or 'btnExportCSV' in line or 'injectTestData' in line or 'btnInjectTestData' in line:
        print(f"Line {i+1}: {line.strip()[:100]}")
