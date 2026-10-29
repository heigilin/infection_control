# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update presentation.html
with open('感控不踩雷網站/presentation.html', 'r', encoding='utf-8') as f:
    p_content = f.read()

# Replace video tag in slidesData[4] to remove poster and add both sources
old_p_video = '''            <div style="border-radius:8px; overflow:hidden; background:#000; box-shadow:0 4px 12px rgba(0,0,0,0.15);">
              <video controls preload="metadata" poster="assets/images/hand_hygiene/01_hand_hygiene_cover.png" style="width:100%; max-height:360px; display:block; object-fit:contain;">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>'''

new_p_video = '''            <div style="border-radius:8px; overflow:hidden; background:#000; box-shadow:0 4px 12px rgba(0,0,0,0.25); border:1px solid #10b981;">
              <video controls playsinline preload="metadata" style="width:100%; max-height:420px; display:block; object-fit:contain; background:#000;">
                <source src="assets/videos/wet_handwash.mp4" type="video/mp4">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>'''

p_content_norm = p_content.replace('\r\n', '\n')
old_p_video_norm = old_p_video.replace('\r\n', '\n')

if old_p_video_norm in p_content_norm:
    p_content_norm = p_content_norm.replace(old_p_video_norm, new_p_video.replace('\r\n', '\n'), 1)
    with open('感控不踩雷網站/presentation.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(p_content_norm)
    print("presentation.html video updated successfully.")
else:
    print("WARNING: old_p_video not found in presentation.html!")

# 2. Update index.html
with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Replace Chapter 04 learn-card with featured full-width card with embedded video player
old_idx_card = '''        <!-- 章節 04 (手部衛生三大實戰核心) -->
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

new_idx_card = '''        <!-- 章節 04 (手部衛生三大實戰核心 ＆ 標準示範影片) -->
        <article class="learn-card" style="grid-column: 1 / -1; border: 2px solid var(--accent); background: linear-gradient(180deg, #0f241f 0%, #091310 100%); box-shadow: 0 8px 30px rgba(15,118,110,0.3);">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
            <h4 style="margin:0; font-size:18px;"><span>🚨</span> 章節 04：手部衛生核心規範 ＆ 標準濕洗手示範影片</h4>
            <span style="background:var(--accent); color:#fff; font-size:12.5px; font-weight:800; padding:4px 12px; border-radius:999px;">
              🎬 示範影音教材 ＋ 可愛步驟圖解
            </span>
          </div>

          <p style="margin-bottom:16px;">
            • <strong>① 接觸不同病人之間必洗手：</strong>離開床位 A 洗手，接觸床位 B 前洗手。戴手套絕對無法取代洗手！<br>
            • <strong>② 搓揉秒數一定要夠：</strong><strong>乾洗手確實搓揉 20~30 秒至完全乾燥</strong>；<strong>濕洗手確實搓揉 40~60 秒充分起泡沖乾</strong>！時間不足無法有效移除暫時性菌叢！<br>
            • <strong>③ 接觸血體液優先濕洗手：</strong>手部接觸病人血液、體液、引流液、排泄物、分泌物或有髒污，<strong>優先以肥皂與流動水濕洗手</strong>物理帶走污染源！<br>
            • <strong style="color:#ef4444;">🚨 臨床常見重大錯誤：</strong><strong>嚴禁在接觸病人呼吸道分泌物、引流液、排泄物或髒汙布品後，未洗手直接進行餵食或管灌 (Tube Feeding)！</strong>接觸髒污後 ➔ 先脫手套 ➔ 徹底洗手 (秒數要夠) ➔ 重新清潔準備 ➔ 方可管灌！
          </p>

          <!-- 實境示範影音區塊 (直接嵌入原生 HTML5 影片播放器) -->
          <div style="background:#040d0b; border:1.5px solid #14b8a6; border-radius:12px; padding:18px; margin-bottom:16px;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:22px;">🎬</span>
                <div>
                  <div style="font-weight:800; color:#5eead4; font-size:16px;">標準濕洗手示範影片（示範教材）</div>
                  <div style="font-size:12.5px; color:#99f6e4;">肥皂起泡 ＋ 內外夾弓大立腕 40~60 秒完整搓洗程序</div>
                </div>
              </div>
              <span style="background:#0f766e; color:#ccfbf1; font-size:12px; font-weight:700; padding:3px 10px; border-radius:999px;">
                ▶ 原生 HTML5 影音播放器
              </span>
            </div>

            <div style="position:relative; width:100%; max-width:820px; margin:0 auto; background:#000; border-radius:10px; overflow:hidden; box-shadow:0 6px 20px rgba(0,0,0,0.6); border:1px solid #115e59;">
              <video controls playsinline preload="metadata" style="width:100%; max-height:460px; display:block; object-fit:contain; background:#000;">
                <source src="assets/videos/wet_handwash.mp4" type="video/mp4">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>

            <div style="margin-top:10px; text-align:center; font-size:13px; color:#99f6e4;">
              💡 <strong>觀看提示：</strong>點擊播放鍵 ▶ 即可直接播放完整教學影片，支援全螢幕 ⛶、進度拖曳與音量控制。
            </div>
          </div>

          <!-- 可愛步驟圖解輔助區 (明確標記為步驟插畫，與上方影片區隔) -->
          <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.12); border-radius:10px; padding:14px;">
            <div style="font-size:14px; font-weight:800; color:#fde047; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
              <span>✨</span> 可愛步驟輔助插畫：肥皂水洗手 4 步驟拆解
            </div>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:10px;">
              <div style="border-radius:8px; overflow:hidden; border:1px solid rgba(255,255,255,0.15); background:#0f172a; text-align:center;">
                <img src="assets/images/hand_hygiene/02_step1_wet_soap_up.png" alt="步驟一：濕與抹肥皂" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="font-size:12px; font-weight:700; color:#cbd5e1; padding:4px 2px;">① 濕抹肥皂</div>
              </div>
              <div style="border-radius:8px; overflow:hidden; border:1px solid rgba(255,255,255,0.15); background:#0f172a; text-align:center;">
                <img src="assets/images/hand_hygiene/03_step2_scrub_20_seconds.png" alt="步驟二：搓揉起泡" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="font-size:12px; font-weight:700; color:#cbd5e1; padding:4px 2px;">② 搓 40~60秒</div>
              </div>
              <div style="border-radius:8px; overflow:hidden; border:1px solid rgba(255,255,255,0.15); background:#0f172a; text-align:center;">
                <img src="assets/images/hand_hygiene/04_step3_rinse_thoroughly.png" alt="步驟三：清水徹底沖洗" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="font-size:12px; font-weight:700; color:#cbd5e1; padding:4px 2px;">③ 流水沖淨</div>
              </div>
              <div style="border-radius:8px; overflow:hidden; border:1px solid rgba(255,255,255,0.15); background:#0f172a; text-align:center;">
                <img src="assets/images/hand_hygiene/05_step4_dry_gently.png" alt="步驟四：捧水關栓並擦乾" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="font-size:12px; font-weight:700; color:#cbd5e1; padding:4px 2px;">④ 紙巾擦乾</div>
              </div>
              <div style="border-radius:8px; overflow:hidden; border:1px solid rgba(255,255,255,0.15); background:#0f172a; text-align:center;">
                <img src="assets/images/hand_hygiene/06_protect_each_other.png" alt="保護病患守護自己" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="font-size:12px; font-weight:700; color:#cbd5e1; padding:4px 2px;">⑤ 守護彼此健康</div>
              </div>
            </div>
          </div>
        </article>'''

# Also update openHhModal video tag inside index.html
old_modal_video = '''            <div style="border-radius:8px; overflow:hidden; background:#000; box-shadow:0 4px 12px rgba(0,0,0,0.15);">
              <video controls preload="metadata" poster="assets/images/hand_hygiene/01_hand_hygiene_cover.png" style="width:100%; max-height:360px; display:block; object-fit:contain;">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>'''

new_modal_video = '''            <div style="border-radius:8px; overflow:hidden; background:#000; box-shadow:0 4px 12px rgba(0,0,0,0.25); border:1px solid #10b981;">
              <video controls playsinline preload="metadata" style="width:100%; max-height:420px; display:block; object-fit:contain; background:#000;">
                <source src="assets/videos/wet_handwash.mp4" type="video/mp4">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>'''

idx_content_norm = idx_content.replace('\r\n', '\n')
old_idx_card_norm = old_idx_card.replace('\r\n', '\n')
old_modal_video_norm = old_modal_video.replace('\r\n', '\n')

if old_idx_card_norm in idx_content_norm:
    idx_content_norm = idx_content_norm.replace(old_idx_card_norm, new_idx_card.replace('\r\n', '\n'), 1)
    print("index.html Chapter 04 card updated successfully.")
else:
    print("WARNING: old_idx_card not found in index.html!")

if old_modal_video_norm in idx_content_norm:
    idx_content_norm = idx_content_norm.replace(old_modal_video_norm, new_modal_video.replace('\r\n', '\n'), 1)
    print("index.html modal video updated successfully.")
else:
    print("WARNING: old_modal_video not found in index.html!")

with open('感控不踩雷網站/index.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(idx_content_norm)
print("Finished updating 感控不踩雷網站/index.html.")
