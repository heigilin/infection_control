import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

targets = [
    'btnNextStep',
    'btnPrevStep',
    'btnOpenDex',
    'learnSection',
    'quizSetupSection',
    'stepField',
    'stepRole',
    'stepScene'
]

for t in targets:
    print(f"=== References to {t} ===")
    for i, line in enumerate(lines, 1):
        if t in line:
            print(f"{i}: {line.strip()}")
