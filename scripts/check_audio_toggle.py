import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'btnAudioToggle' in l or 'toggleAudio' in l:
        print(f"{i+1}: {l.strip()}")
