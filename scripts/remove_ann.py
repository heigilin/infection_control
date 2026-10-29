# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

replacements_idx = [
    ('⚡ 1. 秒查 ANN 隔離醫囑代碼', '⚡ 1. 秒查隔離醫囑與規範'),
    ('開立對應 MDRO 接觸隔離醫囑（ANN 代碼）', '開立對應 MDRO 接觸隔離醫囑'),
    ('見 MDRO 即刻開立 ANN 隔離醫囑', '見 MDRO 即刻開立隔離醫囑'),
    ('① 醫師立即開立隔離醫囑（ANN 代碼）', '① 醫師立即開立隔離醫囑'),
    ('第一時間開立 ANN 隔離醫囑', '第一時間開立隔離醫囑'),
    ('開立對應 MDRO 隔離醫囑（ANN 代碼）', '開立對應 MDRO 隔離醫囑'),
    ('秒查 <strong>ANN 隔離醫囑代碼</strong>', '秒查 <strong>隔離醫囑與規範</strong>')
]

for old, new in replacements_idx:
    if old in text:
        text = text.replace(old, new)
        print(f"index.html: replaced '{old}' -> '{new}'")
    else:
        print(f"WARNING index.html: '{old}' not found!")

with open('感控不踩雷網站/index.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(text)

# 2. Update presentation.html
with open('感控不踩雷網站/presentation.html', 'r', encoding='utf-8') as f:
    p_text = f.read()

replacements_p = [
    ('秒查 ANN 醫囑代碼、口袋 PPE 防呆', '秒查隔離醫囑、口袋 PPE 防呆'),
    ('1. 一秒速查 ANN 隔離醫囑代碼', '1. 一秒速查隔離醫囑與規範'),
    ('立即跳出 ANN000XX 隔離醫囑代碼與解隔條件', '立即跳出對應隔離醫囑類別、防護重點與解隔條件'),
    ('<strong>⚡ 秒查醫囑代碼：</strong>輸入菌名即跳出 ANN 隔離醫囑代碼與解隔條件。', '<strong>⚡ 秒查隔離規範：</strong>輸入菌名即跳出對應隔離醫囑與解隔條件。'),
    ('醫師立開 ANN 隔離醫囑 ➔', '醫師立開隔離醫囑 ➔'),
    ('⚡ 1. 秒查 ANN 隔離醫囑代碼（解決 HIS 代碼記不住）：', '⚡ 1. 秒查隔離醫囑（解決各菌種隔離規範難記問題）：'),
    ('立即跳出對應 ANN 隔離醫囑代碼與解隔條件', '立即跳出對應隔離醫囑與解隔條件'),
    ('開立對應 MDRO 隔離醫囑（ANN 代碼）', '開立對應 MDRO 隔離醫囑')
]

for old, new in replacements_p:
    if old in p_text:
        p_text = p_text.replace(old, new)
        print(f"presentation.html: replaced '{old}' -> '{new}'")
    else:
        print(f"WARNING presentation.html: '{old}' not found!")

with open('感控不踩雷網站/presentation.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(p_text)

print("Done updating index.html and presentation.html!")
