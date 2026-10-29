import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['感控不踩雷網站/presentation.html', '感控不踩雷網站/index.html', '感控不踩雷網站/admin.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        if '手部衛生' in line:
            for phrase in ['手部衛生管灌', '手部衛生與管灌', '手部衛生核心規範 ＆ 管灌常見錯誤防杜', '手部衛生三大核心 ＆ 管灌常見錯誤防杜']:
                if phrase in line:
                    print(f"{fname}:{idx+1} -> {line.strip()[:100]}")
