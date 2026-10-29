import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Find main structural elements inside <main id="home">
in_home = False
for i, line in enumerate(lines):
    if '<main id="home">' in line:
        in_home = True
    if in_home:
        if any(tag in line for tag in ['<div class="site-flow-roadmap"', '<header class="masthead"', '<div class="phase-bar"', '<div class="home-grid"', '<section id="phaseQuiz"', '<div class="setup-box"', '<div id="arena"', '<section class="ward-3d-wrapper"', '<div class="learn-cards-grid"']):
            print(f"Line {i+1}: {line.strip()[:100]}")
    if '</main>' in line:
        in_home = False
