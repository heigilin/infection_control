import os

path = '感控不踩雷網站/index.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

target = 'id="stepRoleWard" class="text-input" maxlength="20"'
if target in c:
    replacement = 'id="stepRoleWard" class="text-input" maxlength="20"\n          <input type="hidden" id="playerWard">'
    c = c.replace(target, replacement, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated index.html with playerWard hidden input")
else:
    print("Target not found")
