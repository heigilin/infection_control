import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

for fpath in ['感控不踩雷網站/presentation.html', '感控不踩雷網站/admin.html']:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    scripts = re.findall(r'<script.*?</script>', text, re.DOTALL)
    script_text = '\n'.join(scripts)
    ids = re.findall(r"document\.getElementById\(['\"]([^'\"]+)['\"]\)", script_text)
    ids = sorted(list(set(ids)))
    missing = [el_id for el_id in ids if not re.search(rf'id=[\'"]{re.escape(el_id)}[\'"]', text)]
    print(f"[{fpath}] Total IDs in getElementById: {len(ids)}, Missing: {missing}")
