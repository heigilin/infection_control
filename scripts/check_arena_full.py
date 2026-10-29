import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect arena html
m = re.search(r'<!-- ===== 考題對決戰場 ARENA ===== -->[\s\S]*?<!-- ===== 認證證書與結果彈窗 ===== -->', content)
if m:
    print('=== ARENA HTML ===')
    print(m.group(0)[:1500])

# Let's inspect renderDuel and selectDuelAnswer
m2 = re.search(r'function renderDuel\(\)[\s\S]*?function finishDuels', content)
if m2:
    print('\n=== RENDER DUEL & SELECT DUEL ANSWER ===')
    print(m2.group(0)[:2000])
