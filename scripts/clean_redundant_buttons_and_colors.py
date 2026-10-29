import re

INDEX_FILE = '感控不踩雷網站/index.html'

with open(INDEX_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the sections around main#home
home_idx = html.find('<main id="home">')
learn_idx = html.find('id="sec-learn"')

print("Length between main#home and sec-learn:", learn_idx - home_idx)
snippet = html[home_idx:learn_idx + 100]
print("--- SNIPPET BEFORE SEC-LEARN ---")
print(snippet[:600])
