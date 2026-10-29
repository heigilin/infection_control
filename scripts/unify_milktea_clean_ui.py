import re
import os

INDEX_FILE = '感控不踩雷網站/index.html'

def clean_and_unify():
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    # =========================================================================
    # 1. 徹底移除多重重複按鈕與暗藍橫幅 (Eliminate all redundant button stacks)
    # =========================================================================

    # 1.1 移除 .site-flow-roadmap (包含【步驟 1】➔ 【步驟 2】的暗藍長條)
    html = re.sub(r'<!-- 學習路徑導引條 -->\s*<div class="site-flow-roadmap">.*?</div>\s*</div>', '', html, flags=re.DOTALL)
    # 也防備單獨的 .site-flow-roadmap
    html = re.sub(r'<div class="site-flow-roadmap">.*?</div>', '', html, flags=re.DOTALL)

    # 1.2 移除 .phase-bar (包含兩個巨大按鈕卡片的切換列)
    html = re.sub(r'<!-- 階段切換導航 \(先學習才闖關\) -->\s*<div class="phase-bar">.*?</div>\s*</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div class="phase-bar">.*?</div>', '', html, flags=re.DOTALL)

    # 1.3 移除 .mobile-action-hub (避免在頁首重複堆疊 2 個巨大卡片按鈕)
    html = re.sub(r'<!-- 手機端專屬：雙軌直覺行動入口.*?-->\s*<div class="mobile-action-hub">.*?</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div class="mobile-action-hub">.*?</div>', '', html, flags=re.DOTALL)

    # 1.4 移除冷色青綠色提示橫幅「想觀看完整投影片全螢幕放映...👉 開啟【步驟 1：完整簡報教材】」
    html = re.sub(r'<div style="background:\s*rgba\(13,\s*148,\s*136,\s*0\.15\);.*?</div>\s*</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div style="background:\s*#fdfaf6; border: 1\.5px solid var\(--milktea-border\); border-left: 6px solid var\(--milktea-accent\);.*?</div>\s*</div>', '', html, flags=re.DOTALL)

    # 1.5 移除章節標題內多餘的按鈕「⚔️ 略過速查，直接闖關 ➔」
    html = re.sub(r'<a href="#sec-quiz" class="main-btn"[^>]*>.*?略過速查.*?</a>', '', html)

    # 1.6 移除第二階段標題內多餘的按鈕「↑ 返回 9 大章節速查」
    html = re.sub(r'<a href="#sec-learn" class="ghost-btn"[^>]*>.*?返回 9 大章節速查.*?</a>', '', html)

    print("Step 1: Successfully removed all redundant button blocks and banners!")

    # =========================================================================
    # 2. 精簡頂部導覽列：由「5 個笨重膠囊按鈕」重構為「優雅極簡文字導覽」
    # =========================================================================
    clean_nav_html = """  <!-- 全站優雅奶茶色極簡導覽列 -->
  <header class="site-nav">
    <div class="nav-inner">
      <a class="nav-brand" href="#home" title="回到首頁">
        <img class="nav-logo" src="assets/avatar.jpg" alt="台大感管頭像">
        <div class="nav-brand-text">
          <span class="nav-title">臺大醫院感控不踩雷</span>
          <span class="nav-subtitle">病房最優雅的守護神</span>
        </div>
      </a>
      <nav class="nav-links">
        <a class="nav-link-item" href="#sec-learn">📖 核心指引</a>
        <a class="nav-link-item" href="#sec-video">🎥 洗手影音</a>
        <a class="nav-link-item" href="#sec-quiz">⚔️ 實戰闖關</a>
        <a class="nav-link-item" href="#sec-line">📱 LINE口袋書</a>
        <a class="nav-link-item nav-link-admin" href="admin.html">📊 主管看板 ↗</a>
      </nav>
    </div>
  </header>"""

    html = re.sub(r'<!-- 全站統一旗艦導覽列 -->\s*<header class="site-nav">.*?</header>', clean_nav_html, html, flags=re.DOTALL)
    html = re.sub(r'<!-- 全站優雅奶茶色極簡導覽列 -->\s*<header class="site-nav">.*?</header>', clean_nav_html, html, flags=re.DOTALL)

    # =========================================================================
    # 3. 首頁 Masthead 迎賓區：精簡乾淨、純暖色系、溫柔導引
    # =========================================================================
    clean_masthead_html = """    <header class="masthead">
      <img class="masthead-logo" src="assets/avatar.jpg" alt="台大感管頭像">
      <div class="masthead-content">
        <p class="kicker">NTUH INFECTION CONTROL · WARM MEDICAL LEARNING</p>
        <h1 class="logo-title">感控不踩雷｜<span>病房最優雅的守護神</span></h1>
        <p class="tagline">把感染管制做成直覺 · 用最溫暖專業的底氣 · 讓臨床工作游刃有餘</p>
        <div class="masthead-links">
          <a href="#sec-learn" class="m-jump-link">📖 閱讀 9 大核心指引 ↓</a>
          <a href="#sec-video" class="m-jump-link">🎥 標準濕洗手示範影音 ↓</a>
          <a href="#sec-quiz" class="m-jump-link m-jump-primary">⚔️ 進入臨床情境闖關 ↓</a>
        </div>
      </div>
    </header>"""

    html = re.sub(r'<header class="masthead">.*?</header>', clean_masthead_html, html, flags=re.DOTALL)

    # =========================================================================
    # 4. 徹底消除全站冷色系 (Cold colors) 替換為溫暖奶茶色
    # =========================================================================
    # 4.1 手部衛生卡片 Chapter 04 背景由深冷墨綠改為奶茶象牙白
    old_ch4_card = r'<article class="learn-card" style="grid-column: 1 / -1; border: 2px solid var\(--accent\); background: linear-gradient\(180deg, #0f241f 0%, #091310 100%\); box-shadow: 0 8px 30px rgba\(15,118,110,0\.3\);">'
    new_ch4_card = r'<article class="learn-card" id="sec-video" style="grid-column: 1 / -1; border: 2px solid var(--milktea-border); background: #ffffff; box-shadow: 0 8px 28px rgba(89, 63, 44, 0.08);">'
    html = re.sub(old_ch4_card, new_ch4_card, html)

    # 4.2 影音容器由極冷暗綠改為溫暖燕麥奶咖
    html = html.replace('background:#040d0b; border:1.5px solid #14b8a6;', 'background:#faf6f0; border:1.5px solid var(--milktea-border);')
    html = html.replace('background:#040d0b;', 'background:#faf6f0;')
    html = html.replace('border:1.5px solid #14b8a6;', 'border:1.5px solid var(--milktea-border);')
    html = html.replace('border: 1.5px solid #14b8a6;', 'border: 1.5px solid var(--milktea-border);')
    html = html.replace('border: 1px solid #14b8a6;', 'border: 1.5px solid var(--milktea-border);')
    html = html.replace('background:#0f766e;', 'background:var(--milktea-accent);')
    html = html.replace('background: #0f766e;', 'background: var(--milktea-accent);')
    html = html.replace('color:#ccfbf1;', 'color:#ffffff;')
    html = html.replace('color: #ccfbf1;', 'color: #ffffff;')
    html = html.replace('color:#5eead4;', 'color:var(--milktea-caramel);')
    html = html.replace('color: #5eead4;', 'color: var(--milktea-caramel);')
    html = html.replace('color:#99f6e4;', 'color:var(--milktea-muted);')
    html = html.replace('color: #99f6e4;', 'color: var(--milktea-muted);')
    html = html.replace('color:#2dd4bf;', 'color:var(--milktea-caramel);')
    html = html.replace('color: #2dd4bf;', 'color: var(--milktea-caramel);')

    # 4.3 移除 CSS 中殘留的深冷藍夜色與冷綠變數
    html = html.replace('--night: #090e1a;', '--night: #f9f6f0;')
    html = html.replace('--slate: #111a2e;', '--slate: #ffffff;')
    html = html.replace('--slate-2: #18233c;', '--slate-2: #fcf9f5;')
    html = html.replace('--mint: #2dd4bf;', '--mint: #8c674b;')
    html = html.replace('--mint-dk: #0f766e;', '--mint-dk: #6e4e37;')
    html = html.replace('--sky: #38bdf8;', '--sky: #8c674b;')
    html = html.replace('--accent: #2dd4bf;', '--accent: #8c674b;')
    html = html.replace('border: 2px solid #2dd4bf;', 'border: 2px solid var(--milktea-border);')
    html = html.replace('border-color: #2dd4bf;', 'border-color: var(--milktea-accent);')
    html = html.replace('border-color: #38bdf8;', 'border-color: var(--milktea-caramel);')
    html = html.replace('background: #2dd4bf;', 'background: var(--milktea-accent);')
    html = html.replace('background: #38bdf8;', 'background: var(--milktea-caramel);')

    # =========================================================================
    # 5. 注入溫柔純粹的奶茶色導覽列與 Masthead 專屬樣式
    # =========================================================================
    refined_milktea_css = """
    /* ==========================================================================
       ☕ 純粹溫暖奶茶色系：收斂按鈕管道、極致護眼、無多重管道凌亂感
       ========================================================================== */
    .site-nav {
      background: rgba(254, 252, 248, 0.96) !important;
      backdrop-filter: blur(16px) !important;
      border-bottom: 1.5px solid #e8ded2 !important;
      padding: 0.65rem clamp(14px, 3vw, 40px) !important;
      box-shadow: 0 2px 14px rgba(78, 55, 38, 0.05) !important;
    }
    .nav-inner {
      display: flex !important;
      align-items: center !important;
      justify-content: space-between !important;
      gap: 16px !important;
      max-width: 1220px !important;
      margin: 0 auto !important;
    }
    .nav-brand {
      display: flex !important;
      align-items: center !important;
      gap: 10px !important;
      text-decoration: none !important;
    }
    .nav-logo {
      width: 38px !important;
      height: 38px !important;
      border-radius: 50% !important;
      border: 1.5px solid var(--milktea-accent) !important;
    }
    .nav-brand-text {
      display: flex !important;
      flex-direction: column !important;
    }
    .nav-title {
      font-size: 1.05rem !important;
      font-weight: 900 !important;
      color: var(--milktea-heading) !important;
      line-height: 1.2 !important;
    }
    .nav-subtitle {
      font-size: 0.72rem !important;
      font-weight: 700 !important;
      color: var(--milktea-muted) !important;
    }
    .nav-links {
      display: flex !important;
      align-items: center !important;
      gap: 8px !important;
      flex-wrap: wrap !important;
    }
    .nav-link-item {
      padding: 6px 12px !important;
      border-radius: 8px !important;
      font-size: 0.88rem !important;
      font-weight: 700 !important;
      color: var(--milktea-body) !important;
      text-decoration: none !important;
      transition: all 0.15s ease !important;
    }
    .nav-link-item:hover {
      color: var(--milktea-heading) !important;
      background: rgba(140, 103, 75, 0.08) !important;
    }
    .nav-link-admin {
      background: #f4ede4 !important;
      border: 1px solid var(--milktea-border) !important;
      color: var(--milktea-heading) !important;
    }
    .nav-link-admin:hover {
      background: #ede1d2 !important;
      border-color: var(--milktea-accent) !important;
    }

    /* Masthead 迎賓卡片：清爽寬闊 */
    .masthead {
      margin: 18px 0 24px !important;
      padding: 24px 28px !important;
      background: #ffffff !important;
      border: 1.5px solid var(--milktea-border) !important;
      border-radius: var(--radius) !important;
      box-shadow: 0 4px 20px rgba(89, 63, 44, 0.06) !important;
      display: flex !important;
      align-items: center !important;
      gap: 20px !important;
    }
    .masthead-logo {
      width: 64px !important;
      height: 64px !important;
      border-radius: 50% !important;
      border: 2px solid var(--milktea-accent) !important;
      flex-shrink: 0 !important;
    }
    .masthead-content {
      flex: 1 !important;
    }
    .kicker {
      font-size: 0.72rem !important;
      font-weight: 800 !important;
      letter-spacing: 1.5px !important;
      color: var(--milktea-caramel) !important;
      margin-bottom: 2px !important;
    }
    .logo-title {
      font-size: 1.55rem !important;
      font-weight: 900 !important;
      color: var(--milktea-heading) !important;
      margin-bottom: 4px !important;
    }
    .logo-title span {
      color: var(--milktea-accent) !important;
    }
    .tagline {
      font-size: 0.88rem !important;
      color: var(--milktea-muted) !important;
      margin-bottom: 14px !important;
    }
    .masthead-links {
      display: flex !important;
      align-items: center !important;
      gap: 10px !important;
      flex-wrap: wrap !important;
    }
    .m-jump-link {
      font-size: 0.82rem !important;
      font-weight: 700 !important;
      padding: 5px 14px !important;
      border-radius: 999px !important;
      text-decoration: none !important;
      background: #f7f0e6 !important;
      color: var(--milktea-body) !important;
      border: 1px solid var(--milktea-border) !important;
      transition: all 0.15s ease !important;
    }
    .m-jump-link:hover {
      background: #ede1d2 !important;
      color: var(--milktea-heading) !important;
    }
    .m-jump-primary {
      background: var(--milktea-accent) !important;
      color: #ffffff !important;
      border-color: var(--milktea-accent-hover) !important;
    }
    .m-jump-primary:hover {
      background: var(--milktea-accent-hover) !important;
      color: #ffffff !important;
    }

    /* 隱藏過去殘留的所有按鈕長條樣式 */
    .site-flow-roadmap, .phase-bar, .mobile-action-hub {
      display: none !important;
    }

    /* 手機端自適應 */
    @media (max-width: 768px) {
      .site-nav {
        padding: 0.5rem 10px !important;
      }
      .nav-links {
        gap: 4px !important;
      }
      .nav-link-item {
        padding: 4px 8px !important;
        font-size: 0.78rem !important;
      }
      .masthead {
        padding: 16px 14px !important;
        gap: 12px !important;
      }
      .masthead-logo {
        width: 44px !important;
        height: 44px !important;
      }
      .logo-title {
        font-size: 1.2rem !important;
      }
      .tagline {
        font-size: 0.8rem !important;
        margin-bottom: 10px !important;
      }
    }
    """

    if '/* ☕ 純粹溫暖奶茶色系：收斂按鈕管道' not in html:
        html = html.replace('</style>', refined_milktea_css + '\n</style>', 1)

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(html)

    print("Step 5: Successfully updated index.html with purified warm milk tea UI!")

if __name__ == '__main__':
    clean_and_unify()
