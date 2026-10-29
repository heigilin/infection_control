import re
import os

PRESENTATION_FILE = '感控不踩雷網站/presentation.html'
ADMIN_FILE = '感控不踩雷網站/admin.html'

def update_presentation():
    with open(PRESENTATION_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update :root variables to milk tea
    old_root = """:root {
      --ink: #0f172a;
      --ink-dark: #020617;
      --soft: #475569;
      --line: #cbd5e1;
      --accent: #085446;
      --accent-2: #04382e;
      --accent-soft: #e8f5f1;
      --gold: #b45309;
      --gold-soft: #fef3c7;
      --danger: #b91c1c;
      --danger-soft: #fee2e2;
      --paper: #ffffff;
      --bg: #f8fafc;
      --radius: 16px;
      --radius-sm: 8px;
    }"""

    new_root = """:root {
      --ink: #362419;
      --ink-dark: #26170e;
      --soft: #826f61;
      --line: #e8ded2;
      --accent: #8e6547;
      --accent-2: #6b4a32;
      --accent-soft: #fdf5ea;
      --gold: #c28233;
      --gold-soft: #fdf8f0;
      --danger: #b74f41;
      --danger-soft: #fdf3f2;
      --paper: #ffffff;
      --bg: #f8f5f0;
      --radius: 16px;
      --radius-sm: 8px;
    }"""

    html = html.replace(old_root, new_root)

    # Update ticker background
    html = html.replace('.ticker {\n      background: #0f172a;\n      color: #e2e8f0;', '.ticker {\n      background: #362419;\n      color: #fdf5ea;')
    html = html.replace('.slide-header {\n      background: #0f241f;', '.slide-header {\n      background: #362419;')

    # Update nav links to point back to the one-page index.html
    html = html.replace('href="index.html?mode=quiz"', 'href="index.html#sec-quiz"')
    html = html.replace('href="index.html"', 'href="index.html"')

    with open(PRESENTATION_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated presentation.html to milk tea palette.")

def update_admin():
    with open(ADMIN_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    old_root_pattern = r':root\s*\{[^}]+\}'
    new_root = """:root {
      --primary: #8e6547;
      --primary-dark: #6b4a32;
      --primary-light: #fdf5ea;
      --accent: #c28233;
      --accent-light: #fdf8f0;
      --danger: #b74f41;
      --danger-light: #fdf3f2;
      --warning: #d97706;
      --warning-light: #fef3c7;
      --success: #527961;
      --success-light: #f2f7f4;
      --bg: #f8f5f0;
      --card-bg: #ffffff;
      --text: #362419;
      --text-muted: #826f61;
      --border: #e8ded2;
      --shadow: 0 4px 16px rgba(89, 63, 44, 0.07);
      --radius: 14px;
    }"""

    html = re.sub(old_root_pattern, new_root, html, count=1)

    with open(ADMIN_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated admin.html to milk tea palette.")

if __name__ == '__main__':
    update_presentation()
    update_admin()
