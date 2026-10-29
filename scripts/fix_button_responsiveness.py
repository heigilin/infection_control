import sys

# 1. Fix 感控不踩雷網站/index.html
with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix broken input
broken_input = '''          <input type="text" id="stepRoleWard" class="text-input" maxlength="20"
          <input type="hidden" id="playerWard"> placeholder="例如：5B 病房、7D、加護病房、急診..." style="width:100%; font-size:14px; padding:9px 12px; border-radius:8px;">'''

fixed_input = '''          <input type="text" id="stepRoleWard" class="text-input" maxlength="20" placeholder="例如：5B 病房、7D、加護病房、急診..." style="width:100%; font-size:14px; padding:9px 12px; border-radius:8px;">
          <input type="hidden" id="playerWard">'''

if broken_input in c:
    c = c.replace(broken_input, fixed_input)
    print("Fixed broken input HTML")
else:
    print("WARNING: broken input pattern not found directly, checking variations")

# Fix stepper and guards
old_stepper_code = '''    stepperLis.forEach(li => {
      li.addEventListener('click', () => {
        showStep(parseInt(li.dataset.step));
      });
    });

    btnPrevStep.addEventListener('click', () => {
      if (state.step > 1) showStep(state.step - 1);
    });

    btnNextStep.addEventListener('click', () => {
      if (state.step < 3) {
        showStep(state.step + 1);
      } else {
        startAdventure();
      }
    });'''

new_stepper_code = '''    if (stepperLis && stepperLis.length > 0) {
      stepperLis.forEach(li => {
        li.addEventListener('click', () => {
          showStep(parseInt(li.dataset.step));
        });
      });
    }

    if (btnPrevStep) {
      btnPrevStep.addEventListener('click', () => {
        if (state.step > 1) showStep(state.step - 1);
      });
    }

    if (btnNextStep) {
      btnNextStep.addEventListener('click', () => {
        if (state.step < 3) {
          showStep(state.step + 1);
        } else {
          startAdventure();
        }
      });
    }

    // 模式切換按鈕 (全方位實戰 / 極速避雷)
    const btnModeFull = document.getElementById('btnModeFull');
    const btnModeRapid = document.getElementById('btnModeRapid');
    if (btnModeFull && btnModeRapid) {
      btnModeFull.addEventListener('click', () => {
        btnModeFull.classList.add('active');
        btnModeFull.style.background = 'var(--milktea-accent)';
        btnModeFull.style.color = '#ffffff';
        btnModeFull.style.borderColor = 'var(--milktea-accent)';
        btnModeRapid.classList.remove('active');
        btnModeRapid.style.background = '#ffffff';
        btnModeRapid.style.color = 'var(--milktea-body)';
        btnModeRapid.style.borderColor = 'var(--milktea-border)';
        state.quizMode = 'full';
        sound.play('click');
      });
      btnModeRapid.addEventListener('click', () => {
        btnModeRapid.classList.add('active');
        btnModeRapid.style.background = 'var(--milktea-accent)';
        btnModeRapid.style.color = '#ffffff';
        btnModeRapid.style.borderColor = 'var(--milktea-accent)';
        btnModeFull.classList.remove('active');
        btnModeFull.style.background = '#ffffff';
        btnModeFull.style.color = 'var(--milktea-body)';
        btnModeFull.style.borderColor = 'var(--milktea-border)';
        state.quizMode = 'rapid';
        sound.play('click');
      });
    }'''

if old_stepper_code in c:
    c = c.replace(old_stepper_code, new_stepper_code)
    print("Fixed stepper and added mode button listeners")
else:
    print("WARNING: old stepper code not found directly")

# Fix btnAudioToggle & btnHudAudio listeners
old_audio_code = '''    btnAudioToggle.addEventListener('click', toggleAudio);
    btnHudAudio.addEventListener('click', toggleAudio);'''

new_audio_code = '''    if (btnAudioToggle) btnAudioToggle.addEventListener('click', toggleAudio);
    if (btnHudAudio) btnHudAudio.addEventListener('click', toggleAudio);'''

if old_audio_code in c:
    c = c.replace(old_audio_code, new_audio_code)
    print("Fixed audio toggle guards")

# Fix btnOpenDex
old_dex_code = '''    document.getElementById('btnOpenDex').addEventListener('click', showDex);
    document.getElementById('btnHudDex').addEventListener('click', showDex);'''

new_dex_code = '''    const btnOpenDex = document.getElementById('btnOpenDex');
    if (btnOpenDex) btnOpenDex.addEventListener('click', showDex);
    const btnHudDex = document.getElementById('btnHudDex');
    if (btnHudDex) btnHudDex.addEventListener('click', showDex);'''

if old_dex_code in c:
    c = c.replace(old_dex_code, new_dex_code)
    print("Fixed btnOpenDex guards")

with open('感控不踩雷網站/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Saved 感控不踩雷網站/index.html")

# 2. Fix presentation.html
with open('感控不踩雷網站/presentation.html', 'r', encoding='utf-8') as f:
    pc = f.read()

old_p_btn = "document.getElementById('btnStartSlideShow').addEventListener('click', () => openSlide(0));"
new_p_btn = "const btnStartSlideShow = document.getElementById('btnStartSlideShow');\n    if (btnStartSlideShow) btnStartSlideShow.addEventListener('click', () => openSlide(0));"

if old_p_btn in pc:
    pc = pc.replace(old_p_btn, new_p_btn)
    with open('感控不踩雷網站/presentation.html', 'w', encoding='utf-8') as f:
        f.write(pc)
    print("Fixed presentation.html btnStartSlideShow guard")
