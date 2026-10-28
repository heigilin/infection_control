import os
import re

INDEX_PATH = '感控不踩雷網站/index.html'
PRESENTATION_PATH = '感控不踩雷網站/presentation.html'

def overhaul_index():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Mobile Overhaul CSS
    mobile_css = """
    /* =========================================================
       🔥 行動版極致體驗 (Mobile-First Intuitive UX Overhaul)
       修復版面擁擠、文字直立排列、按鈕擠壓與操作不直覺問題
       ========================================================= */
    .mobile-action-hub {
      display: none;
    }

    @media (max-width: 768px) {
      /* 頂部導覽列：極簡單行、無字元擠壓、乾淨俐落 */
      .site-nav {
        padding: 0.5rem 10px !important;
        position: sticky;
        top: 0;
        z-index: 100;
        background: rgba(8, 18, 15, 0.96) !important;
        backdrop-filter: blur(12px) !important;
        border-bottom: 1px solid rgba(45, 212, 191, 0.3) !important;
      }
      .nav-inner {
        flex-direction: row !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 8px !important;
        margin: 0 !important;
      }
      .nav-brand {
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
        min-width: 0 !important;
        flex: 1 1 auto !important;
      }
      .nav-logo {
        width: 32px !important;
        height: 32px !important;
        flex-shrink: 0 !important;
      }
      .nav-brand-text {
        min-width: 0 !important;
      }
      .nav-title {
        font-size: 0.92rem !important;
        font-weight: 900 !important;
        color: #ffffff !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
      }
      .nav-flow-hint {
        display: none !important; /* 手機端隱藏冗長小標，避免文字直立擠壓 */
      }
      .nav-links {
        display: flex !important;
        align-items: center !important;
        gap: 6px !important;
        flex-shrink: 0 !important;
        overflow-x: visible !important;
      }
      .nav-btn {
        padding: 0.32rem 0.6rem !important;
        font-size: 0.76rem !important;
        border-radius: 999px !important;
        gap: 4px !important;
      }
      /* 隱藏桌機版冗長的步驟 1/2 導引橫幅，手機改用專屬雙軌行動卡片 */
      .site-flow-roadmap {
        display: none !important;
      }

      /* 頁首 Masthead 精簡化 */
      .masthead {
        padding: 0.75rem 0.5rem 0.25rem !important;
        text-align: center !important;
      }
      .masthead-logo {
        display: none !important; /* 避免重複頭像佔據版面 */
      }
      .masthead .kicker {
        display: none !important;
      }
      .logo-title {
        font-size: 1.25rem !important;
        margin-bottom: 0.25rem !important;
        line-height: 1.3 !important;
      }
      .tagline {
        font-size: 0.8rem !important;
        margin-bottom: 0.75rem !important;
        color: #99f6e4 !important;
      }

      /* 🔥 手機雙軌直覺行動入口 (直覺二選一：讀教材 或 考測驗) */
      .mobile-action-hub {
        display: grid !important;
        grid-template-columns: 1fr;
        gap: 10px;
        margin: 0 0 16px;
      }
      .action-card {
        border-radius: 14px;
        padding: 14px 16px;
        text-decoration: none;
        display: block;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
        border: 1.5px solid;
        transition: transform 0.15s ease;
      }
      .action-card:active {
        transform: scale(0.98);
      }
      .card-learn-portal {
        background: linear-gradient(135deg, rgba(15, 118, 110, 0.3) 0%, rgba(6, 78, 59, 0.4) 100%);
        border-color: #2dd4bf;
      }
      .card-quiz-portal {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.35) 0%, rgba(15, 23, 42, 0.6) 100%);
        border-color: #38bdf8;
      }
      .action-card-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 6px;
      }
      .step-pill-1 {
        background: #2dd4bf;
        color: #042f2e;
        font-size: 11px;
        font-weight: 900;
        padding: 2px 8px;
        border-radius: 999px;
      }
      .step-pill-2 {
        background: #38bdf8;
        color: #082f49;
        font-size: 11px;
        font-weight: 900;
        padding: 2px 8px;
        border-radius: 999px;
      }
      .action-badge {
        font-size: 11.5px;
        color: #94a3b8;
        font-weight: 700;
      }
      .action-card-title {
        font-size: 1.05rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        gap: 6px;
      }
      .action-card-desc {
        font-size: 0.8rem;
        color: #cbd5e1;
        line-height: 1.45;
        margin: 0 0 10px;
      }
      .action-btn-pill {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        width: 100%;
        padding: 8px 12px;
        border-radius: 8px;
        font-size: 0.86rem;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
      }
      .btn-pill-learn {
        background: #0f766e;
        box-shadow: 0 2px 8px rgba(15, 118, 110, 0.4);
      }
      .btn-pill-quiz {
        background: #0284c7;
        box-shadow: 0 2px 8px rgba(2, 132, 199, 0.4);
      }

      /* 階段分頁列 (Phase Bar)：手機自適應膠囊設計 */
      .phase-bar {
        grid-template-columns: 1fr 1fr !important;
        gap: 8px !important;
        margin-bottom: 16px !important;
      }
      .phase-tab {
        padding: 10px 10px !important;
        border-radius: 12px !important;
        gap: 8px !important;
      }
      .phase-icon {
        font-size: 22px !important;
      }
      .phase-text small {
        display: none !important;
      }
      .phase-text strong {
        font-size: 0.84rem !important;
        white-space: nowrap !important;
      }

      /* 3D 場景畫布防誤觸：垂直滾動優先 */
      #world, #duel3DCanvas {
        touch-action: pan-y !important;
      }

      /* 闖關考題戰鬥舞台：縮減高度，留給考題選項最大可見度 */
      .duel-3d-stage-container {
        height: 135px !important;
      }
      .monster-card {
        padding: 8px 12px !important;
        gap: 8px !important;
        margin-bottom: 10px !important;
      }
      .monster-avatar {
        font-size: 28px !important;
      }
      .monster-meta h3 {
        font-size: 0.95rem !important;
        margin-bottom: 2px !important;
      }
      .monster-meta p {
        font-size: 0.78rem !important;
        line-height: 1.35 !important;
      }
      .question-prompt {
        font-size: 1rem !important;
        padding: 12px 14px !important;
        margin-bottom: 12px !important;
        line-height: 1.5 !important;
      }
      .quiz-options {
        gap: 8px !important;
        margin-bottom: 12px !important;
      }
      .option-btn {
        padding: 12px 14px !important;
        font-size: 0.88rem !important;
        min-height: 48px !important;
        border-radius: 10px !important;
      }

      /* 守護神檔案面板在手機端的優化 */
      .home-grid {
        gap: 16px !important;
      }
      .panel {
        padding: 14px 12px !important;
        border-radius: 14px !important;
      }
      .choice-card {
        padding: 12px !important;
      }
      .stepper {
        gap: 4px !important;
        padding: 6px 8px !important;
      }
      .stepper li {
        font-size: 0.78rem !important;
        padding: 4px 8px !important;
      }
    }
    """

    # Inject CSS before </style>
    if '/* 🔥 行動版極致體驗' not in content:
        content = content.replace('</style>', mobile_css + '\n</style>', 1)

    # 2. Add Mobile Action Hub HTML right below <header class="masthead">...</header>
    mobile_hub_html = """
    <!-- 手機端專屬：雙軌直覺行動入口 (一鍵直達 讀教材 vs 實戰考題) -->
    <div class="mobile-action-hub">
      <a class="action-card card-learn-portal" href="presentation.html" title="開啟步驟 1：10 大核心章節簡報與示範影片">
        <div class="action-card-header">
          <span class="step-pill-1">步驟 1</span>
          <span class="action-badge">核心指引 ＆ 示範影音</span>
        </div>
        <div class="action-card-title">📖 閱讀感控簡報教材 ↗</div>
        <p class="action-card-desc">完整 10 單元標準規範 · 標準肥皂水洗手示範影片</p>
        <div class="action-btn-pill btn-pill-learn">開啟簡報教材 ➔</div>
      </a>

      <div class="action-card card-quiz-portal" id="btnHeroQuizStart" style="cursor:pointer;" title="開啟步驟 2：臨床情境盲盒考題對決">
        <div class="action-card-header">
          <span class="step-pill-2">步驟 2</span>
          <span class="action-badge">盲盒對決 ＆ 守護神認證</span>
        </div>
        <div class="action-card-title">⚔️ 開始實戰情境闖關</div>
        <p class="action-card-desc">10 題臨床情境盲盒考驗 · 避開常見地雷 · 領取認證</p>
        <div class="action-btn-pill btn-pill-quiz">進入實戰測驗 ➔</div>
      </div>
    </div>
"""

    if 'class="mobile-action-hub"' not in content:
        pattern = r'(</header>\s*<!-- 階段切換導航)'
        content = re.sub(pattern, r'</header>\n' + mobile_hub_html + r'\n    <!-- 階段切換導航', content, count=1)

    # 3. Fix switchPhase in index.html to not force auto-scroll on initial load
    old_switch = """    function switchPhase(phase) {
      if (phase === 'learn') {
        if (tabPhaseLearn) tabPhaseLearn.classList.add('active');
        if (tabPhaseQuiz) tabPhaseQuiz.classList.remove('active');
        if (learnSection) learnSection.style.display = 'block';
        if (quizSetupSection) quizSetupSection.style.display = 'none';
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } else {
        if (tabPhaseLearn) tabPhaseLearn.classList.remove('active');
        if (tabPhaseQuiz) tabPhaseQuiz.classList.add('active');
        if (learnSection) learnSection.style.display = 'none';
        if (quizSetupSection) quizSetupSection.style.display = 'block';
        if (quizSetupSection) quizSetupSection.scrollIntoView({ behavior: 'smooth' });
      }
      sound.play('click');
    }"""

    new_switch = """    function switchPhase(phase, options = {}) {
      const autoScroll = options.scroll ?? true;
      if (phase === 'learn') {
        if (tabPhaseLearn) tabPhaseLearn.classList.add('active');
        if (tabPhaseQuiz) tabPhaseQuiz.classList.remove('active');
        if (learnSection) learnSection.style.display = 'block';
        if (quizSetupSection) quizSetupSection.style.display = 'none';
        if (autoScroll) window.scrollTo({ top: 0, behavior: 'smooth' });
      } else {
        if (tabPhaseLearn) tabPhaseLearn.classList.remove('active');
        if (tabPhaseQuiz) tabPhaseQuiz.classList.add('active');
        if (learnSection) learnSection.style.display = 'none';
        if (quizSetupSection) quizSetupSection.style.display = 'block';
        if (autoScroll && quizSetupSection) {
          quizSetupSection.scrollIntoView({ behavior: 'smooth' });
        }
      }
      if (options.playSound !== false) {
        sound.play('click');
      }
    }"""

    content = content.replace(old_switch, new_switch)

    # 4. Modify initial mode detection to not auto-scroll
    old_init = """    const urlParams = new URLSearchParams(window.location.search);
    const mode = urlParams.get('mode');
    if (mode === 'learn') {
      switchPhase('learn');
    } else {
      // 預設進入步驟 2 闖關，並提供回到步驟 1 閱讀教材
      switchPhase('quiz');
    }"""

    new_init = """    const urlParams = new URLSearchParams(window.location.search);
    const mode = urlParams.get('mode');
    if (mode === 'learn') {
      switchPhase('learn', { scroll: false, playSound: false });
    } else if (mode === 'quiz_scroll') {
      switchPhase('quiz', { scroll: true, playSound: false });
    } else {
      // 手機與桌機首頁載入：保留於頂端，展示清楚雙軌入口，不突兀跳躍
      switchPhase('quiz', { scroll: false, playSound: false });
    }

    const btnHeroQuizStart = document.getElementById('btnHeroQuizStart');
    if (btnHeroQuizStart) {
      btnHeroQuizStart.addEventListener('click', () => {
        switchPhase('quiz', { scroll: true, playSound: true });
      });
    }"""

    content = content.replace(old_init, new_init)

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("overhaul_index completed successfully.")

def overhaul_presentation():
    with open(PRESENTATION_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Mobile presentation CSS overhaul
    p_mobile_css = """
    /* =========================================================
       🔥 簡報行動版專屬優化 (Mobile-First Slide Reader)
       修復標題折行擠壓、全螢幕彈窗左右邊界過寬、上一張/下一張排版
       ========================================================= */
    @media (max-width: 768px) {
      .site-nav {
        padding: 0.5rem 10px !important;
        position: sticky;
        top: 0;
        z-index: 100;
      }
      .nav-inner {
        flex-direction: row !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 8px !important;
      }
      .nav-brand {
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
        min-width: 0 !important;
        flex: 1 1 auto !important;
      }
      .nav-logo {
        width: 32px !important;
        height: 32px !important;
        flex-shrink: 0 !important;
      }
      .nav-title {
        font-size: 0.92rem !important;
        font-weight: 900 !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
      }
      .nav-flow-hint {
        display: none !important;
      }
      .nav-links {
        display: flex !important;
        align-items: center !important;
        gap: 6px !important;
        flex-shrink: 0 !important;
      }
      .nav-btn {
        padding: 0.32rem 0.6rem !important;
        font-size: 0.76rem !important;
        border-radius: 999px !important;
      }
      .site-flow-roadmap {
        display: none !important;
      }

      /* 投影片彈窗 (Slide Modal) 行動全螢幕沉浸佈局 */
      .slide-modal {
        padding: 0 !important;
        background: #0f172a !important;
      }
      .slide-stage {
        height: 100vh !important;
        max-height: 100vh !important;
        width: 100vw !important;
        max-width: 100vw !important;
        border-radius: 0 !important;
        display: flex !important;
        flex-direction: column !important;
      }
      .slide-header {
        padding: 8px 10px !important;
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 8px !important;
        background: #0f241f !important;
        flex-shrink: 0 !important;
      }
      .slide-header-title {
        font-size: 13px !important;
        white-space: nowrap !important;
        color: #5eead4 !important;
        font-weight: 800 !important;
        flex-shrink: 0 !important;
      }
      .slide-header-controls {
        display: flex !important;
        align-items: center !important;
        gap: 6px !important;
        min-width: 0 !important;
        flex: 1 1 auto !important;
        justify-content: flex-end !important;
      }
      .slide-select {
        font-size: 12px !important;
        padding: 4px 6px !important;
        max-width: 150px !important;
        flex: 1 1 auto !important;
      }
      .slide-close-btn {
        padding: 4px 10px !important;
        font-size: 12px !important;
        white-space: nowrap !important;
        flex-shrink: 0 !important;
      }
      .slide-body {
        padding: 14px 12px !important;
        flex: 1 1 auto !important;
        overflow-y: auto !important;
        -webkit-overflow-scrolling: touch !important;
      }
      .slide-main-title {
        font-size: 19px !important;
        line-height: 1.35 !important;
        margin-bottom: 10px !important;
      }
      .slide-content-text {
        font-size: 14px !important;
        line-height: 1.6 !important;
        margin-bottom: 12px !important;
      }
      .slide-key-points {
        font-size: 13.5px !important;
        padding: 12px 14px !important;
        line-height: 1.65 !important;
      }
      /* 底部導引列 (Footer Navigation) */
      .slide-footer {
        padding: 8px 10px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 8px !important;
        background: #f8fafc !important;
        border-top: 1px solid #e2e8f0 !important;
        flex-shrink: 0 !important;
      }
      .slide-nav-btn {
        padding: 8px 12px !important;
        font-size: 13px !important;
        white-space: nowrap !important;
        flex: 1 1 0 !important;
        min-width: 80px !important;
        text-align: center !important;
      }
      .slide-counter {
        font-size: 12px !important;
        white-space: nowrap !important;
        flex: 0 0 auto !important;
        padding: 0 4px !important;
        text-align: center !important;
      }
      /* 示範影音在行動裝置的適應排版 */
      .slide-body video {
        width: 100% !important;
        max-height: 220px !important;
        border-radius: 8px !important;
      }
    }
    """

    if '/* 🔥 簡報行動版專屬優化' not in content:
        content = content.replace('</style>', p_mobile_css + '\n</style>', 1)

    with open(PRESENTATION_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("overhaul_presentation completed successfully.")

if __name__ == '__main__':
    overhaul_index()
    overhaul_presentation()
