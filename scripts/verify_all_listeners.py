import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check every addEventListener line and its surrounding context
lines = text.split('\n')
for idx, line in enumerate(lines):
    if '.addEventListener(' in line:
        # Check if caller is directly chained to document.getElementById
        m = re.search(r"document\.getElementById\(['\"]([^'\"]+)['\"]\)\.addEventListener", line)
        if m:
            el_id = m.group(1)
            # check if id is in HTML
            in_html = f'id="{el_id}"' in text
            print(f"Line {idx+1}: document.getElementById('{el_id}') direct call. In HTML: {in_html}")
        else:
            # Variable call, print it
            m2 = re.search(r"([a-zA-Z0-9_]+)\.addEventListener", line)
            if m2:
                var_name = m2.group(1)
                # print 3 lines before
                ctx = ' | '.join(lines[max(0, idx-2):idx+1])
                print(f"Line {idx+1}: {var_name}.addEventListener. Context: {ctx.strip()[:120]}")
