import re

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove "↑ 返回 9 大章節速查"
text = re.sub(r'<a href="#sec-learn" class="ghost-btn"[^>]*>.*?返回 9 大章節速查.*?</a>', '', text, flags=re.DOTALL)

# 2. Remove "← 返回「第一階段：核心感控學習教材」"
text = re.sub(r'<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">\s*<button type="button" class="ghost-btn" id="btnBackToLearn".*?</button>\s*</div>', '', text, flags=re.DOTALL)

with open('感控不踩雷網站/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Cleaned back-to-learn buttons successfully')
