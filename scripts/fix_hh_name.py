# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update presentation.html
with open('感控不踩雷網站/presentation.html', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    # Quick button
    ('<span class="qb-name">手部衛生管灌</span>', '<span class="qb-name">手部衛生</span>'),
    ('title="開啟：手部衛生三大核心與管灌常見錯誤防杜"', 'title="開啟：手部衛生三大核心規範與示範影音"'),
    # Meta description
    ('手部衛生管灌地雷', '手部衛生核心規範'),
    # Chapter 04 tag
    ('tag: "章節 04 · 手部衛生與管灌常見錯誤防杜"', 'tag: "章節 04 · 手部衛生核心規範"'),
    # Catalog tag
    ('<span class="tcard-tag">章節 04 · 手部衛生與管灌常見錯誤防杜</span>', '<span class="tcard-tag">章節 04 · 手部衛生核心規範</span>')
]

for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
        print(f"presentation.html: replaced '{old}' -> '{new}'")
    else:
        print(f"WARNING presentation.html: '{old}' not found!")

with open('感控不踩雷網站/presentation.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(text)

# 2. Update admin.html
with open('感控不踩雷網站/admin.html', 'r', encoding='utf-8') as f:
    adm_text = f.read()

adm_replacements = [
    ('手部衛生管灌地雷', '手部衛生核心規範'),
    ('手部衛生管灌禁忌', '手部衛生核心規範')
]

for old, new in adm_replacements:
    if old in adm_text:
        adm_text = adm_text.replace(old, new)
        print(f"admin.html: replaced '{old}' -> '{new}'")
    else:
        print(f"WARNING admin.html: '{old}' not found!")

with open('感控不踩雷網站/admin.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(adm_text)

print("Done updating presentation.html and admin.html!")
