# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update presentation.html
with open('感控不踩雷網站/presentation.html', 'r', encoding='utf-8') as f:
    p_content = f.read()

# Update catalog card
old_catalog_p = '<p class="tcard-desc">手部衛生關鍵重點與臨床絕對禁忌：</p>'
new_catalog_p = '''<div style="margin:2px 0 10px; display:inline-flex; align-items:center; gap:6px; background:#f0fdf4; border:1px solid #86efac; color:#166534; font-size:12.5px; font-weight:700; padding:3px 10px; border-radius:999px; width:fit-content;">🎬 附：標準濕洗手實境影音 ＆ 可愛步驟圖解</div>
            <p class="tcard-desc">手部衛生關鍵重點與臨床絕對禁忌：</p>'''

if old_catalog_p in p_content:
    p_content = p_content.replace(old_catalog_p, new_catalog_p, 1)
    print("Catalog card updated successfully.")
else:
    print("WARNING: old_catalog_p not found!")

# Update slidesData[4].points
old_points_end = '''• 守護神法則：接觸髒污後 ➔ <strong>先脫除手套 ➔ 徹底洗手 (搓揉秒數要夠) ➔ 重新清潔準備 ➔ 方可管灌！</strong>
        `'''

new_media_html = '''• 守護神法則：接觸髒污後 ➔ <strong>先脫除手套 ➔ 徹底洗手 (搓揉秒數要夠) ➔ 重新清潔準備 ➔ 方可管灌！</strong><br><br>
          <!-- 實境示範影音教材 -->
          <div style="margin-top:16px; background:#f0fdf4; border:1.5px solid #86efac; border-radius:12px; padding:16px;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; flex-wrap:wrap; gap:6px;">
              <span style="font-weight:800; color:#166534; font-size:15px; display:flex; align-items:center; gap:6px;">
                🎬 <strong>標準濕洗手示範影片</strong>（肥皂起泡＋內外夾弓大立腕 40~60 秒）
              </span>
              <span style="background:#bbf7d0; color:#14532d; font-size:12px; font-weight:700; padding:2px 8px; border-radius:999px;">
                臺大感管臨床教材
              </span>
            </div>
            <div style="border-radius:8px; overflow:hidden; background:#000; box-shadow:0 4px 12px rgba(0,0,0,0.15);">
              <video controls preload="metadata" poster="assets/images/hand_hygiene/01_hand_hygiene_cover.png" style="width:100%; max-height:360px; display:block; object-fit:contain;">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>
            <p style="margin:8px 0 0 0; font-size:13px; color:#15803d; line-height:1.5;">
              💡 <strong>觀看指引：</strong>標準濕洗手程序：<strong>濕</strong>（水淋濕雙手塗抹肥皂）➔ <strong>搓</strong>（確實搓揉 40~60 秒，完整涵蓋掌心、指背、指縫、指節、大拇指、指尖與手腕）➔ <strong>沖</strong>（流動清水徹底沖淨泡沫）➔ <strong>捧與擦</strong>（擦手紙擦乾雙手不留水滴，用紙巾包覆關閉水龍頭）。
            </p>
          </div>

          <!-- 可愛步驟圖解畫廊 -->
          <div style="margin-top:16px; background:#faf5ff; border:1.5px solid #d8b4fe; border-radius:12px; padding:16px;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; flex-wrap:wrap; gap:6px;">
              <span style="font-weight:800; color:#6b21a8; font-size:15px; display:flex; align-items:center; gap:6px;">
                ✨ <strong>可愛步驟圖解：濕洗手 4 步驟</strong>
              </span>
              <span style="background:#f3e8ff; color:#7e22ce; font-size:12px; font-weight:700; padding:2px 8px; border-radius:999px;">
                精選圖解指引
              </span>
            </div>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(160px, 1fr)); gap:10px;">
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #e9d5ff; box-shadow:0 2px 6px rgba(107,33,168,0.06); text-align:center;">
                <img src="assets/images/hand_hygiene/02_step1_wet_soap_up.png" alt="步驟一：濕與抹肥皂" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:8px 4px; font-size:12.5px; font-weight:700; color:#581c87;">① 濕 ＆ 抹肥皂<br><span style="font-size:11px; font-weight:500; color:#7e22ce;">淋濕雙手塗抹肥皂</span></div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #e9d5ff; box-shadow:0 2px 6px rgba(107,33,168,0.06); text-align:center;">
                <img src="assets/images/hand_hygiene/03_step2_scrub_20_seconds.png" alt="步驟二：搓揉起泡" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:8px 4px; font-size:12.5px; font-weight:700; color:#581c87;">② 搓 40~60 秒<br><span style="font-size:11px; font-weight:500; color:#7e22ce;">內外夾弓大立腕起泡</span></div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #e9d5ff; box-shadow:0 2px 6px rgba(107,33,168,0.06); text-align:center;">
                <img src="assets/images/hand_hygiene/04_step3_rinse_thoroughly.png" alt="步驟三：清水徹底沖洗" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:8px 4px; font-size:12.5px; font-weight:700; color:#581c87;">③ 沖 徹底沖淨<br><span style="font-size:11px; font-weight:500; color:#7e22ce;">清水徹底沖淨泡沫</span></div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #e9d5ff; box-shadow:0 2px 6px rgba(107,33,168,0.06); text-align:center;">
                <img src="assets/images/hand_hygiene/05_step4_dry_gently.png" alt="步驟四：捧水關栓並擦乾" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:8px 4px; font-size:12.5px; font-weight:700; color:#581c87;">④ 捧 ＆ 紙巾擦乾<br><span style="font-size:11px; font-weight:500; color:#7e22ce;">紙巾擦乾、紙巾關栓</span></div>
              </div>
            </div>
          </div>

          <!-- 洗手五時機可愛圖解 -->
          <div style="margin-top:16px; background:#eff6ff; border:1.5px solid #bfdbfe; border-radius:12px; padding:16px;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; flex-wrap:wrap; gap:6px;">
              <span style="font-weight:800; color:#1e40af; font-size:15px; display:flex; align-items:center; gap:6px;">
                🖐️ <strong>洗手 5 時機可愛圖解 (WHO Hand Hygiene Moments)</strong>
              </span>
              <span style="background:#dbeafe; color:#1d4ed8; font-size:12px; font-weight:700; padding:2px 8px; border-radius:999px;">
                臨床守護神必備
              </span>
            </div>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:8px;">
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #bfdbfe; text-align:center;">
                <img src="assets/images/hand_hygiene/HH (1).png" alt="時機 1: 接觸病人前" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:6px; font-size:11.5px; font-weight:700; color:#1e3a8a;">1. 接觸病人前</div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #bfdbfe; text-align:center;">
                <img src="assets/images/hand_hygiene/HH (2).png" alt="時機 2: 執行清潔/無菌操作前" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:6px; font-size:11.5px; font-weight:700; color:#1e3a8a;">2. 清潔/無菌前</div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #bfdbfe; text-align:center;">
                <img src="assets/images/hand_hygiene/HH (3).png" alt="時機 3: 暴露病人體液風險後" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:6px; font-size:11.5px; font-weight:700; color:#1e3a8a;">3. 暴露體液後</div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #bfdbfe; text-align:center;">
                <img src="assets/images/hand_hygiene/HH (4).png" alt="時機 4: 接觸病人後" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:6px; font-size:11.5px; font-weight:700; color:#1e3a8a;">4. 接觸病人後</div>
              </div>
              <div style="background:#fff; border-radius:8px; overflow:hidden; border:1px solid #bfdbfe; text-align:center;">
                <img src="assets/images/hand_hygiene/HH (5).png" alt="時機 5: 接觸病人周遭環境後" style="width:100%; aspect-ratio:16/9; object-fit:cover; display:block;" loading="lazy">
                <div style="padding:6px; font-size:11.5px; font-weight:700; color:#1e3a8a;">5. 接觸環境後</div>
              </div>
            </div>
          </div>
        `'''

# Normalize newlines for matching
p_content_norm = p_content.replace('\r\n', '\n')
old_points_end_norm = old_points_end.replace('\r\n', '\n')

if old_points_end_norm in p_content_norm:
    p_content_norm = p_content_norm.replace(old_points_end_norm, new_media_html.replace('\r\n', '\n'), 1)
    with open('感控不踩雷網站/presentation.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(p_content_norm)
    print("presentation.html slidesData updated successfully.")
else:
    print("WARNING: old_points_end not found!")
