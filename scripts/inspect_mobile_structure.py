import re

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

ids = re.findall(r'id=["\']([^"\']+)["\']', text)
relevant_ids = [x for x in ids if any(k in x.lower() for k in ['section', 'modal', 'duel', 'arena', 'phase', 'stage', 'quiz', 'step'])]
print('Relevant IDs:', relevant_ids)
