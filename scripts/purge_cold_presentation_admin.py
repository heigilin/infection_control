import re

PRESENTATION_FILE = '感控不踩雷網站/presentation.html'
ADMIN_FILE = '感控不踩雷網站/admin.html'

def purge_presentation():
    with open(PRESENTATION_FILE, 'r', encoding='utf-8') as f:
        t = f.read()

    # Replace cold greens & teals with milk tea
    t = t.replace('#085446', '#8e6547')
    t = t.replace('#04382e', '#6b4a32')
    t = t.replace('#0f766e', '#8e6547')
    t = t.replace('#2dd4bf', '#b87b4e')
    t = t.replace('#14b8a6', '#e8ded2')
    t = t.replace('#5eead4', '#c28233')
    t = t.replace('#99f6e4', '#826f61')
    t = t.replace('#0f241f', '#362419')
    t = t.replace('#040d0b', '#faf6f0')
    t = t.replace('#ecfdf5', '#fbf7f1')
    t = t.replace('#10b981', '#587c64')
    t = t.replace('#047857', '#587c64')

    with open(PRESENTATION_FILE, 'w', encoding='utf-8') as f:
        f.write(t)
    print("Purged cold colors from presentation.html")

def purge_admin():
    with open(ADMIN_FILE, 'r', encoding='utf-8') as f:
        t = f.read()

    t = t.replace('#085446', '#8e6547')
    t = t.replace('#04382e', '#6b4a32')
    t = t.replace('#2dd4bf', '#b87b4e')
    t = t.replace('#38bdf8', '#b87b4e')

    with open(ADMIN_FILE, 'w', encoding='utf-8') as f:
        f.write(t)
    print("Purged cold colors from admin.html")

if __name__ == '__main__':
    purge_presentation()
    purge_admin()
