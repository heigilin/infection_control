import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['感控不踩雷網站/index.html', '感控不踩雷網站/presentation.html', '感控不踩雷網站/admin.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    matches = re.findall(r'.{0,40}ANN.{0,40}', text)
    print(f"=== {fname} ({len(matches)} matches) ===")
    for m in matches:
        print("  ...", m.strip().replace('\n', ' '), "...")
