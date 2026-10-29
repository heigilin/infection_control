import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '''    // 初始化玩家名稱
    if (state.nick) playerNickInput.value = state.nick;'''

replacement = '''    // 初始化玩家名稱與病房單位
    const playerWardInput = document.getElementById('playerWard');
    const stepRoleWardInput = document.getElementById('stepRoleWard');

    if (state.nick) playerNickInput.value = state.nick;
    if (state.ward) {
      if (playerWardInput) playerWardInput.value = state.ward;
      if (stepRoleWardInput) stepRoleWardInput.value = state.ward;
    }

    if (playerNickInput) {
      playerNickInput.addEventListener('input', () => {
        state.nick = playerNickInput.value.trim();
        localStorage.setItem('ntuh_guardian_nick', state.nick);
      });
    }

    // 雙向即時同步側邊欄與步驟 2 的病房輸入
    if (playerWardInput && stepRoleWardInput) {
      playerWardInput.addEventListener('input', () => {
        state.ward = playerWardInput.value.trim();
        stepRoleWardInput.value = playerWardInput.value;
        localStorage.setItem('ntuh_guardian_ward', state.ward);
      });
      stepRoleWardInput.addEventListener('input', () => {
        state.ward = stepRoleWardInput.value.trim();
        playerWardInput.value = stepRoleWardInput.value;
        localStorage.setItem('ntuh_guardian_ward', state.ward);
      });
    }'''

assert target in content, "target not found in index.html"
content = content.replace(target, replacement)

with open('感控不踩雷網站/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated playerWard wiring in 感控不踩雷網站/index.html")
