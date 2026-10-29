import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'assets' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.js', '.json', '.gs', '.py')):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if '手部衛生管灌' in content:
                    lines = content.splitlines()
                    for idx, line in enumerate(lines):
                        if '手部衛生管灌' in line:
                            print(f"{path}:{idx+1} -> {line.strip()[:120]}")
            except Exception as e:
                pass
