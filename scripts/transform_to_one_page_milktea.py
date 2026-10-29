import re
import os

INDEX_FILE = '感控不踩雷網站/index.html'

def apply_milktea_onepage():
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update <html ... data-theme="milktea">
    html = re.sub(r'<html\s+([^>]*?)data-theme="[^"]*"', r'<html \1data-theme="milktea"', html)
    if 'data-theme="milktea"' not in html:
        html = html.replace('<html lang="zh-TW">', '<html lang="zh-TW" data-theme="milktea">')

    print("Step 1: Set data-theme to milktea")

    # 2. Inject Milk Tea CSS variables at the beginning of :root
    milktea_vars = """
    /* ===== 溫潤優雅奶茶色系 (Warm Milk Tea & Latte Palette) 一頁式專屬美學 ===== */
    :root, html[data-theme="milktea"] {
      --milktea-bg: #f8f5f0;
      --milktea-bg-warm: #faf7f2;
      --milktea-cream: #fffdfa;
      --milktea-card: #ffffff;
      --milktea-card-sub: #fbf7f1;
      --milktea-border: #e8ded2;
      --milktea-border-light: #f0e7db;
      --milktea-border-dk: #d2c1ae;
      
      --milktea-accent: #8e6547;
      --milktea-accent-hover: #775338;
      --milktea-caramel: #b87b4e;
      --milktea-caramel-hover: #a1673b;
      --milktea-foam: #fdf5ea;
      --milktea-tea: #ab7d58;

      --milktea-heading: #362419;
      --milktea-body: #4c3b30;
      --milktea-muted: #826f61;
      --milktea-subtle: #a18e80;

      --milktea-sage: #527961;
      --milktea-sage-bg: #f2f7f4;
      --milktea-amber: #c28233;
      --milktea-amber-bg: #fdf8f0;
      --milktea-terracotta: #b74f41;
      --milktea-terracotta-bg: #fdf3f2;

      /* 相容變數覆蓋為高雅奶茶風 */
      --night: #f8f5f0;
      --slate: #ffffff;
      --slate-2: #fcf8f3;
      --slate-3: #f5ebe0;
      --line: #e8ded2;
      --mint: #8e6547;
      --mint-dk: #6b4a32;
      --sun: #c28233;
      --berry: #b74f41;
      --sky: #8e6547;
      --grape: #947158;
      --danger: #b74f41;
      --paper: #ffffff;
      --ink: #362419;
      --soft: #826f61;
      --rule: #e8ded2;
      --fg: #362419;
      --fg-2: #4c3b30;
      --fg-3: #826f61;
      --accent: #8e6547;
      --home-bg: linear-gradient(135deg, #faf7f2 0%, #f6f1e8 50%, #ede3d4 100%);
      --card-bg: rgba(255, 255, 255, 0.95);
      --font-sans: 'Noto Sans TC', system-ui, -apple-system, sans-serif;
    }
"""

    if '/* ===== 溫潤優雅奶茶色系' not in html:
        html = re.sub(r'(:root\s*\{)', milktea_vars + r'\n    \1', html, count=1)

    print("Step 2: Added milk tea root variables")

    # 3. Add Comprehensive Milk Tea and One-Page Layout CSS overrides
    onepage_css = """
    /* ==========================================================================
       ☕ 奶茶色系與一頁式無縫瀏覽極致架構 (Milk Tea Single-Page Architecture)
       ========================================================================== */
    html {
      scroll-behavior: smooth;
    }

    body {
      background-color: var(--milktea-bg) !important;
      color: var(--milktea-body) !important;
    }

    /* 頂部導覽列：溫潤奶茶磨砂質感 */
    .site-nav {
      background: rgba(254, 252, 248, 0.95) !important;
      backdrop-filter: blur(14px) !important;
      border-bottom: 1.5px solid var(--milktea-border) !important;
      box-shadow: 0 4px 20px rgba(78, 55, 38, 0.06) !important;
    }
    .nav-title {
      color: var(--milktea-heading) !important;
    }
    .nav-flow-hint {
      color: var(--milktea-accent) !important;
    }
    .nav-btn {
      background: #f5ede4 !important;
      border: 1px solid var(--milktea-border) !important;
      color: var(--milktea-body) !important;
      transition: all 0.2s ease !important;
    }
    .nav-btn:hover {
      background: #ede1d2 !important;
      border-color: var(--milktea-accent) !important;
      color: var(--milktea-heading) !important;
      transform: translateY(-1px);
    }
    .nav-btn.active {
      background: var(--milktea-accent) !important;
      color: #ffffff !important;
      border-color: var(--milktea-accent-hover) !important;
      box-shadow: 0 2px 10px rgba(142, 101, 71, 0.3) !important;
    }
    .nav-btn-line {
      background: #476a52 !important;
      color: #ffffff !important;
      border-color: #3d5b46 !important;
    }
    .nav-btn-line:hover {
      background: #3c5a45 !important;
      color: #ffffff !important;
    }

    /* 首頁 Masthead 迎賓橫幅 */
    .masthead {
      background: var(--card-bg) !important;
      border: 1.5px solid var(--milktea-border) !important;
      box-shadow: 0 8px 30px rgba(89, 63, 44, 0.07) !important;
    }
    .logo-title {
      color: var(--milktea-heading) !important;
    }
    .logo-title span {
      color: var(--milktea-accent) !important;
    }
    .tagline {
      color: var(--milktea-muted) !important;
    }
    .kicker {
      color: var(--milktea-caramel) !important;
    }

    /* 一頁式各區塊通用卡片與標題樣式 */
    .onepage-section-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 20px;
      padding: 12px 18px;
      background: linear-gradient(135deg, #fdfaf6 0%, #f7f0e6 100%);
      border: 1.5px solid var(--milktea-border);
      border-left: 6px solid var(--milktea-accent);
      border-radius: var(--radius);
      box-shadow: 0 3px 12px rgba(89, 63, 44, 0.05);
    }
    .onepage-section-title {
      font-size: 1.28rem;
      font-weight: 900;
      color: var(--milktea-heading);
      margin: 0;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .onepage-section-desc {
      font-size: 0.88rem;
      color: var(--milktea-muted);
      margin: 4px 0 0;
      line-height: 1.5;
    }

    /* 9 大核心指引學習卡片 (奶茶色風華) */
    .learn-panel {
      display: block !important; /* 一頁式始終展示 */
      margin-bottom: 36px;
    }
    .learn-intro-banner {
      background: #fbf7f1 !important;
      border: 1.5px solid var(--milktea-border) !important;
      color: var(--milktea-body) !important;
      box-shadow: 0 4px 16px rgba(89, 63, 44, 0.05) !important;
    }
    .learn-intro-banner h3 {
      color: var(--milktea-heading) !important;
    }
    .learn-cards-grid {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)) !important;
      gap: 18px !important;
    }
    .learn-card {
      background: #ffffff !important;
      border: 1.5px solid var(--milktea-border) !important;
      border-radius: var(--radius) !important;
      padding: 20px 22px !important;
      box-shadow: 0 4px 18px rgba(89, 63, 44, 0.06) !important;
      transition: all 0.2s ease !important;
      color: var(--milktea-body) !important;
    }
    .learn-card:hover {
      border-color: var(--milktea-caramel) !important;
      box-shadow: 0 8px 26px rgba(89, 63, 44, 0.12) !important;
      transform: translateY(-2px);
    }
    .learn-card h4 {
      color: var(--milktea-heading) !important;
      border-bottom: 1.5px solid var(--milktea-border-light) !important;
      padding-bottom: 10px !important;
      margin-bottom: 12px !important;
      font-size: 1.05rem !important;
      font-weight: 800 !important;
    }
    .learn-card strong {
      color: var(--milktea-heading) !important;
    }

    /* 影音示範專區 (Video Feature Section) */
    .video-feature-box {
      background: #ffffff;
      border: 2px solid var(--milktea-accent);
      border-radius: var(--radius);
      padding: 24px;
      margin-bottom: 36px;
      box-shadow: 0 8px 28px rgba(89, 63, 44, 0.09);
    }
    .video-screen-wrapper {
      position: relative;
      background: #1e1712;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    }

    /* 第二階段闖關面板 (一頁式自然順序呈現) */
    #quizSetupSection {
      display: block !important; /* 一頁式始終呈現 */
      margin-top: 10px;
      margin-bottom: 40px;
    }
    .panel {
      background: #ffffff !important;
      border: 1.5px solid var(--milktea-border) !important;
      color: var(--milktea-body) !important;
      box-shadow: 0 6px 22px rgba(89, 63, 44, 0.06) !important;
    }
    .stepper {
      background: #f7f1e7 !important;
      border: 1px solid var(--milktea-border) !important;
    }
    .stepper li {
      color: var(--milktea-muted) !important;
    }
    .stepper li.active {
      background: var(--milktea-accent) !important;
      color: #ffffff !important;
    }
    .choice-card {
      background: #fdfaf6 !important;
      border: 1.5px solid var(--milktea-border) !important;
      color: var(--milktea-body) !important;
    }
    .choice-card:hover {
      border-color: var(--milktea-caramel) !important;
      background: #faf4ec !important;
    }
    .choice-card.selected {
      border-color: var(--milktea-accent) !important;
      background: #fbf5ee !important;
      box-shadow: 0 0 16px rgba(142, 101, 71, 0.25) !important;
    }
    .choice-card h3 {
      color: var(--milktea-heading) !important;
    }
    .choice-badge {
      background: var(--milktea-accent) !important;
      color: #ffffff !important;
    }
    .text-input {
      background: #fcf9f5 !important;
      border: 1.5px solid var(--milktea-border) !important;
      color: var(--milktea-heading) !important;
    }
    .text-input:focus {
      border-color: var(--milktea-accent) !important;
      background: #ffffff !important;
      outline: none;
      box-shadow: 0 0 0 3px rgba(142, 101, 71, 0.2) !important;
    }
    .main-btn {
      background: linear-gradient(135deg, var(--milktea-accent) 0%, var(--milktea-accent-hover) 100%) !important;
      color: #ffffff !important;
      box-shadow: 0 4px 14px rgba(142, 101, 71, 0.35) !important;
      border: none !important;
    }
    .main-btn:hover {
      background: linear-gradient(135deg, var(--milktea-accent-hover) 0%, #5d3f2a) !important;
      transform: translateY(-1px);
    }
    .ghost-btn {
      background: #f5ede4 !important;
      border: 1.5px solid var(--milktea-border) !important;
      color: var(--milktea-heading) !important;
    }
    .ghost-btn:hover {
      background: #ede1d2 !important;
      border-color: var(--milktea-accent) !important;
    }

    /* 對決舞台 ARENA (奶茶暖調適配) */
    .arena-box {
      background: #fffdfa !important;
      border: 2px solid var(--milktea-accent) !important;
      color: var(--milktea-heading) !important;
      box-shadow: 0 20px 60px rgba(54, 36, 25, 0.35) !important;
    }
    .monster-card {
      background: #fbf6ef !important;
      border: 1px solid var(--milktea-border) !important;
    }
    .monster-meta h3 {
      color: var(--milktea-heading) !important;
    }
    .monster-meta p {
      color: var(--milktea-body) !important;
    }
    .question-prompt {
      background: #fdfaf6 !important;
      border: 1.5px solid var(--milktea-border) !important;
      color: var(--milktea-heading) !important;
    }
    .option-btn {
      background: #ffffff !important;
      border: 1.5px solid var(--milktea-border) !important;
      color: var(--milktea-body) !important;
    }
    .option-btn:hover:not(:disabled) {
      background: #fbf5ee !important;
      border-color: var(--milktea-accent) !important;
      color: var(--milktea-heading) !important;
    }
    .option-btn.correct {
      background: #edf7f0 !important;
      border-color: var(--milktea-sage) !important;
      color: #1e462d !important;
    }
    .option-btn.wrong {
      background: #fdf2f2 !important;
      border-color: var(--milktea-terracotta) !important;
      color: #6d1f18 !important;
    }

    /* 奶茶色系手機雙軌直覺行動入口 */
    .card-learn-portal {
      background: linear-gradient(135deg, #fdfaf6 0%, #f6ede1 100%) !important;
      border-color: var(--milktea-accent) !important;
    }
    .card-quiz-portal {
      background: linear-gradient(135deg, #faf4ec 0%, #f1e4d3 100%) !important;
      border-color: var(--milktea-caramel) !important;
    }
    .step-pill-1 {
      background: var(--milktea-accent) !important;
      color: #ffffff !important;
    }
    .step-pill-2 {
      background: var(--milktea-caramel) !important;
      color: #ffffff !important;
    }
    .action-card-title {
      color: var(--milktea-heading) !important;
    }
    .action-card-desc {
      color: var(--milktea-muted) !important;
    }
    .btn-pill-learn {
      background: var(--milktea-accent) !important;
      color: #ffffff !important;
    }
    .btn-pill-quiz {
      background: var(--milktea-caramel) !important;
      color: #ffffff !important;
    }

    /* 頁尾 */
    .site-footer {
      margin-top: 60px;
      padding: 32px 16px 40px;
      text-align: center;
      border-top: 1.5px solid var(--milktea-border);
      background: #fbf7f1;
      border-radius: var(--radius) var(--radius) 0 0;
      color: var(--milktea-muted);
      font-size: 0.9rem;
    }
    .site-footer a {
      color: var(--milktea-accent);
      text-decoration: none;
      font-weight: 700;
    }
    .site-footer a:hover {
      text-decoration: underline;
    }
    """

    if '/* ☕ 奶茶色系與一頁式無縫瀏覽極致架構' not in html:
        html = html.replace('</style>', onepage_css + '\n</style>', 1)

    print("Step 3: Added One-page milk tea CSS")

    # 4. Update the sticky nav to One-Page Anchor Links
    old_nav_links_pattern = r'<nav class="nav-links">.*?</nav>'
    new_nav_links = """<nav class="nav-links">
        <a class="nav-btn" href="#sec-learn" title="直達第一階段：9 大感控實戰指引速查">
          <span>📖 核心指引</span>
        </a>
        <a class="nav-btn" href="#sec-video" title="直達示範影音：標準肥皂水洗手 4 步驟拆解">
          <span>🎥 洗手影音</span>
        </a>
        <a class="nav-btn active" href="#sec-quiz" title="直達第二階段：情境盲盒闖關測驗">
          <span>⚔️ 實戰闖關</span>
        </a>
        <a class="nav-btn" href="#sec-line" title="直達臨床口袋顧問：台大感管 LINE @ntuhic">
          <span>📱 LINE口袋書</span>
        </a>
        <a class="nav-btn" href="admin.html" title="查看全院同仁答題成效與弱點統計">
          <span>📊 主管看板</span>
        </a>
      </nav>"""

    html = re.sub(old_nav_links_pattern, new_nav_links, html, count=1, flags=re.DOTALL)
    print("Step 4: Updated nav-links to one-page smooth anchors")

    # 5. Update mobile-action-hub links to smooth anchors
    html = html.replace('href="presentation.html"', 'href="#sec-learn"')
    print("Step 5: Updated action card links to anchor #sec-learn")

    # 6. Ensure learnSection and quizSetupSection have clean section IDs and both are displayed
    # In index.html, find `<section class="learn-panel" id="learnSection">` and add anchor id `id="sec-learn"`
    html = html.replace('<section class="learn-panel" id="learnSection">', '<section class="learn-panel" id="sec-learn">')
    html = html.replace('<div id="quizSetupSection" style="display:none;">', '<div id="sec-quiz" class="quiz-section">')
    html = html.replace('<div id="quizSetupSection">', '<div id="sec-quiz" class="quiz-section">')

    # 7. Add dedicated section headers for the one-page flow
    learn_section_header = """      <!-- 一頁式第一區塊標題：9 大核心實戰重點速查 -->
      <div class="onepage-section-header">
        <div>
          <h2 class="onepage-section-title"><span>📖</span> 第一階段：臺大醫院 9 大核心實戰指引速查</h2>
          <p class="onepage-section-desc">感染管制不是生硬的規定，而是臨床游刃有餘的專業底氣。請先快速複習以下 9 大重點，隨時可順流向下滑動進行實戰闖關：</p>
        </div>
        <a href="#sec-quiz" class="main-btn" style="padding:8px 18px; font-size:14px; text-decoration:none; display:inline-flex; align-items:center; gap:6px;">
          ⚔️ 略過速查，直接闖關 ➔
        </a>
      </div>
"""

    if 'class="onepage-section-header"' not in html:
        html = html.replace('<section class="learn-panel" id="sec-learn">', '<section class="learn-panel" id="sec-learn">\n' + learn_section_header)

    # 8. Add anchor id="sec-video" to the hand hygiene card
    html = html.replace('<!-- 章節 04 (手部衛生) -->\n        <article class="learn-card"', '<!-- 章節 04 (手部衛生) -->\n        <article class="learn-card" id="sec-video"')
    html = html.replace('<!-- 章節 04 (手部衛生) -->\r\n        <article class="learn-card"', '<!-- 章節 04 (手部衛生) -->\r\n        <article class="learn-card" id="sec-video"')

    # 9. Add anchor id="sec-line" to the LINE card
    html = html.replace('<!-- 臨床口袋神隊友：台大感管 LINE 官方帳號 (@ntuhic) -->\n      <div style="background:', '<!-- 臨床口袋神隊友：台大感管 LINE 官方帳號 (@ntuhic) -->\n      <div id="sec-line" style="background:')
    html = html.replace('<!-- 臨床口袋神隊友：台大感管 LINE 官方帳號 (@ntuhic) -->\r\n      <div style="background:', '<!-- 臨床口袋神隊友：台大感管 LINE 官方帳號 (@ntuhic) -->\r\n      <div id="sec-line" style="background:')

    # 10. Add quiz section header
    quiz_section_header = """      <!-- 一頁式第二區塊標題：實戰情境盲盒對決 -->
      <div class="onepage-section-header" style="border-left-color:var(--milktea-caramel); margin-top:20px;">
        <div>
          <h2 class="onepage-section-title"><span>⚔️</span> 第二階段：臨床實戰闖關盲盒對決</h2>
          <p class="onepage-section-desc">選擇臨床場域與身分，迎接 10 題臨床實戰情境考驗，避開常見地雷，獲頒「病房最優雅的守護神」榮譽證書！</p>
        </div>
        <a href="#sec-learn" class="ghost-btn" style="padding:8px 18px; font-size:14px; text-decoration:none; display:inline-flex; align-items:center; gap:6px;">
          ↑ 返回 9 大章節速查
        </a>
      </div>
"""
    if '第二階段：臨床實戰闖關盲盒對決' not in html:
        html = html.replace('<div id="sec-quiz" class="quiz-section">', '<div id="sec-quiz" class="quiz-section">\n' + quiz_section_header)

    # 11. Add warm Milk Tea Footer at the end of <main id="home">
    site_footer = """
    <!-- 溫暖奶茶色頁尾 -->
    <footer class="site-footer">
      <div style="max-width:800px; margin:0 auto;">
        <div style="display:flex; justify-content:center; align-items:center; gap:8px; margin-bottom:10px;">
          <img src="assets/avatar.jpg" alt="台大感管" style="width:30px; height:30px; border-radius:50%; border:1.5px solid var(--milktea-accent);">
          <strong style="color:var(--milktea-heading); font-size:1.05rem;">國立臺灣大學醫學院附設醫院 感染管制中心</strong>
        </div>
        <p style="margin-bottom:12px; line-height:1.6;">
          NTUH Infection Control · 把感控做成直覺，用最溫暖專業的底氣，守護病患也保護自己。<br>
          臨床口袋諮詢：加入感管 LINE 官方帳號 <a href="https://line.me/R/ti/p/@ntuhic" target="_blank">@ntuhic</a> 秒查隔離醫囑與多語衛教
        </p>
        <div style="display:flex; justify-content:center; gap:16px; font-weight:700; flex-wrap:wrap;">
          <a href="#home">↑ 回到頂端</a>
          <span>·</span>
          <a href="#sec-learn">📖 核心指引</a>
          <span>·</span>
          <a href="#sec-video">🎥 洗手影音</a>
          <span>·</span>
          <a href="#sec-quiz">⚔️ 實戰闖關</a>
          <span>·</span>
          <a href="#sec-line">📱 LINE 口袋書</a>
          <span>·</span>
          <a href="admin.html">📊 主管看板</a>
        </div>
        <p style="margin-top:16px; font-size:0.8rem; color:var(--milktea-subtle);">
          © 2026 臺大醫院感染管制中心 版權所有 ｜ 一頁式直覺學習系統
        </p>
      </div>
    </footer>
"""
    if 'class="site-footer"' not in html:
        html = html.replace('</main>', site_footer + '\n  </main>')

    # 12. Fix JavaScript switchPhase to keep both sections visible in One-Page layout
    js_onepage_replace = """    function switchPhase(phase, options = {}) {
      const autoScroll = options.scroll ?? true;
      const targetSec = phase === 'learn' ? document.getElementById('sec-learn') : document.getElementById('sec-quiz');
      if (tabPhaseLearn) tabPhaseLearn.classList.toggle('active', phase === 'learn');
      if (tabPhaseQuiz) tabPhaseQuiz.classList.toggle('active', phase === 'quiz');

      // 一頁式體驗：兩個區塊均自然並存，點擊時平滑滑動至目標區塊
      const learnSec = document.getElementById('sec-learn') || document.getElementById('learnSection');
      const quizSec = document.getElementById('sec-quiz') || document.getElementById('quizSetupSection');
      if (learnSec) learnSec.style.display = 'block';
      if (quizSec) quizSec.style.display = 'block';

      if (autoScroll && targetSec) {
        targetSec.scrollIntoView({ behavior: 'smooth' });
      }
      if (options.playSound) {
        sound.play('click');
      }
    }"""

    # Replace the old switchPhase implementation
    pattern_switch = r'function switchPhase\(phase, options = \{\}\)\s*\{.*?\n    \}'
    html = re.sub(pattern_switch, js_onepage_replace, html, count=1, flags=re.DOTALL)

    # 13. Ensure themePicker includes milktea
    old_theme_picker = """          <div class="theme-pick" id="themePicker">
            <button class="theme-btn active" data-theme="night">星夜深藍</button>
            <button class="theme-btn" data-theme="mint">感管翡翠</button>
            <button class="theme-btn" data-theme="sun">晨曦暖杏</button>
            <button class="theme-btn" data-theme="paper">典雅雪白</button>
          </div>"""

    new_theme_picker = """          <div class="theme-pick" id="themePicker">
            <button class="theme-btn active" data-theme="milktea">絲滑奶茶 ☕</button>
            <button class="theme-btn" data-theme="mint">溫暖翡翠</button>
            <button class="theme-btn" data-theme="sun">晨曦暖杏</button>
            <button class="theme-btn" data-theme="paper">典雅雪白</button>
            <button class="theme-btn" data-theme="night">星夜深藍</button>
          </div>"""

    html = html.replace(old_theme_picker, new_theme_picker)

    # Update state default theme to milktea
    html = html.replace("theme: localStorage.getItem('ntuh_guardian_theme') || 'night'", "theme: localStorage.getItem('ntuh_guardian_theme') || 'milktea'")

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(html)

    print("Successfully transformed index.html to One-Page Milk Tea design!")

if __name__ == '__main__':
    apply_milktea_onepage()
