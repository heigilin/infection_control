# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update presentation.html
with open('感控不踩雷網站/presentation.html', 'r', encoding='utf-8') as f:
    p_text = f.read()

# Fix CSS for .slide-modal, .slide-stage, .slide-header, .slide-footer on mobile
p_css_target = '''    /* 投影片全螢幕播放彈窗 (Slide Presentation Modal) */
    .slide-modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(8, 18, 15, 0.94);
      backdrop-filter: blur(12px);
      z-index: 200;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }
    .slide-modal.hidden { display: none; }
    .slide-stage {
      width: min(1100px, 100%);
      max-height: calc(100vh - 36px);
      height: min(860px, calc(100vh - 36px));
      background: #ffffff;
      border-radius: var(--radius);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6);
      position: relative;
    }
    .slide-header {
      background: #0f241f;
      color: #fff;
      padding: 14px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 3px solid var(--accent);
    }
    .slide-header-title {
      font-size: 15px;
      font-weight: 800;
      color: #e2f1ec;
      display: flex;
      align-items: center;
      gap: 8px;
    }'''

p_css_replacement = '''    /* 投影片全螢幕播放彈窗 (Slide Presentation Modal) */
    .slide-modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(8, 18, 15, 0.94);
      backdrop-filter: blur(12px);
      z-index: 200;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }
    .slide-modal.hidden { display: none; }
    .slide-stage {
      width: min(1100px, 100%);
      max-height: calc(100vh - 36px);
      height: min(860px, calc(100vh - 36px));
      background: #ffffff;
      border-radius: var(--radius);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6);
      position: relative;
    }
    .slide-header {
      background: #0f241f;
      color: #fff;
      padding: 12px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 3px solid var(--accent);
      gap: 10px;
    }
    .slide-header-title {
      font-size: 15px;
      font-weight: 800;
      color: #e2f1ec;
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      min-width: 0;
      flex-shrink: 0;
    }
    .slide-header-controls {
      display: flex;
      align-items: center;
      gap: 8px;
      min-width: 0;
    }

    /* 手機直向與小螢幕自適應排版 (防止標題擠壓成直行，控制鈕自動縮放) */
    @media (max-width: 768px) {
      .slide-modal {
        padding: 0;
      }
      .slide-stage {
        height: 100vh;
        max-height: 100vh;
        width: 100vw;
        border-radius: 0;
      }
      .slide-header {
        padding: 8px 12px;
        flex-direction: column;
        align-items: stretch;
        gap: 6px;
      }
      .slide-header-title {
        font-size: 13.5px;
        white-space: nowrap;
        justify-content: flex-start;
      }
      .slide-header-controls {
        display: flex;
        align-items: center;
        gap: 6px;
        width: 100%;
      }
      .slide-select {
        flex: 1;
        max-width: none;
        font-size: 12px;
        padding: 4px 6px;
      }
      .slide-close-btn {
        padding: 4px 10px;
        font-size: 12px;
        white-space: nowrap;
        flex-shrink: 0;
      }
      .slide-body {
        padding: 14px 12px;
      }
      .slide-footer {
        padding: 8px 12px;
        gap: 6px;
      }
      .slide-nav-btn {
        padding: 7px 12px;
        font-size: 12.5px;
        white-space: nowrap;
      }
      .slide-counter {
        font-size: 11.5px;
        white-space: nowrap;
      }
    }'''

p_text_norm = p_text.replace('\r\n', '\n')
p_css_target_norm = p_css_target.replace('\r\n', '\n')

if p_css_target_norm in p_text_norm:
    p_text_norm = p_text_norm.replace(p_css_target_norm, p_css_replacement.replace('\r\n', '\n'), 1)
    print("presentation.html CSS updated successfully.")
else:
    print("WARNING: p_css_target not found in presentation.html!")

# Update slide-header HTML in presentation.html
old_slide_header_html = '''      <div class="slide-header">
        <div class="slide-header-title">
          <span>🖥️</span> 臺大醫院感管簡報教材
        </div>
        <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
          <select class="slide-select" id="slideQuickSelect" title="快速跳轉至其他章節簡報"></select>
          <button class="slide-close-btn" id="btnCloseSlide" title="關閉簡報，返回章節總覽目錄">
            <span>✕</span> 返回章節總覽
          </button>
        </div>
      </div>'''

new_slide_header_html = '''      <div class="slide-header">
        <div class="slide-header-title">
          <span>🖥️ 臺大醫院感管簡報教材</span>
        </div>
        <div class="slide-header-controls">
          <select class="slide-select" id="slideQuickSelect" title="快速跳轉至其他章節簡報"></select>
          <button class="slide-close-btn" id="btnCloseSlide" title="關閉簡報，返回章節總覽目錄">
            <span>✕</span> 返回章節總覽
          </button>
        </div>
      </div>'''

old_slide_header_html_norm = old_slide_header_html.replace('\r\n', '\n')
if old_slide_header_html_norm in p_text_norm:
    p_text_norm = p_text_norm.replace(old_slide_header_html_norm, new_slide_header_html.replace('\r\n', '\n'), 1)
    print("presentation.html slide-header HTML updated successfully.")
else:
    print("WARNING: old_slide_header_html not found!")

# Update slidesData[4] video box in presentation.html
old_p_video_box = '''          <!-- 實境示範影音教材 (內嵌 GitHub 雲端播放與本機備援) -->
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

new_p_video_box = '''          <!-- 實境示範影音教材 (完整支援 GitHub 雲端串流與本地雙線路) -->
          <div style="margin-top:16px; background:#040d0b; border:1.5px solid #14b8a6; border-radius:12px; padding:16px; box-shadow:0 4px 16px rgba(0,0,0,0.3);">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; flex-wrap:wrap; gap:8px;">
              <span style="font-weight:800; color:#5eead4; font-size:15px; display:flex; align-items:center; gap:6px;">
                🎬 <strong>標準濕洗手示範影片</strong>（40~60 秒起泡與搓洗程序）
              </span>
              <div style="display:flex; align-items:center; gap:6px;">
                <a href="https://heigilin.github.io/HH/" target="_blank" rel="noopener" style="background:#0f766e; color:#ccfbf1; font-size:12px; font-weight:700; padding:2px 10px; border-radius:999px; text-decoration:none; display:inline-flex; align-items:center; gap:4px;">
                  🌐 互動教學站 ↗
                </a>
              </div>
            </div>

            <!-- 原生 HTML5 串流播放器 (包含 GitHub Pages 雲端與本地高速播放) -->
            <div style="border-radius:8px; overflow:hidden; background:#000; box-shadow:0 4px 12px rgba(0,0,0,0.4); border:1px solid #10b981; position:relative; width:100%;">
              <video controls playsinline preload="metadata" style="width:100%; max-height:420px; display:block; object-fit:contain; background:#000;">
                <source src="https://heigilin.github.io/HH/handwashing_training_web.mp4" type="video/mp4">
                <source src="assets/videos/handwashing_training_web.mp4" type="video/mp4">
                <source src="assets/videos/wet_handwash.mp4" type="video/mp4">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>

            <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; font-size:12.5px; color:#99f6e4;">
              <span>💡 <strong>串流來源：</strong>GitHub 雲端高畫質影音 ｜ 支援手機全螢幕播放 ⛶</span>
              <a href="https://heigilin.github.io/HH/handwashing_training_web.mp4" target="_blank" style="color:#5eead4; text-decoration:underline;">
                ▶ 另開視窗播放
              </a>
            </div>
          </div>'''

old_p_video_box_norm = old_p_video_box.replace('\r\n', '\n')
if old_p_video_box_norm in p_text_norm:
    p_text_norm = p_text_norm.replace(old_p_video_box_norm, new_p_video_box.replace('\r\n', '\n'), 1)
    print("presentation.html video box updated successfully.")
else:
    print("WARNING: old_p_video_box not found in presentation.html!")

with open('感控不踩雷網站/presentation.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(p_text_norm)

# 2. Update index.html
with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    idx_text = f.read()

old_idx_video_box = '''          <!-- 實境示範影音區塊 (內嵌 GitHub 線上播放與本機備援) -->
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

new_idx_video_box = '''          <!-- 實境示範影音區塊 (完整支援 GitHub 雲端串流與本地雙線路) -->
          <div style="background:#040d0b; border:1.5px solid #14b8a6; border-radius:12px; padding:18px; margin-bottom:16px;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:22px;">🎬</span>
                <div>
                  <div style="font-weight:800; color:#5eead4; font-size:16px;">標準濕洗手示範影片（實境示範教材）</div>
                  <div style="font-size:12.5px; color:#99f6e4;">肥皂起泡 ＋ 內外夾弓大立腕 40~60 秒完整搓洗程序</div>
                </div>
              </div>
              <div style="display:flex; align-items:center; gap:8px;">
                <a href="https://heigilin.github.io/HH/" target="_blank" rel="noopener" style="background:#0f766e; color:#ccfbf1; font-size:12px; font-weight:700; padding:4px 12px; border-radius:999px; text-decoration:none; display:inline-flex; align-items:center; gap:4px;">
                  🌐 互動教學站 ↗
                </a>
              </div>
            </div>

            <!-- 原生 HTML5 串流播放器 (包含 GitHub Pages 雲端與本地高速播放) -->
            <div style="position:relative; width:100%; max-width:820px; margin:0 auto; background:#000; border-radius:10px; overflow:hidden; box-shadow:0 6px 20px rgba(0,0,0,0.6); border:1px solid #115e59;">
              <video controls playsinline preload="metadata" style="width:100%; max-height:460px; display:block; object-fit:contain; background:#000;">
                <source src="https://heigilin.github.io/HH/handwashing_training_web.mp4" type="video/mp4">
                <source src="assets/videos/handwashing_training_web.mp4" type="video/mp4">
                <source src="assets/videos/wet_handwash.mp4" type="video/mp4">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>

            <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; font-size:13px; color:#99f6e4;">
              <span>💡 <strong>影音來源：</strong>GitHub 雲端高畫質串流 ｜ 點擊播放鍵 ▶ 即可直接觀看</span>
              <a href="https://heigilin.github.io/HH/handwashing_training_web.mp4" target="_blank" style="color:#5eead4; text-decoration:underline;">
                ▶ 另開全螢幕觀看
              </a>
            </div>
          </div>'''

idx_text_norm = idx_text.replace('\r\n', '\n')
old_idx_video_box_norm = old_idx_video_box.replace('\r\n', '\n')

if old_idx_video_box_norm in idx_text_norm:
    idx_text_norm = idx_text_norm.replace(old_idx_video_box_norm, new_idx_video_box.replace('\r\n', '\n'), 1)
    print("index.html Chapter 04 video box updated successfully.")
else:
    print("WARNING: old_idx_video_box not found in index.html!")

# Update openHhModal video tag in index.html
old_modal_vid_box = '''            <div style="position:relative; width:100%; aspect-ratio:16/9; max-height:420px; background:#000; border-radius:8px; overflow:hidden; border:1px solid #115e59;">
              <iframe src="https://heigilin.github.io/HH/" style="width:100%; height:100%; border:none; display:block;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="標準濕洗手示範影片"></iframe>
            </div>'''

new_modal_vid_box = '''            <div style="position:relative; width:100%; background:#000; border-radius:8px; overflow:hidden; border:1px solid #115e59;">
              <video controls playsinline preload="metadata" style="width:100%; max-height:420px; display:block; object-fit:contain; background:#000;">
                <source src="https://heigilin.github.io/HH/handwashing_training_web.mp4" type="video/mp4">
                <source src="assets/videos/handwashing_training_web.mp4" type="video/mp4">
                <source src="assets/videos/wet_handwash.mp4" type="video/mp4">
                <source src="assets/videos/溼洗手.mp4" type="video/mp4">
                您的瀏覽器不支援 HTML5 影片播放。
              </video>
            </div>'''

old_modal_vid_box_norm = old_modal_vid_box.replace('\r\n', '\n')
if old_modal_vid_box_norm in idx_text_norm:
    idx_text_norm = idx_text_norm.replace(old_modal_vid_box_norm, new_modal_vid_box.replace('\r\n', '\n'), 1)
    print("index.html openHhModal video box updated successfully.")
else:
    print("WARNING: old_modal_vid_box not found in index.html!")

with open('感控不踩雷網站/index.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(idx_text_norm)

print("Updated both HTML files.")
