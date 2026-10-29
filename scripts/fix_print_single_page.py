import re

with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add print CSS before </style>
print_css = """
    /* ===== 榮譽證書專用單頁列印樣式 (A4 Single Page Certificate Print) ===== */
    @page {
      size: A4 portrait;
      margin: 15mm 20mm;
    }

    @media print {
      /* 1. 隱藏背景所有非證書元件，杜絕多頁與背景文字外溢 */
      html, body {
        background: #ffffff !important;
        color: #2b1810 !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 100% !important;
        height: auto !important;
        overflow: visible !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }

      body > *:not(#dialogOverlay) {
        display: none !important;
      }

      .site-nav,
      .top-nav,
      #home,
      #arena,
      #hud,
      #ward3DContainer,
      #feedbackSheet,
      #questHud,
      #quizSetupSection,
      #dialogTitle,
      .dialog-header,
      .dialog-close,
      .no-print,
      footer {
        display: none !important;
      }

      /* 2. 重設彈窗為一般文檔流，取消 fixed 導致的跨頁重複列印現象 */
      #dialogOverlay {
        position: static !important;
        display: block !important;
        width: 100% !important;
        height: auto !important;
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
        backdrop-filter: none !important;
        box-shadow: none !important;
        inset: auto !important;
      }

      #dialogOverlay.hidden {
        display: none !important;
      }

      .card-sheet {
        position: static !important;
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
        max-height: none !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow: visible !important;
      }

      #dialogContent {
        padding: 0 !important;
        margin: 0 !important;
      }

      /* 3. 榮譽證書精緻單頁框排版，確保恰好容納於一張 A4 紙張內 */
      .cert-frame {
        position: static !important;
        box-sizing: border-box !important;
        width: 100% !important;
        max-width: 680px !important;
        margin: 20px auto 0 !important;
        padding: 36px 32px !important;
        background: #ffffff !important;
        border: 4px double #8c674b !important;
        border-radius: 12px !important;
        box-shadow: none !important;
        text-align: center !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
      }

      .cert-seal {
        font-size: 3.5rem !important;
        line-height: 1 !important;
        margin-bottom: 8px !important;
        animation: none !important;
      }

      .cert-title {
        font-family: 'Playfair Display', Georgia, serif !important;
        font-size: 1.45rem !important;
        color: #633e24 !important;
        margin: 0 0 4px !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px !important;
      }

      .cert-sub {
        font-size: 0.82rem !important;
        color: #7d6b5e !important;
        margin: 0 0 16px !important;
        letter-spacing: 1px !important;
      }

      .cert-user {
        font-size: 1.55rem !important;
        font-weight: 900 !important;
        color: #2b1810 !important;
        border-bottom: 2px solid #8c674b !important;
        padding: 0 20px 4px !important;
        margin-bottom: 16px !important;
        display: inline-block !important;
      }

      .cert-words {
        font-size: 0.92rem !important;
        color: #423228 !important;
        line-height: 1.7 !important;
        max-width: 540px !important;
        margin: 0 auto 20px !important;
      }

      .cert-meta-row {
        display: flex !important;
        justify-content: space-around !important;
        border-top: 1.5px dashed #c9b4a1 !important;
        padding-top: 14px !important;
        margin-top: 10px !important;
        font-size: 0.8rem !important;
        color: #635043 !important;
        flex-wrap: wrap !important;
        gap: 12px !important;
      }

      .cert-meta-row strong {
        color: #2b1810 !important;
      }

      /* 4. 嚴格隱藏所有按鈕與宣傳條，杜絕非證書文字印出 */
      .cert-frame button,
      .cert-frame .main-btn,
      .cert-frame .ghost-btn,
      .no-print {
        display: none !important;
      }
    }
"""

if '</style>' in c and '@media print' not in c:
    c = c.replace('</style>', print_css + '\n  </style>', 1)
    print("Added @media print styles to index.html")
else:
    print("Note: @media print already present or </style> not found")

# 2. Update finishDuels to guard against duplicate triggers
old_finish_duels = """    function finishDuels() {
      sound.play('win');
      arenaEl.classList.add('hidden');
      hudEl.classList.add('hidden');
      const wCont = document.getElementById('ward3DContainer');
      if (wCont) wCont.classList.add('hidden');
      const topNavEl = document.querySelector('.top-nav');
      if (topNavEl) topNavEl.style.display = '';
      document.getElementById('home').style.display = 'block';
      showCertificate();
    }"""

new_finish_duels = """    function finishDuels() {
      if (state.finishedDuels) return;
      state.finishedDuels = true;
      sound.play('win');
      arenaEl.classList.add('hidden');
      hudEl.classList.add('hidden');
      const wCont = document.getElementById('ward3DContainer');
      if (wCont) wCont.classList.add('hidden');
      const topNavEl = document.querySelector('.top-nav');
      if (topNavEl) topNavEl.style.display = '';
      document.getElementById('home').style.display = 'block';
      showCertificate();
    }"""

if old_finish_duels in c:
    c = c.replace(old_finish_duels, new_finish_duels)
    print("Added debounce guard to finishDuels")

# 3. Reset state.finishedDuels in startAdventure
old_reset_state = """      state.currentQ = 0;
      state.score = 0;
      state.shield = 100;
      state.mistakes = [];"""

new_reset_state = """      state.currentQ = 0;
      state.score = 0;
      state.shield = 100;
      state.mistakes = [];
      state.finishedDuels = false;"""

if old_reset_state in c:
    c = c.replace(old_reset_state, new_reset_state)
    print("Added state.finishedDuels reset to startAdventure")

# 4. Add .no-print to LINE banner and button row in certHtml
old_cert_extra = """          <div style="background:rgba(6, 78, 59, 0.35); border:1.5px solid #10b981; border-radius:10px; padding:14px; margin:1.25rem 0 0.5rem; text-align:left;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:6px;">
              <strong style="color:#a7f3d0; font-size:14.5px;">📱 臨床工作別單打獨鬥！將感控專家裝進手機口袋</strong>
              <span style="background:#06c755; color:#fff; font-size:12px; font-weight:800; padding:2px 8px; border-radius:999px;">@ntuhic</span>
            </div>
            <div style="font-size:13px; color:#ecfdf5; line-height:1.6;">
              日常值班秒查 <strong>隔離醫囑與規範</strong>、<strong>口袋 PPE 圖解</strong>與<strong>法傳通報時限</strong>，24 小時隨身待命不用等電話！
            </div>
            <div style="margin-top:8px; text-align:right;">
              <a href="https://line.me/R/ti/p/@ntuhic" target="_blank" rel="noopener" style="background:#06c755; color:#fff !important; font-weight:900; padding:6px 16px; border-radius:999px; font-size:13px; text-decoration:none; display:inline-flex; align-items:center; gap:4px;">👉 一鍵加入台大感管 LINE 帳號 ↗</a>
            </div>
          </div>
          <div style="margin-top:1.5rem; display:flex; justify-content:center; gap:0.75rem; flex-wrap:wrap;">
            <button class="main-btn" onclick="window.print()">🖨️ 列印 / 保存為 PDF</button>
            <a class="ghost-btn" href="#sec-learn" style="color:var(--mint); border-color:var(--mint); font-weight:800;">
              📑 複習核心簡報教材 ↗
            </a>
            <a class="ghost-btn" href="admin.html" target="_blank" rel="noopener" style="background:var(--slate-3); color:#ffd166; border-color:var(--accent);">
              📊 病房主管成果看板 ↗
            </a>
          </div>"""

new_cert_extra = """          <div class="no-print" style="background:rgba(6, 78, 59, 0.35); border:1.5px solid #10b981; border-radius:10px; padding:14px; margin:1.25rem 0 0.5rem; text-align:left;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:6px;">
              <strong style="color:#a7f3d0; font-size:14.5px;">📱 臨床工作別單打獨鬥！將感控專家裝進手機口袋</strong>
              <span style="background:#06c755; color:#fff; font-size:12px; font-weight:800; padding:2px 8px; border-radius:999px;">@ntuhic</span>
            </div>
            <div style="font-size:13px; color:#ecfdf5; line-height:1.6;">
              日常值班秒查 <strong>隔離醫囑與規範</strong>、<strong>口袋 PPE 圖解</strong>與<strong>法傳通報時限</strong>，24 小時隨身待命不用等電話！
            </div>
            <div style="margin-top:8px; text-align:right;">
              <a href="https://line.me/R/ti/p/@ntuhic" target="_blank" rel="noopener" style="background:#06c755; color:#fff !important; font-weight:900; padding:6px 16px; border-radius:999px; font-size:13px; text-decoration:none; display:inline-flex; align-items:center; gap:4px;">👉 一鍵加入台大感管 LINE 帳號 ↗</a>
            </div>
          </div>
          <div class="no-print" style="margin-top:1.5rem; display:flex; justify-content:center; gap:0.75rem; flex-wrap:wrap;">
            <button class="main-btn" onclick="window.print()">🖨️ 列印 / 保存為 PDF</button>
            <a class="ghost-btn" href="#sec-learn" onclick="document.getElementById('dialogOverlay').classList.add('hidden')" style="color:var(--mint); border-color:var(--mint); font-weight:800;">
              📑 複習核心簡報教材 ↗
            </a>
            <a class="ghost-btn" href="admin.html" target="_blank" rel="noopener" style="background:var(--slate-3); color:#ffd166; border-color:var(--accent);">
              📊 病房主管成果看板 ↗
            </a>
          </div>"""

if old_cert_extra in c:
    c = c.replace(old_cert_extra, new_cert_extra)
    print("Added no-print class to promotional banner and button row")

with open('感控不踩雷網站/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Saved 감控不踩雷網站/index.html")
