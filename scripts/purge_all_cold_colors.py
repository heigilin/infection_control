import re

INDEX_FILE = '感控不踩雷網站/index.html'

def purge_cold():
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Clean the section between </header> (masthead) and line card / learn-cards
    # Remove any broken tags and insert the clean sec-learn header
    old_fragment_pattern = r'</header>\s*(?:<div class="action-card-title".*?</div>\s*</div>\s*)?'
    clean_learn_start = """</header>

    <!-- ===== 第一階段：9 大核心實戰指引速查 ===== -->
    <section class="learn-panel" id="sec-learn">
      <div class="onepage-section-header">
        <div>
          <h2 class="onepage-section-title"><span>📖</span> 第一階段：臺大醫院 9 大核心實戰指引速查</h2>
          <p class="onepage-section-desc">感染管制不是生硬的規定，而是臨床游刃有餘的專業底氣。請詳閱以下 9 大重點，順流向下滑動即可進行實戰闖關：</p>
        </div>
      </div>
"""

    html = re.sub(r'</header>\s*<div class="action-card-title">.*?</div>\s*</div>', clean_learn_start, html, flags=re.DOTALL)
    if 'id="sec-learn"' not in html:
        html = html.replace('</header>', clean_learn_start, 1)

    # 2. Replace all cold rgba colors with warm milk tea colors
    # 2.1 Cyan/mint glows (52, 211, 180) -> warm caramel/tea (140, 103, 75)
    html = re.sub(r'rgba\(\s*52,\s*211,\s*180,\s*([0-9\.]+)\)', r'rgba(140, 103, 75, \1)', html)
    # 2.2 Mint accents (45, 212, 191) -> warm caramel (184, 123, 78)
    html = re.sub(r'rgba\(\s*45,\s*212,\s*191,\s*([0-9\.]+)\)', r'rgba(184, 123, 78, \1)', html)
    # 2.3 Dark teals (15, 118, 110) & (13, 148, 136) -> warm dark roast (89, 63, 44)
    html = re.sub(r'rgba\(\s*15,\s*118,\s*110,\s*([0-9\.]+)\)', r'rgba(89, 63, 44, \1)', html)
    html = re.sub(r'rgba\(\s*13,\s*148,\s*136,\s*([0-9\.]+)\)', r'rgba(89, 63, 44, \1)', html)
    # 2.4 Dark navy blue backgrounds (17, 26, 46) -> warm white/ivory
    html = re.sub(r'rgba\(\s*17,\s*26,\s*46,\s*([0-9\.]+)\)', r'rgba(255, 255, 255, 0.95)', html)
    # 2.5 Dark slate (15, 23, 42) -> white card
    html = re.sub(r'rgba\(\s*15,\s*23,\s*42,\s*([0-9\.]+)\)', r'#ffffff', html)

    # 3. Replace all remaining cold hex colors
    html = html.replace('#2dd4bf', 'var(--milktea-accent)')
    html = html.replace('#0f766e', 'var(--milktea-accent)')
    html = html.replace('#14b8a6', 'var(--milktea-border)')
    html = html.replace('#5eead4', 'var(--milktea-caramel)')
    html = html.replace('#99f6e4', 'var(--milktea-muted)')
    html = html.replace('#38bdf8', 'var(--milktea-caramel)')
    html = html.replace('#090e1a', '#f9f6f0')
    html = html.replace('#111a2e', '#ffffff')
    html = html.replace('#18233c', '#fbf8f3')
    html = html.replace('#0f241f', '#36241a')
    html = html.replace('#040d0b', '#faf6f0')
    html = html.replace('#115e59', 'var(--milktea-border)')
    html = html.replace('#059669', 'var(--milktea-accent)')

    # 4. Enhance .cta-go-quiz to pure milk tea
    cta_css = """
    .cta-go-quiz {
      background: linear-gradient(135deg, var(--milktea-accent) 0%, var(--milktea-caramel) 100%) !important;
      color: #ffffff !important;
      border: none !important;
      padding: 16px 28px !important;
      border-radius: 12px !important;
      font-size: 1.1rem !important;
      font-weight: 800 !important;
      box-shadow: 0 6px 20px rgba(140, 103, 75, 0.3) !important;
      cursor: pointer !important;
      transition: all 0.2s ease !important;
    }
    .cta-go-quiz:hover {
      background: linear-gradient(135deg, var(--milktea-accent-hover) 0%, #6e492e) !important;
      box-shadow: 0 8px 24px rgba(140, 103, 75, 0.45) !important;
      transform: translateY(-2px) !important;
    }
    """
    if '.cta-go-quiz {' in html and 'linear-gradient(135deg, var(--milktea-accent)' not in html:
        html = html.replace('</style>', cta_css + '\n</style>', 1)

    # 5. Fix smooth scroll for btnGoToQuiz
    html = html.replace("if (btnGoToQuiz) btnGoToQuiz.addEventListener('click', () => switchPhase('quiz'));", "if (btnGoToQuiz) btnGoToQuiz.addEventListener('click', () => { const q = document.getElementById('sec-quiz'); if (q) q.scrollIntoView({ behavior: 'smooth' }); });")

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(html)

    print("Purge all cold colors completed successfully!")

if __name__ == '__main__':
    purge_cold()
