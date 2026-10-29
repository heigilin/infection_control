import sys

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Guard btnNextDuel
old_next_duel = """    btnNextDuel.addEventListener('click', () => {
      if (state.currentQ < duels.length - 1) {
        state.currentQ++;
        renderDuel();
        sound.play('click');
      } else {
        finishDuels();
      }
    });"""

new_next_duel = """    if (btnNextDuel) {
      btnNextDuel.addEventListener('click', () => {
        if (state.currentQ < duels.length - 1) {
          state.currentQ++;
          renderDuel();
          sound.play('click');
        } else {
          finishDuels();
        }
      });
    }"""

if old_next_duel in c:
    c = c.replace(old_next_duel, new_next_duel)
    print("Guarded btnNextDuel")

# 2. Guard btnCloseDialog & btnHudExit
old_close_dialog = """    btnCloseDialog.addEventListener('click', () => {
      dialogOverlay.classList.add('hidden');
      sound.play('click');
    });

    const btnOpenDex = document.getElementById('btnOpenDex');
    if (btnOpenDex) btnOpenDex.addEventListener('click', showDex);
    const btnHudDex = document.getElementById('btnHudDex');
    if (btnHudDex) btnHudDex.addEventListener('click', showDex);
    document.getElementById('btnHudExit').addEventListener('click', () => {
      arenaEl.classList.add('hidden');
      hudEl.classList.add('hidden');
      document.getElementById('home').style.display = 'block';
      sound.play('click');
    });"""

new_close_dialog = """    if (btnCloseDialog) {
      btnCloseDialog.addEventListener('click', () => {
        if (dialogOverlay) dialogOverlay.classList.add('hidden');
        sound.play('click');
      });
    }

    const btnOpenDex = document.getElementById('btnOpenDex');
    if (btnOpenDex) btnOpenDex.addEventListener('click', showDex);
    const btnHudDex = document.getElementById('btnHudDex');
    if (btnHudDex) btnHudDex.addEventListener('click', showDex);
    const btnHudExit = document.getElementById('btnHudExit');
    if (btnHudExit) {
      btnHudExit.addEventListener('click', () => {
        if (arenaEl) arenaEl.classList.add('hidden');
        if (hudEl) hudEl.classList.add('hidden');
        const homeEl = document.getElementById('home');
        if (homeEl) homeEl.style.display = 'block';
        sound.play('click');
      });
    }"""

if old_close_dialog in c:
    c = c.replace(old_close_dialog, new_close_dialog)
    print("Guarded btnCloseDialog & btnHudExit")

# 3. Guard 3D Ward buttons (around line 4290-4355)
old_ward_btns = """    document.getElementById('btnCloseNpcDialog').addEventListener('click', () => {
      document.getElementById('npcDialogModal').classList.add('hidden');
      sound.play('click');
    });
    document.getElementById('btnNpcDialogOk').addEventListener('click', () => {
      document.getElementById('npcDialogModal').classList.add('hidden');
      sound.play('click');
      if (currentActiveNpcTarget === 'monster') {
        startBossDuel();
      }
    });

    document.getElementById('btnQuestGo').addEventListener('click', () => {
      // 快速導航直達當前任務怪獸
      if (wardBoss && wardPlayer) {
        wardPlayer.position.x = wardBoss.position.x - 1.2;
        wardPlayer.position.z = wardBoss.position.z + 0.8;
        showNpcDialog('怪獸對決引導', '妳/你已飛身抵達怪獸面前！準備好展開對決了嗎？', 'monster');
      }
    });
    document.getElementById('btnWardCompass').addEventListener('click', () => {
      // 重置視角置中於玩家身後
      if (wardPlayer) {
        wardCamera.position.set(wardPlayer.position.x, 3.8, wardPlayer.position.z + 5.2);
        wardCamera.lookAt(wardPlayer.position.x, 1.0, wardPlayer.position.z);
        sound.play('click');
      }
    });
    document.getElementById('btnWardDex').addEventListener('click', showDex);
    document.getElementById('btnWardSound').addEventListener('click', () => {
      toggleAudio();
      document.getElementById('btnWardSound').textContent = sound.enabled ? '🔊 音效' : '🔇 靜音';
    });
    document.getElementById('btnWardExit').addEventListener('click', () => {
      cancelAnimationFrame(wardAnimId);
      document.getElementById('ward3DContainer').classList.add('hidden');
      document.getElementById('home').style.display = 'block';
      const topNav = document.querySelector('.top-nav');
      if (topNav) topNav.style.display = 'flex';
      sound.play('click');
    });
    document.getElementById('btnChangeScene').addEventListener('click', toggleWardSceneTheme);"""

new_ward_btns = """    const btnCloseNpcDialog = document.getElementById('btnCloseNpcDialog');
    if (btnCloseNpcDialog) {
      btnCloseNpcDialog.addEventListener('click', () => {
        const modal = document.getElementById('npcDialogModal');
        if (modal) modal.classList.add('hidden');
        sound.play('click');
      });
    }
    const btnNpcDialogOk = document.getElementById('btnNpcDialogOk');
    if (btnNpcDialogOk) {
      btnNpcDialogOk.addEventListener('click', () => {
        const modal = document.getElementById('npcDialogModal');
        if (modal) modal.classList.add('hidden');
        sound.play('click');
        if (currentActiveNpcTarget === 'monster') {
          startBossDuel();
        }
      });
    }

    const btnQuestGo = document.getElementById('btnQuestGo');
    if (btnQuestGo) {
      btnQuestGo.addEventListener('click', () => {
        if (wardBoss && wardPlayer) {
          wardPlayer.position.x = wardBoss.position.x - 1.2;
          wardPlayer.position.z = wardBoss.position.z + 0.8;
          showNpcDialog('怪獸對決引導', '妳/你已飛身抵達怪獸面前！準備好展開對決了嗎？', 'monster');
        }
      });
    }
    const btnWardCompass = document.getElementById('btnWardCompass');
    if (btnWardCompass) {
      btnWardCompass.addEventListener('click', () => {
        if (wardPlayer && wardCamera) {
          wardCamera.position.set(wardPlayer.position.x, 3.8, wardPlayer.position.z + 5.2);
          wardCamera.lookAt(wardPlayer.position.x, 1.0, wardPlayer.position.z);
          sound.play('click');
        }
      });
    }
    const btnWardDex = document.getElementById('btnWardDex');
    if (btnWardDex) btnWardDex.addEventListener('click', showDex);
    const btnWardSound = document.getElementById('btnWardSound');
    if (btnWardSound) {
      btnWardSound.addEventListener('click', () => {
        toggleAudio();
        btnWardSound.textContent = sound.enabled ? '🔊 音效' : '🔇 靜音';
      });
    }
    const btnWardExit = document.getElementById('btnWardExit');
    if (btnWardExit) {
      btnWardExit.addEventListener('click', () => {
        cancelAnimationFrame(wardAnimId);
        const wCont = document.getElementById('ward3DContainer');
        if (wCont) wCont.classList.add('hidden');
        const homeEl = document.getElementById('home');
        if (homeEl) homeEl.style.display = 'block';
        const topNav = document.querySelector('.top-nav');
        if (topNav) topNav.style.display = 'flex';
        sound.play('click');
      });
    }
    const btnChangeScene = document.getElementById('btnChangeScene');
    if (btnChangeScene) btnChangeScene.addEventListener('click', toggleWardSceneTheme);"""

if old_ward_btns in c:
    c = c.replace(old_ward_btns, new_ward_btns)
    print("Guarded 3D Ward buttons")

with open('感控不踩雷網站/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Saved 감控不踩雷網站/index.html")
