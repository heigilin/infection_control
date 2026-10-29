import re

INDEX_FILE = '感控不踩雷網站/index.html'

def refine_details():
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Chapter 04 video container and text
    html = html.replace('border:1px solid #115e59;', 'border:2px solid var(--milktea-accent); box-shadow:0 8px 26px rgba(89,63,44,0.15);')
    html = html.replace('color:#99f6e4;', 'color:var(--milktea-body);')
    html = html.replace('color:#5eead4;', 'color:var(--milktea-caramel);')

    # 2. Update step diagram box
    html = html.replace('background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.12);', 'background:#fbf7f1; border:1.5px solid var(--milktea-border);')
    html = html.replace('color:#fde047;', 'color:var(--milktea-heading);')
    html = html.replace('border:1px solid rgba(255,255,255,0.15); background:#0f172a;', 'border:1.5px solid var(--milktea-border-light); background:#ffffff;')
    html = html.replace('color:#cbd5e1;', 'color:var(--milktea-body);')

    # 3. Update banner "📖 想觀看完整投影片全螢幕放映與精美圖文？"
    old_banner = """      <div style="background: rgba(13, 148, 136, 0.15); border: 1.5px solid #14b8a6; border-radius: var(--radius); padding: 18px 22px; margin-bottom: 22px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:14px;">
        <div>
          <strong style="color:#5eead4; font-size:16px;">📖 想觀看完整投影片全螢幕放映與精美圖文？</strong>
          <p style="color:#cbd5e1; font-size:14px; margin:4px 0 0;">請開啟【步驟 1：先閱讀教材】全功能簡報站（支援全螢幕投影片放映、外籍看護多語專題）：</p>
        </div>
        <a href="#sec-learn" style="background:#0f766e; color:#ffffff !important; font-weight:800; font-size:14.5px; padding:9px 20px; border-radius:999px; text-decoration:none; display:inline-flex; align-items:center; gap:6px; box-shadow:0 3px 10px rgba(15,118,110,0.3);">👉 開啟【步驟 1：完整簡報教材】 ↗</a>
      </div>"""

    new_banner = """      <div style="background: #fdfaf6; border: 1.5px solid var(--milktea-border); border-left: 6px solid var(--milktea-accent); border-radius: var(--radius); padding: 18px 22px; margin-bottom: 22px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:14px; box-shadow: 0 4px 16px rgba(89,63,44,0.05);">
        <div>
          <strong style="color:var(--milktea-heading); font-size:16px;">📖 一頁式完整感控指引速查 · 隨身學習</strong>
          <p style="color:var(--milktea-muted); font-size:14px; margin:4px 0 0;">全站已整合為一頁式流暢瀏覽，包含 9 大核心指引、標準濕洗手示範影片與實戰盲盒考題對決：</p>
        </div>
        <a href="#sec-quiz" class="main-btn" style="color:#ffffff !important; font-weight:800; font-size:14.5px; padding:9px 20px; border-radius:999px; text-decoration:none; display:inline-flex; align-items:center; gap:6px; box-shadow:0 3px 10px rgba(142,101,71,0.3);">⚔️ 滑動至實戰闖關 ➔</a>
      </div>"""

    html = html.replace(old_banner, new_banner)

    # 4. Update LINE card styling
    html = html.replace('background: rgba(15, 23, 42, 0.85); border: 1px solid #14b8a6;', 'background: #ffffff; border: 1.5px solid var(--milktea-border);')
    html = html.replace('border-bottom:1px solid #263554;', 'border-bottom:1.5px solid var(--milktea-border-light);')
    html = html.replace('background:#0f766e; color:#fff;', 'background:#527961; color:#ffffff;')
    html = html.replace('background:rgba(255,255,255,0.04); border-radius:8px; padding:12px 14px; border:1px solid rgba(255,255,255,0.08);', 'background:#fbf7f1; border-radius:10px; padding:12px 14px; border:1px solid var(--milktea-border-light);')
    html = html.replace('color:#2dd4bf;', 'color:var(--milktea-caramel);')
    html = html.replace('color:#94a3b8;', 'color:var(--milktea-body);')

    # 5. Update floating 3D particle colors in JavaScript to milk tea tones
    html = html.replace("['#34d3b4', '#ffd166', '#6aa8ff', '#9a7cff']", "['#b87b4e', '#c28233', '#8e6547', '#d2c1ae']")
    html = html.replace("auraColor = (typeof state !== 'undefined' && state && state.auraColor) ? state.auraColor : '#ffd166';", "auraColor = (typeof state !== 'undefined' && state && state.auraColor) ? state.auraColor : '#c28233';")

    # 6. Update HUD styling in case of adventure duel
    hud_css = """
    #hud {
      background: rgba(254, 252, 248, 0.95) !important;
      border: 1.5px solid var(--milktea-border) !important;
      color: var(--milktea-heading) !important;
      box-shadow: 0 4px 20px rgba(89, 63, 44, 0.1) !important;
    }
    .hud-badge {
      background: #fbf7f1 !important;
      color: var(--milktea-heading) !important;
      border: 1px solid var(--milktea-border) !important;
    }
    .hud-hp-bar {
      background: #e8ded2 !important;
    }
    .hud-hp-fill {
      background: linear-gradient(90deg, #b87b4e, #8e6547) !important;
    }
    """
    if '#hud {' not in html:
        html = html.replace('</style>', hud_css + '\n</style>', 1)

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(html)

    print("Refined milk tea details completed successfully.")

if __name__ == '__main__':
    refine_details()
