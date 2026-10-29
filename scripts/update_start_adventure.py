with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_start = """    function startAdventure() {
      state.nick = playerNickInput.value.trim() || '雅琪';
      const inputWard = (playerWardInput ? playerWardInput.value.trim() : '') || (stepRoleWardInput ? stepRoleWardInput.value.trim() : '');
      state.ward = inputWard || state.ward || '5B 病房';
      if (state.role === '其他') {
        state.customRole = customRoleInput.value.trim() || '醫事同仁';
      }
      localStorage.setItem('ntuh_guardian_nick', state.nick);
      localStorage.setItem('ntuh_guardian_ward', state.ward);

      const displayRole = state.role === '其他' && state.customRole ? state.customRole : state.role;
      hudPlayerName.textContent = `${state.nick} · ${state.ward} (${displayRole})`;
      const roleIcons = { '護理師': '🩺', '醫師': '👨‍⚕️', '清潔人員': '🧹', '其他': '🌟' };
      hudRoleIcon.textContent = roleIcons[state.role] || '🌟';

      state.currentQ = 0;
      state.score = 0;
      state.shield = 100;
      state.mistakes = [];
      updateHp();

      // 隱藏首頁與頂部導航列，啟動沉浸式全螢幕 3D 病房實境大世界！
      document.getElementById('home').style.display = 'none';
      const topNavEl = document.querySelector('.top-nav');
      if (topNavEl) topNavEl.style.display = 'none';
      document.getElementById('ward3DContainer').classList.remove('hidden');
      sound.play('click');

      // 初始化 3D 病房 RPG 世界與角色
      initWard3DWorld();
      resetWardActors();
    }

    document.getElementById('btnStartAdventure').addEventListener('click', startAdventure);"""

new_start = """    function startAdventure() {
      state.nick = (playerNickInput ? playerNickInput.value.trim() : '') || '雅琪';
      const inputWard = (playerWardInput ? playerWardInput.value.trim() : '') || (stepRoleWardInput ? stepRoleWardInput.value.trim() : '');
      state.ward = inputWard || state.ward || '5B 病房';
      if (state.role === '其他') {
        state.customRole = (customRoleInput ? customRoleInput.value.trim() : '') || '醫事同仁';
      }
      localStorage.setItem('ntuh_guardian_nick', state.nick);
      localStorage.setItem('ntuh_guardian_ward', state.ward);

      const displayRole = state.role === '其他' && state.customRole ? state.customRole : state.role;
      if (hudPlayerName) hudPlayerName.textContent = `${state.nick} · ${state.ward} (${displayRole})`;
      const roleIcons = { '護理師': '🩺', '醫師': '👨‍⚕️', '清潔人員': '🧹', '其他': '🌟' };
      if (hudRoleIcon) hudRoleIcon.textContent = roleIcons[state.role] || '🌟';

      state.currentQ = 0;
      state.score = 0;
      state.shield = 100;
      state.mistakes = [];
      updateHp();

      // 隱藏首頁與頂部導航列，啟動沉浸式全螢幕 3D 病房實境大世界！
      const homeEl = document.getElementById('home');
      if (homeEl) homeEl.style.display = 'none';
      const topNavEl = document.querySelector('.top-nav');
      if (topNavEl) topNavEl.style.display = 'none';
      const wardCont = document.getElementById('ward3DContainer');
      if (wardCont) wardCont.classList.remove('hidden');
      sound.play('click');

      // 初始化 3D 病房 RPG 世界與角色
      initWard3DWorld();
      resetWardActors();
    }

    const btnStartAdventure = document.getElementById('btnStartAdventure');
    if (btnStartAdventure) {
      btnStartAdventure.addEventListener('click', startAdventure);
    }"""

if old_start in c:
    c = c.replace(old_start, new_start)
    with open('感控不踩雷網站/index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Guarded startAdventure and btnStartAdventure successfully")
else:
    print("WARNING: old_start pattern not found")
