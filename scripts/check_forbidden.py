import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

forbidden = ['底氣', 'ANN', '可愛', '殺菌', 'E:\\', 'Y:\\']
files = [
    '感控不踩雷網站/index.html',
    '感控不踩雷網站/learning.html',
    '感控不踩雷網站/presentation.html',
    '感控不踩雷網站/admin.html',
    './index.html',
    './learning.html',
    './presentation.html',
    './admin.html'
]

has_error = False
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    for word in forbidden:
        count = text.count(word)
        if count > 0:
            print(f"ERROR: {fpath} has {count} occurrences of '{word}'")
            has_error = True

if not has_error:
    print("SUCCESS: 0 forbidden words found across all files!")
