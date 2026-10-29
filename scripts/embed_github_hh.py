# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update presentation.html
with open('感控不踩雷網站/presentation.html', 'r', encoding='utf-8') as f:
    p_content = f.read()

old_p_block = '''          <!-- 實境示範影音教材 -->
          <div style="margin-top:16px; background:#f0fdf4; border:1.5px solid #86efac; border-radius:12px; padding:16px;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; flex-wrap:wrap; gap:6px;">
              <span style="font-weight:800; color:#166534; font-size:15px; display:flex; align-items:center; gap:6px;">
                🎬 <strong>標準濕洗手示範影片</strong>（肥皂起泡＋內外夾弓大立腕 40~60 秒）
              </span>
              <span style="background:#bbf7d0; color:#14532d; font-size:12px; font-weight:700; padding:2px 8px; border-radius:999px;">
                臺大感管臨床教材
              </span>
            </div>
            <div style="border-radius:8px; overflow:hidden; background:#000; box-shadow:0 4px 12px rgba(0,0,0,0.25); border:1px solid #10b981;">
              <video controls playsinline preload="metadata" style="width:100%; max-height:420px; display:block; object-fit:contain; background:#000;">
                <source src="assets/videos/wet_handwash.mp4" type="video/mp4">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>
            <p style="margin:8px 0 0 0; font-size:13px; color:#15803d; line-height:1.5;">
              💡 <strong>觀看指引：</strong>標準濕洗手程序：<strong>濕</strong>（水淋濕雙手塗抹肥皂）➔ <strong>搓</strong>（確實搓揉 40~60 秒，完整涵蓋掌心、指背、指縫、指節、大拇指、指尖與手腕）➔ <strong>沖</strong>（流動清水徹底沖淨泡沫）➔ <strong>捧與擦</strong>（擦手紙擦乾雙手不留水滴，用紙巾包覆關閉水龍頭）。
            </p>
          </div>'''

new_p_block = '''          <!-- 實境示範影音教材 (內嵌 GitHub 雲端播放與本機備援) -->
          <div style="margin-top:16px; background:#040d0b; border:1.5px solid #14b8a6; border-radius:12px; padding:16px; box-shadow:0 4px 16px rgba(0,0,0,0.3);">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; flex-wrap:wrap; gap:8px;">
              <span style="font-weight:800; color:#5eead4; font-size:15px; display:flex; align-items:center; gap:6px;">
                🎬 <strong>標準濕洗手示範影片</strong>（線上影音教材 ｜ 40~60 秒標準程序）
              </span>
              <div style="display:flex; align-items:center; gap:6px;">
                <a href="https://heigilin.github.io/HH/" target="_blank" rel="noopener" style="background:#0f766e; color:#ccfbf1; font-size:12px; font-weight:700; padding:2px 10px; border-radius:999px; text-decoration:none; display:inline-flex; align-items:center; gap:4px;">
                  🌐 GitHub 原站 ↗
                </a>
              </div>
            </div>

            <!-- GitHub 線上內嵌播放器 -->
            <div style="border-radius:8px; overflow:hidden; background:#000; box-shadow:0 4px 12px rgba(0,0,0,0.25); border:1px solid #10b981; position:relative; width:100%; aspect-ratio:16/9; max-height:450px;">
              <iframe src="https://heigilin.github.io/HH/" style="width:100%; height:100%; border:none; display:block;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="標準濕洗手示範影片"></iframe>
            </div>

            <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
              <span style="font-size:12.5px; color:#99f6e4;">
                💡 <strong>線上影音來源：</strong><a href="https://heigilin.github.io/HH/" target="_blank" rel="noopener" style="color:#5eead4; text-decoration:underline;">heigilin.github.io/HH</a> ｜ 支援全螢幕放大觀看
              </span>
              <button type="button" onclick="const p = document.getElementById('slideLocalVideoWrap'); if (p) { p.style.display = (p.style.display === 'none' ? 'block' : 'none'); }" style="background:transparent; border:1px solid #14b8a6; color:#99f6e4; font-size:11.5px; padding:2px 8px; border-radius:4px; cursor:pointer;">
                📁 切換本機離線播放
              </button>
            </div>

            <!-- 本機離線備援播放器 -->
            <div id="slideLocalVideoWrap" style="display:none; margin-top:12px; border-top:1px dashed #115e59; padding-top:12px;">
              <div style="font-size:12px; color:#a7f3d0; margin-bottom:6px;">本機離線高速播放器：</div>
              <video controls playsinline preload="metadata" style="width:100%; max-height:380px; display:block; object-fit:contain; background:#000; border-radius:6px;">
                <source src="assets/videos/wet_handwash.mp4" type="video/mp4">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>
          </div>'''

p_content_norm = p_content.replace('\r\n', '\n')
old_p_block_norm = old_p_block.replace('\r\n', '\n')

if old_p_block_norm in p_content_norm:
    p_content_norm = p_content_norm.replace(old_p_block_norm, new_p_block.replace('\r\n', '\n'), 1)
    with open('感控不踩雷網站/presentation.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(p_content_norm)
    print("presentation.html iframe embedded successfully.")
else:
    print("WARNING: old_p_block not found in presentation.html!")

# 2. Update index.html Chapter 04 card and openHhModal
with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

old_idx_box = '''          <!-- 實境示範影音區塊 (直接嵌入原生 HTML5 影片播放器) -->
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
          </div>'''

new_idx_box = '''          <!-- 實境示範影音區塊 (內嵌 GitHub 線上播放與本機備援) -->
          <div style="background:#040d0b; border:1.5px solid #14b8a6; border-radius:12px; padding:18px; margin-bottom:16px;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:22px;">🎬</span>
                <div>
                  <div style="font-weight:800; color:#5eead4; font-size:16px;">標準濕洗手示範影片（線上影音教材）</div>
                  <div style="font-size:12.5px; color:#99f6e4;">肥皂起泡 ＋ 內外夾弓大立腕 40~60 秒完整搓洗程序</div>
                </div>
              </div>
              <div style="display:flex; align-items:center; gap:8px;">
                <a href="https://heigilin.github.io/HH/" target="_blank" rel="noopener" style="background:#0f766e; color:#ccfbf1; font-size:12px; font-weight:700; padding:4px 12px; border-radius:999px; text-decoration:none; display:inline-flex; align-items:center; gap:4px;">
                  🌐 GitHub 原站觀看 ↗
                </a>
              </div>
            </div>

            <!-- GitHub 線上內嵌播放器 -->
            <div style="position:relative; width:100%; max-width:820px; aspect-ratio:16/9; max-height:460px; margin:0 auto; background:#000; border-radius:10px; overflow:hidden; box-shadow:0 6px 20px rgba(0,0,0,0.6); border:1px solid #115e59;">
              <iframe src="https://heigilin.github.io/HH/" style="width:100%; height:100%; border:none; display:block;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="標準濕洗手示範影片"></iframe>
            </div>

            <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; font-size:13px; color:#99f6e4;">
              <span>💡 <strong>線上影音來源：</strong><a href="https://heigilin.github.io/HH/" target="_blank" rel="noopener" style="color:#5eead4; text-decoration:underline;">heigilin.github.io/HH</a> ｜ 支援全螢幕觀看</span>
              <button type="button" onclick="const p = document.getElementById('idxLocalVideoWrap'); if (p) { p.style.display = (p.style.display === 'none' ? 'block' : 'none'); }" style="background:transparent; border:1px solid #14b8a6; color:#99f6e4; font-size:12px; padding:3px 10px; border-radius:4px; cursor:pointer;">
                📁 切換本機離線播放
              </button>
            </div>

            <!-- 本機離線備援播放器 -->
            <div id="idxLocalVideoWrap" style="display:none; margin-top:14px; border-top:1px dashed #115e59; padding-top:14px;">
              <div style="font-size:12.5px; color:#a7f3d0; margin-bottom:8px;">本機離線高速播放器：</div>
              <video controls playsinline preload="metadata" style="width:100%; max-height:400px; display:block; object-fit:contain; background:#000; border-radius:6px; margin:0 auto;">
                <source src="assets/videos/wet_handwash.mp4" type="video/mp4">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>
          </div>'''

idx_content_norm = idx_content.replace('\r\n', '\n')
old_idx_box_norm = old_idx_box.replace('\r\n', '\n')

if old_idx_box_norm in idx_content_norm:
    idx_content_norm = idx_content_norm.replace(old_idx_box_norm, new_idx_box.replace('\r\n', '\n'), 1)
    print("index.html Chapter 04 iframe embedded successfully.")
else:
    print("WARNING: old_idx_box not found in index.html!")

# Also update openHhModal in index.html to include GitHub iframe
old_modal_vid = '''          <div style="background:#f0fdf4; border:1.5px solid #86efac; border-radius:12px; padding:16px; margin-bottom:16px;">
            <h4 style="margin:0 0 8px 0; color:#166534; font-size:15px; font-weight:800; display:flex; align-items:center; gap:6px;">
              🎬 標準濕洗手實境示範影音（40~60 秒起泡與搓洗程序）
            </h4>
            <div style="border-radius:8px; overflow:hidden; background:#000; box-shadow:0 4px 12px rgba(0,0,0,0.25); border:1px solid #10b981;">
              <video controls playsinline preload="metadata" style="width:100%; max-height:420px; display:block; object-fit:contain; background:#000;">
                <source src="assets/videos/wet_handwash.mp4" type="video/mp4">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>
            <p style="margin:8px 0 0 0; font-size:13px; color:#15803d; line-height:1.5;">
              💡 <strong>觀看指引：</strong>標準濕洗手程序包含：<strong>濕</strong>（水淋濕雙手塗抹肥皂）➔ <strong>搓</strong>（確實搓揉 40~60 秒，完整涵蓋掌心、指背、指縫、指節、大拇指、指尖與手腕）➔ <strong>沖</strong>（流動清水徹底沖淨泡沫）➔ <strong>捧與擦</strong>（擦手紙擦乾雙手不留水滴，用紙巾包覆關閉水龍頭）。
            </p>
          </div>'''

new_modal_vid = '''          <div style="background:#040d0b; border:1.5px solid #14b8a6; border-radius:12px; padding:16px; margin-bottom:16px;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; flex-wrap:wrap; gap:8px;">
              <h4 style="margin:0; color:#5eead4; font-size:15px; font-weight:800; display:flex; align-items:center; gap:6px;">
                🎬 標準濕洗手示範影片（線上影音教材）
              </h4>
              <a href="https://heigilin.github.io/HH/" target="_blank" rel="noopener" style="background:#0f766e; color:#ccfbf1; font-size:12px; font-weight:700; padding:2px 10px; border-radius:999px; text-decoration:none;">
                🌐 GitHub 原站 ↗
              </a>
            </div>
            <div style="position:relative; width:100%; aspect-ratio:16/9; max-height:420px; background:#000; border-radius:8px; overflow:hidden; border:1px solid #115e59;">
              <iframe src="https://heigilin.github.io/HH/" style="width:100%; height:100%; border:none; display:block;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="標準濕洗手示範影片"></iframe>
            </div>
            <p style="margin:8px 0 0 0; font-size:12.5px; color:#99f6e4; line-height:1.5;">
              💡 <strong>觀看指引：</strong>影片託管於 GitHub Pages (<a href="https://heigilin.github.io/HH/" target="_blank" rel="noopener" style="color:#5eead4; text-decoration:underline;">heigilin.github.io/HH</a>)，示範 40~60 秒標準肥皂起泡與搓洗流程。
            </p>
          </div>'''

old_modal_vid_norm = old_modal_vid.replace('\r\n', '\n')
if old_modal_vid_norm in idx_content_norm:
    idx_content_norm = idx_content_norm.replace(old_modal_vid_norm, new_modal_vid.replace('\r\n', '\n'), 1)
    print("index.html openHhModal updated with iframe successfully.")
else:
    print("WARNING: old_modal_vid not found in index.html!")

with open('感控不踩雷網站/index.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(idx_content_norm)
print("Finished updating 感控不踩雷網站/index.html.")
