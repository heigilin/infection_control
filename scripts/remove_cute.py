# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

replacements_idx = [
    ('🎬 示範影音教材 ＋ 可愛步驟圖解', '🎬 示範影音教材 ＋ 步驟圖解'),
    ('<!-- 可愛步驟圖解輔助區 (明確標記為步驟插畫，與上方影片區隔) -->', '<!-- 步驟圖解輔助區 -->'),
    ('<span>✨</span> 可愛步驟輔助插畫：肥皂水洗手 4 步驟拆解', '<span>✨</span> 步驟輔助圖解：肥皂水洗手 4 步驟拆解'),
    ('【標準濕洗手示範影片 ＆ 可愛步驟圖解】', '【標準濕洗手示範影片 ＆ 步驟圖解】'),
    ('✨ 可愛步驟圖解：濕洗手 4 步驟', '✨ 步驟圖解：濕洗手 4 步驟'),
    ('🖐️ 洗手 5 時機可愛圖解 (WHO Hand Hygiene Moments)', '🖐️ 洗手 5 大時機圖解 (WHO Hand Hygiene Moments)'),
    ("openDialog('<span>🎬</span> 標準濕洗手示範影片 ＆ 可愛步驟圖解'", "openDialog('<span>🎬</span> 標準濕洗手示範影片 ＆ 步驟圖解'"),
    ('🎬 觀看標準濕洗手示範影音 ＆ 可愛圖解 ➔', '🎬 觀看標準濕洗手示範影音 ＆ 步驟圖解 ➔')
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
    ('🎬 附：標準濕洗手實境影音 ＆ 可愛步驟圖解', '🎬 附：標準濕洗手實境影音 ＆ 步驟圖解'),
    ('<!-- 可愛步驟圖解畫廊 -->', '<!-- 步驟圖解畫廊 -->'),
    ('✨ <strong>可愛步驟圖解：濕洗手 4 步驟</strong>', '✨ <strong>步驟圖解：濕洗手 4 步驟</strong>'),
    ('<!-- 洗手五時機可愛圖解 -->', '<!-- 洗手五時機圖解 -->'),
    ('🖐️ <strong>洗手 5 時機可愛圖解 (WHO Hand Hygiene Moments)</strong>', '🖐️ <strong>洗手 5 大時機圖解 (WHO Hand Hygiene Moments)</strong>')
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
