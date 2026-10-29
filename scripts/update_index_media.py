# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Chapter 04 learn-card
old_ch4 = '''        <!-- 章節 04 (手部衛生三大實戰核心) -->
        <article class="learn-card">
          <h4><span>🚨</span> 章節 04：手部衛生核心規範 ＆ 管灌常見錯誤防杜</h4>
          <p>
            • <strong>① 接觸不同病人之間必洗手：</strong>離開床位 A 洗手，接觸床位 B 前洗手。戴手套絕對無法取代洗手！<br>
            • <strong>② 搓揉秒數一定要夠：</strong><strong>乾洗手確實搓揉 20~30 秒至完全乾燥</strong>；<strong>濕洗手確實搓揉 40~60 秒充分起泡沖乾</strong>！時間不足無法有效移除暫時性菌叢！<br>
            • <strong>③ 接觸血體液優先濕洗手：</strong>手部接觸病人血液、體液、引流液、排泄物、分泌物或有髒污，<strong>優先以肥皂與流動水濕洗手</strong>物理帶走污染源！<br>
            • <strong style="color:#ef4444;">🚨 臨床常見重大錯誤：</strong><strong>嚴禁在接觸病人呼吸道分泌物、引流液、排泄物或髒汙布品後，未洗手直接進行餵食或管灌 (Tube Feeding)！</strong>接觸髒污後 ➔ 先脫手套 ➔ 徹底洗手 (秒數要夠) ➔ 重新清潔準備 ➔ 方可管灌！
          </p>
        </article>'''

new_ch4 = '''        <!-- 章節 04 (手部衛生三大實戰核心) -->
        <article class="learn-card">
          <h4><span>🚨</span> 章節 04：手部衛生核心規範 ＆ 管灌常見錯誤防杜</h4>
          <p>
            • <strong>① 接觸不同病人之間必洗手：</strong>離開床位 A 洗手，接觸床位 B 前洗手。戴手套絕對無法取代洗手！<br>
            • <strong>② 搓揉秒數一定要夠：</strong><strong>乾洗手確實搓揉 20~30 秒至完全乾燥</strong>；<strong>濕洗手確實搓揉 40~60 秒充分起泡沖乾</strong>！時間不足無法有效移除暫時性菌叢！<br>
            • <strong>③ 接觸血體液優先濕洗手：</strong>手部接觸病人血液、體液、引流液、排泄物、分泌物或有髒污，<strong>優先以肥皂與流動水濕洗手</strong>物理帶走污染源！<br>
            • <strong style="color:#ef4444;">🚨 臨床常見重大錯誤：</strong><strong>嚴禁在接觸病人呼吸道分泌物、引流液、排泄物或髒汙布品後，未洗手直接進行餵食或管灌 (Tube Feeding)！</strong>接觸髒污後 ➔ 先脫手套 ➔ 徹底洗手 (秒數要夠) ➔ 重新清潔準備 ➔ 方可管灌！
          </p>
          <!-- 影音與可愛步驟圖解展開區 -->
          <div style="margin-top:14px; padding-top:12px; border-top:1px dashed #cbd5e1;">
            <button type="button" onclick="openHhModal()" style="background:#f0fdf4; border:1.5px solid #86efac; color:#166534; font-size:13.5px; font-weight:800; padding:8px 16px; border-radius:999px; cursor:pointer; display:inline-flex; align-items:center; gap:8px; box-shadow:0 2px 6px rgba(16,185,129,0.12); transition:transform 0.15s;">
              🎬 觀看標準濕洗手實境示範影片 (40~60秒) ＆ 可愛圖解 ➔
            </button>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:8px; margin-top:10px;">
              <div onclick="openHhModal()" style="cursor:pointer; border-radius:6px; overflow:hidden; border:1px solid #e2e8f0; background:#f8fafc;" title="點擊放大觀看">
                <img src="assets/images/hand_hygiene/02_step1_wet_soap_up.png" alt="步驟一：濕與抹肥皂" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="font-size:11.5px; font-weight:700; color:#334155; text-align:center; padding:3px;">① 濕抹肥皂</div>
              </div>
              <div onclick="openHhModal()" style="cursor:pointer; border-radius:6px; overflow:hidden; border:1px solid #e2e8f0; background:#f8fafc;" title="點擊放大觀看">
                <img src="assets/images/hand_hygiene/03_step2_scrub_20_seconds.png" alt="步驟二：搓揉起泡" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="font-size:11.5px; font-weight:700; color:#334155; text-align:center; padding:3px;">② 搓揉 40~60秒</div>
              </div>
              <div onclick="openHhModal()" style="cursor:pointer; border-radius:6px; overflow:hidden; border:1px solid #e2e8f0; background:#f8fafc;" title="點擊放大觀看">
                <img src="assets/images/hand_hygiene/04_step3_rinse_thoroughly.png" alt="步驟三：清水徹底沖洗" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="font-size:11.5px; font-weight:700; color:#334155; text-align:center; padding:3px;">③ 流水沖淨</div>
              </div>
              <div onclick="openHhModal()" style="cursor:pointer; border-radius:6px; overflow:hidden; border:1px solid #e2e8f0; background:#f8fafc;" title="點擊放大觀看">
                <img src="assets/images/hand_hygiene/05_step4_dry_gently.png" alt="步驟四：捧水關栓並擦乾" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="font-size:11.5px; font-weight:700; color:#334155; text-align:center; padding:3px;">④ 紙巾擦乾</div>
              </div>
            </div>
          </div>
        </article>'''

# 2. Update Dex Item 3
old_dex_item = '''          <div class="dex-item" style="border-left: 4px solid var(--danger);">
            <h4><span>🚨</span> 3. 手部衛生三大核心 ＆ 絕對管灌禁忌</h4>
            <p><strong>接觸不同病人之間必洗手：</strong>手套不能取代洗手！<br>
            <strong>搓揉秒數一定要夠：</strong>乾洗手 20~30 秒至乾；濕洗手 40~60 秒起泡沖乾。<br>
            <strong>接觸血體液優先濕洗手：</strong>摸到血液體液分泌物或有髒污，優先肥皂水濕洗手！<br>
            <strong>絕對禁忌：</strong><strong>嚴禁摸完分泌物、引流液或髒汙後，未洗手直接進行餵食或管灌 (Tube Feeding)！</strong></p>
          </div>'''

new_dex_item = '''          <div class="dex-item" style="border-left: 4px solid var(--danger);">
            <h4><span>🚨</span> 3. 手部衛生三大核心 ＆ 絕對管灌禁忌</h4>
            <p><strong>接觸不同病人之間必洗手：</strong>手套不能取代洗手！<br>
            <strong>搓揉秒數一定要夠：</strong>乾洗手 20~30 秒至乾；濕洗手 40~60 秒起泡沖乾。<br>
            <strong>接觸血體液優先濕洗手：</strong>摸到血液體液分泌物或有髒污，優先肥皂水濕洗手！<br>
            <strong>絕對禁忌：</strong><strong>嚴禁摸完分泌物、引流液或髒汙後，未洗手直接進行餵食或管灌 (Tube Feeding)！</strong></p>
            <div style="margin-top:8px;">
              <button type="button" onclick="openHhModal()" style="background:#f0fdf4; border:1px solid #86efac; color:#166534; font-size:12px; font-weight:800; padding:4px 12px; border-radius:999px; cursor:pointer; display:inline-flex; align-items:center; gap:6px;">
                🎬 觀看標準濕洗手示範影音 ＆ 可愛圖解 ➔
              </button>
            </div>
          </div>'''

# 3. Update NPC 淑芬 dialog
old_npc = '''        text.innerHTML = `「同仁辛苦了！歡迎來到 <strong>${state.ward || '5B病房'}</strong> 現場！<br><br>
        切記進出接觸隔離病室時，<strong>手套 ＋ 防水隔離衣</strong> 綁帶一定要繫緊，嚴禁穿著隔離衣回護理站接聽電話！<br>
        洗手搓揉時間一定要足夠（乾洗手 20~30 秒至乾、濕洗手 40~60 秒起泡沖淨），才能有效移除暫時性菌叢喔！」`;'''

new_npc = '''        text.innerHTML = `「同仁辛苦了！歡迎來到 <strong>${state.ward || '5B病房'}</strong> 現場！<br><br>
        切記進出接觸隔離病室時，<strong>手套 ＋ 防水隔離衣</strong> 綁帶一定要繫緊，嚴禁穿著隔離衣回護理站接聽電話！<br>
        洗手搓揉時間一定要足夠（乾洗手 20~30 秒至乾、濕洗手 40~60 秒起泡沖淨），才能有效移除暫時性菌叢喔！<br><br>
        <div style="margin-top:10px; padding:10px; background:#f0fdf4; border-radius:8px; border:1px solid #86efac;">
          🎬 <strong>臨床影音教材：</strong>我們為大家整理了【標準濕洗手示範影片 ＆ 可愛步驟圖解】，隨時點開複習！<br>
          <button type="button" onclick="document.getElementById('npcDialogModal').classList.add('hidden'); openHhModal();" style="margin-top:6px; background:#0f766e; color:#fff; border:none; padding:6px 14px; border-radius:6px; font-weight:800; cursor:pointer; font-size:13px;">▶ 立即播放濕洗手示範影片</button>
        </div>」`;'''

# 4. Add openHhModal function near openDialog
old_opendialog = '''    function openDialog(title, html) {
      dialogTitle.innerHTML = title;
      dialogContent.innerHTML = html;
      dialogOverlay.classList.remove('hidden');
      sound.play('click');
    }'''

new_opendialog = '''    function openDialog(title, html) {
      dialogTitle.innerHTML = title;
      dialogContent.innerHTML = html;
      dialogOverlay.classList.remove('hidden');
      sound.play('click');
    }

    function openHhModal() {
      const hhHtml = `
        <div style="padding:4px 0;">
          <div style="background:#f0fdf4; border:1.5px solid #86efac; border-radius:12px; padding:16px; margin-bottom:16px;">
            <h4 style="margin:0 0 8px 0; color:#166534; font-size:15px; font-weight:800; display:flex; align-items:center; gap:6px;">
              🎬 標準濕洗手實境示範影音（40~60 秒起泡與搓洗程序）
            </h4>
            <div style="border-radius:8px; overflow:hidden; background:#000; box-shadow:0 4px 12px rgba(0,0,0,0.15);">
              <video controls preload="metadata" poster="assets/images/hand_hygiene/01_hand_hygiene_cover.png" style="width:100%; max-height:360px; display:block; object-fit:contain;">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>
            <p style="margin:8px 0 0 0; font-size:13px; color:#15803d; line-height:1.5;">
              💡 <strong>觀看指引：</strong>標準濕洗手程序包含：<strong>濕</strong>（水淋濕雙手塗抹肥皂）➔ <strong>搓</strong>（確實搓揉 40~60 秒，完整涵蓋掌心、指背、指縫、指節、大拇指、指尖與手腕）➔ <strong>沖</strong>（流動清水徹底沖淨泡沫）➔ <strong>捧與擦</strong>（擦手紙擦乾雙手不留水滴，用紙巾包覆關閉水龍頭）。
            </p>
          </div>

          <div style="background:#faf5ff; border:1.5px solid #d8b4fe; border-radius:12px; padding:16px; margin-bottom:16px;">
            <h4 style="margin:0 0 10px 0; color:#6b21a8; font-size:15px; font-weight:800; display:flex; align-items:center; gap:6px;">
              ✨ 可愛步驟圖解：濕洗手 4 步驟
            </h4>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:10px;">
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #e9d5ff; text-align:center;">
                <img src="assets/images/hand_hygiene/02_step1_wet_soap_up.png" alt="步驟一：濕與抹肥皂" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:6px; font-size:12px; font-weight:700; color:#581c87;">① 濕 ＆ 抹肥皂</div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #e9d5ff; text-align:center;">
                <img src="assets/images/hand_hygiene/03_step2_scrub_20_seconds.png" alt="步驟二：搓揉起泡" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:6px; font-size:12px; font-weight:700; color:#581c87;">② 搓 40~60 秒</div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #e9d5ff; text-align:center;">
                <img src="assets/images/hand_hygiene/04_step3_rinse_thoroughly.png" alt="步驟三：清水徹底沖洗" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:6px; font-size:12px; font-weight:700; color:#581c87;">③ 沖 徹底沖淨</div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #e9d5ff; text-align:center;">
                <img src="assets/images/hand_hygiene/05_step4_dry_gently.png" alt="步驟四：捧水關栓並擦乾" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:6px; font-size:12px; font-weight:700; color:#581c87;">④ 捧 ＆ 紙巾擦乾</div>
              </div>
            </div>
          </div>

          <div style="background:#eff6ff; border:1.5px solid #bfdbfe; border-radius:12px; padding:16px;">
            <h4 style="margin:0 0 10px 0; color:#1e40af; font-size:15px; font-weight:800; display:flex; align-items:center; gap:6px;">
              🖐️ 洗手 5 時機可愛圖解 (WHO Hand Hygiene Moments)
            </h4>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(110px, 1fr)); gap:8px;">
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #bfdbfe; text-align:center;">
                <img src="assets/images/hand_hygiene/HH (1).png" alt="時機 1: 接觸病人前" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:4px; font-size:11px; font-weight:700; color:#1e3a8a;">1. 接觸病人前</div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #bfdbfe; text-align:center;">
                <img src="assets/images/hand_hygiene/HH (2).png" alt="時機 2: 執行清潔/無菌前" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:4px; font-size:11px; font-weight:700; color:#1e3a8a;">2. 清潔/無菌前</div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #bfdbfe; text-align:center;">
                <img src="assets/images/hand_hygiene/HH (3).png" alt="時機 3: 暴露體液後" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:4px; font-size:11px; font-weight:700; color:#1e3a8a;">3. 暴露體液後</div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #bfdbfe; text-align:center;">
                <img src="assets/images/hand_hygiene/HH (4).png" alt="時機 4: 接觸病人後" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:4px; font-size:11px; font-weight:700; color:#1e3a8a;">4. 接觸病人後</div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #bfdbfe; text-align:center;">
                <img src="assets/images/hand_hygiene/HH (5).png" alt="時機 5: 接觸環境後" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:4px; font-size:11px; font-weight:700; color:#1e3a8a;">5. 接觸環境後</div>
              </div>
            </div>
          </div>
        </div>
      `;
      openDialog('<span>🎬</span> 標準濕洗手示範影片 ＆ 可愛步驟圖解', hhHtml);
    }
    window.openHhModal = openHhModal;'''

content_norm = content.replace('\r\n', '\n')

matches = 0
if old_ch4.replace('\r\n', '\n') in content_norm:
    content_norm = content_norm.replace(old_ch4.replace('\r\n', '\n'), new_ch4.replace('\r\n', '\n'), 1)
    matches += 1
    print("1. ch4 replaced successfully.")
else:
    print("WARNING: old_ch4 not found!")

if old_dex_item.replace('\r\n', '\n') in content_norm:
    content_norm = content_norm.replace(old_dex_item.replace('\r\n', '\n'), new_dex_item.replace('\r\n', '\n'), 1)
    matches += 1
    print("2. dex_item replaced successfully.")
else:
    print("WARNING: old_dex_item not found!")

if old_npc.replace('\r\n', '\n') in content_norm:
    content_norm = content_norm.replace(old_npc.replace('\r\n', '\n'), new_npc.replace('\r\n', '\n'), 1)
    matches += 1
    print("3. npc replaced successfully.")
else:
    print("WARNING: old_npc not found!")

if old_opendialog.replace('\r\n', '\n') in content_norm:
    content_norm = content_norm.replace(old_opendialog.replace('\r\n', '\n'), new_opendialog.replace('\r\n', '\n'), 1)
    matches += 1
    print("4. opendialog replaced successfully.")
else:
    print("WARNING: old_opendialog not found!")

if matches == 4:
    with open('感控不踩雷網站/index.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(content_norm)
    print("All 4 modifications written to 感控不踩雷網站/index.html!")
else:
    print(f"Only {matches}/4 modifications succeeded!")
