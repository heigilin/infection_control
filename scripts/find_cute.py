import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'assets' in root or 'output' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.js', '.json', '.gs', '.py')):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if '可愛' in content:
                    lines = content.splitlines()
                    for idx, line in enumerate(lines):
                        if '可愛' in line:
                            print(f"{path}:{idx+1} -> {line.strip()[:120]}")
            except Exception as e:
                pass
