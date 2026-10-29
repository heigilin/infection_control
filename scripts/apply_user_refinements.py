import re
import os

INDEX_FILE = '感控不踩雷網站/index.html'
PRESENTATION_FILE = '感控不踩雷網站/presentation.html'
ADMIN_FILE = '感控不踩雷網站/admin.html'

def refine_all():
    # =========================================================================
    # 1. 替換「底氣」為臺灣臨床自然用詞 (專業把關 / 扎實實力 / 專業防線)
    # =========================================================================
    files_to_check = [INDEX_FILE, PRESENTATION_FILE, ADMIN_FILE]
    for fpath in files_to_check:
        with open(fpath, 'r', encoding='utf-8') as f:
            t = f.read()

        # 替換各種底氣相關語句
        t = t.replace('用最專業的底氣', '用最扎實的專業實力')
        t = t.replace('用最溫暖專業的底氣', '用最扎實的專業把關')
        t = t.replace('專業的底氣', '專業把關')
        t = t.replace('專業底氣', '專業把關')
        t = t.replace('守護神底氣', '守護神專業實力')
        t = t.replace('黃金底氣', '琥珀金光')
        t = t.replace('底氣', '專業實力')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(t)
        print(f"Purged '底氣' from {fpath}")

    # =========================================================================
    # 2. 處理 index.html 專屬細節
    # =========================================================================
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    # 2.1 移除 Image 1 紅框：.masthead-links
    masthead_links_pattern = r'<div class="masthead-links">.*?</div>'
    html = re.sub(masthead_links_pattern, '', html, flags=re.DOTALL)
    print("Removed .masthead-links from masthead")

    # 2.2 移除 Image 2 紅框：學習卡片中的「• ①」、「• ②」、「• ③」、「• 🚨」
    html = html.replace('• <strong>①', '<strong>①')
    html = html.replace('• <strong>②', '<strong>②')
    html = html.replace('• <strong>③', '<strong>③')
    html = html.replace('• <strong style="color:#ef4444;">🚨', '<strong style="color:#b74f41;">🚨')
    html = html.replace('• 🚨', '🚨')
    html = html.replace('• <strong>🚨', '<strong>🚨')
    print("Removed redundant bullets before numbers and alert emojis")

    # 2.3 修改 Image 3：避免標籤底色被誤認為是按鈕
    # 將「🎬 示範影音教材 ＋ 步驟圖解」等徽章改為非按鈕式的淡雅線條標籤
    old_badge_1 = r'<span style="background:var\(--accent\);\s*color:#fff;\s*font-size:12\.5px;\s*font-weight:800;\s*padding:4px 12px;\s*border-radius:999px;">\s*🎬 示範影音教材 ＋ 步驟圖解\s*</span>'
    new_badge_1 = '<span style="background:transparent; color:var(--milktea-accent); font-size:12px; font-weight:700; padding:2px 10px; border:1px dashed var(--milktea-border-dk); border-radius:4px;">🎬 示範影音教材 ＋ 步驟圖解</span>'
    html = re.sub(old_badge_1, new_badge_1, html)

    # 還有 LINE 卡片的標籤
    old_line_badge = r'<span style="background:#527961;\s*color:#ffffff;\s*font-size:12\.5px;\s*font-weight:700;\s*padding:4px 12px;\s*border-radius:999px;">LINE ID: @ntuhic ✦ 24hr 口袋感控顧問</span>'
    new_line_badge = '<span style="background:transparent; color:var(--milktea-sage); font-size:12px; font-weight:700; padding:2px 10px; border:1px solid var(--milktea-border); border-radius:4px;">LINE ID: @ntuhic ✦ 24hr 口袋感控顧問</span>'
    html = re.sub(old_line_badge, new_line_badge, html)

    # choice-badge 樣式優化，避免像按鈕
    badge_css_override = """
    .choice-badge {
      background: transparent !important;
      color: var(--milktea-accent) !important;
      border: 1px solid var(--milktea-border-dk) !important;
      box-shadow: none !important;
      font-weight: 700 !important;
    }
    """
    if '.choice-badge {' not in html:
        html = html.replace('</style>', badge_css_override + '\n</style>', 1)

    print("Refined badges so they are not mistaken for clickable buttons")

    # 2.4 移除 Image 4：刪除多餘的「我已熟讀以上重點，立即進入第二階段實戰闖關對決」按鈕
    btn_go_quiz_pattern = r'<button type="button" class="cta-go-quiz" id="btnGoToQuiz">.*?</button>'
    html = re.sub(btn_go_quiz_pattern, '', html, flags=re.DOTALL)
    print("Removed redundant btnGoToQuiz button")

    # =========================================================================
    # 3. 「可以不要選場域」：重構闖關區，移除選場域與 Stepper 繁瑣分頁
    # =========================================================================
    # 找到 quizSetupSection 內容並簡化為單一卡片直覺登入：
    # 直接輸入病房、姓名、選擇身分，一鍵開始測驗
    old_quiz_setup_pattern = r'<div class="home-grid">.*?<!-- 右側：角色設定面板 \(Profile Panel\) -->\s*<aside class="profile panel">.*?</aside>\s*</div>'
    
    clean_quiz_setup_html = """<div class="home-grid" style="display:grid; grid-template-columns: 1.2fr 0.8fr; gap:20px; align-items:start;">
      <!-- 左側：職別與單位身分設定 (無需繁瑣選場域，直覺登入) -->
      <section class="panel" style="padding:24px; background:#ffffff; border:1.5px solid var(--milktea-border); border-radius:var(--radius); box-shadow:0 4px 20px rgba(89,63,44,0.06);">
        <div style="margin-bottom:18px;">
          <h3 style="font-size:1.15rem; font-weight:900; color:var(--milktea-heading); margin-bottom:4px; display:flex; align-items:center; gap:8px;">
            <span>🩺</span> 請選擇您的臨床職別
          </h3>
          <p style="font-size:0.85rem; color:var(--milktea-muted); margin:0;">
            系統將根據您的專業職別，動態適配防護策略與專屬考點重點：
          </p>
        </div>

        <!-- 職別選擇卡片網格 -->
        <div class="choice-grid" id="roleChoiceGrid" style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:16px;">
          <div class="choice-card selected" data-role="護理師" data-icon="🩺" style="cursor:pointer;">
            <div style="font-size:11px; color:var(--milktea-accent); font-weight:700; margin-bottom:2px;">前線核心照護</div>
            <div class="choice-icon" style="font-size:26px; margin-bottom:4px;">🩺</div>
            <h4 style="margin:0 0 4px; font-size:1.05rem; color:var(--milktea-heading);">護理師</h4>
            <p style="font-size:0.78rem; color:var(--milktea-muted); margin:0; line-height:1.4;">
              門口備 PPE 車、病人間洗手、杜絕摸分泌物後管灌、即刻衛教紀錄。
            </p>
          </div>
          <div class="choice-card" data-role="醫師" data-icon="👨‍⚕️" style="cursor:pointer;">
            <div style="font-size:11px; color:var(--milktea-accent); font-weight:700; margin-bottom:2px;">精準抗藥菌與置管決策</div>
            <div class="choice-icon" style="font-size:26px; margin-bottom:4px;">👨‍⚕️</div>
            <h4 style="margin:0 0 4px; font-size:1.05rem; color:var(--milktea-heading);">醫師</h4>
            <p style="font-size:0.78rem; color:var(--milktea-muted); margin:0; line-height:1.4;">
              見 MDRO 即刻開立隔離醫囑；中心導管置管前超音波評估必備「無菌傳導膠」。
            </p>
          </div>
          <div class="choice-card" data-role="清潔人員" data-icon="🧹" style="cursor:pointer;">
            <div style="font-size:11px; color:var(--milktea-accent); font-weight:700; margin-bottom:2px;">環境無菌防護</div>
            <div class="choice-icon" style="font-size:26px; margin-bottom:4px;">🧹</div>
            <h4 style="margin:0 0 4px; font-size:1.05rem; color:var(--milktea-heading);">清潔人員</h4>
            <p style="font-size:0.78rem; color:var(--milktea-muted); margin:0; line-height:1.4;">
              認明隔離牌、穿戴手套隔離衣；先清一般後清 MDRO，跨病房間絕不穿同一雙髒手套。
            </p>
          </div>
          <div class="choice-card" data-role="其他" data-icon="🌟" style="cursor:pointer;">
            <div style="font-size:11px; color:var(--milktea-accent); font-weight:700; margin-bottom:2px;">跨科協同把關</div>
            <div class="choice-icon" style="font-size:26px; margin-bottom:4px;">🌟</div>
            <h4 style="margin:0 0 4px; font-size:1.05rem; color:var(--milktea-heading);">其他醫事同仁</h4>
            <p style="font-size:0.78rem; color:var(--milktea-muted); margin:0; line-height:1.4;">
              呼吸治療師、放射師、照服員、營養送餐等，遵守進出隔離與洗手直覺。
            </p>
          </div>
        </div>

        <div id="otherRoleBox" style="display:none; margin-top:8px; margin-bottom:14px;">
          <input type="text" id="customRoleInput" class="text-input" placeholder="請自訂您的職別（如：呼吸治療師、醫事放射師...）" style="width:100%; padding:8px 12px; border-radius:8px; font-size:13.5px;">
        </div>

        <!-- 挑戰題庫模式 -->
        <div style="display:flex; align-items:center; justify-content:space-between; gap:10px; background:#fbf7f1; padding:10px 14px; border-radius:10px; border:1px solid var(--milktea-border);">
          <span style="font-size:0.85rem; font-weight:800; color:var(--milktea-heading);">挑戰模式：</span>
          <div style="display:flex; gap:8px;">
            <button type="button" class="mode-select-btn active" id="btnModeFull" data-mode="full" style="padding:4px 12px; font-size:12.5px; border-radius:6px; border:1px solid var(--milktea-accent); background:var(--milktea-accent); color:#ffffff; font-weight:700; cursor:pointer;">全方位實戰 (5題)</button>
            <button type="button" class="mode-select-btn" id="btnModeRapid" data-mode="rapid" style="padding:4px 12px; font-size:12.5px; border-radius:6px; border:1px solid var(--milktea-border); background:#ffffff; color:var(--milktea-body); font-weight:700; cursor:pointer;">極速避雷 (5題)</button>
          </div>
        </div>
      </section>

      <!-- 右側：同仁姓名與病房登錄面板 -->
      <aside class="panel" style="padding:24px; background:#ffffff; border:1.5px solid var(--milktea-border); border-radius:var(--radius); box-shadow:0 4px 20px rgba(89,63,44,0.06);">
        <h3 style="font-size:1.15rem; font-weight:900; color:var(--milktea-heading); margin-bottom:14px; display:flex; align-items:center; gap:8px;">
          <span>👤</span> 填入您的同仁資料
        </h3>

        <div style="margin-bottom:14px;">
          <label for="stepRoleWard" style="display:block; font-weight:800; font-size:13.5px; margin-bottom:6px; color:var(--milktea-heading);">
            🏥 所屬病房 / 臨床單位名稱：
          </label>
          <input type="text" id="stepRoleWard" class="text-input" maxlength="20" placeholder="例如：5B 病房、7D、加護病房、急診..." style="width:100%; font-size:14px; padding:9px 12px; border-radius:8px;">
        </div>

        <div style="margin-bottom:18px;">
          <label for="playerNick" style="display:block; font-weight:800; font-size:13.5px; margin-bottom:6px; color:var(--milktea-heading);">
            ✍️ 您的暱稱 / 姓名（證書顯示）：
          </label>
          <input type="text" id="playerNick" class="text-input" maxlength="12" placeholder="請輸入姓名（例如：雅琪）" style="width:100%; font-size:14px; padding:9px 12px; border-radius:8px;">
        </div>

        <div style="margin-bottom:20px; display:flex; align-items:center; justify-content:space-between; font-size:13px; color:var(--milktea-muted);">
          <span>🎵 音效反饋：</span>
          <button type="button" class="opt-btn active" id="btnAudioToggle" style="padding:4px 12px; border-radius:6px; font-size:12px; font-weight:700; border:1px solid var(--milktea-border); background:#fcf8f3; color:var(--milktea-heading); cursor:pointer;">🔊 音效開啟</button>
        </div>

        <!-- 核心出發按鈕：極大化、醒目、一觸即發 -->
        <button class="main-btn" id="btnStartAdventure" style="width:100%; padding:14px 20px; font-size:16px; font-weight:900; border-radius:10px; display:flex; align-items:center; justify-content:center; gap:8px; cursor:pointer;">
          <span>⚔️</span> 進入情境對決戰場（開始測驗）➔
        </button>
      </aside>
    </div>"""

    html = re.sub(old_quiz_setup_pattern, clean_quiz_setup_html, html, flags=re.DOTALL)
    print("Simplified quiz setup (removed field selection, unified inputs and role picker)")

    # 3.1 確保 JavaScript 兼容簡化後的測驗登入流程
    # 支援模式按鈕點擊切換
    mode_js_patch = """
    // 挑戰模式切換 (全方位 vs 極速避雷)
    const btnModeFull = document.getElementById('btnModeFull');
    const btnModeRapid = document.getElementById('btnModeRapid');
    if (btnModeFull && btnModeRapid) {
      btnModeFull.addEventListener('click', () => {
        state.mode = 'full';
        btnModeFull.classList.add('active');
        btnModeFull.style.background = 'var(--milktea-accent)';
        btnModeFull.style.color = '#ffffff';
        btnModeRapid.classList.remove('active');
        btnModeRapid.style.background = '#ffffff';
        btnModeRapid.style.color = 'var(--milktea-body)';
      });
      btnModeRapid.addEventListener('click', () => {
        state.mode = 'rapid';
        btnModeRapid.classList.add('active');
        btnModeRapid.style.background = 'var(--milktea-accent)';
        btnModeRapid.style.color = '#ffffff';
        btnModeFull.classList.remove('active');
        btnModeFull.style.background = '#ffffff';
        btnModeFull.style.color = 'var(--milktea-body)';
      });
    }
    """
    if 'btnModeFull' not in html:
        html = html.replace('document.getElementById(\'btnStartAdventure\').addEventListener(\'click\', startAdventure);', mode_js_patch + '\n    document.getElementById(\'btnStartAdventure\').addEventListener(\'click\', startAdventure);')

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html refinements applied successfully!")

if __name__ == '__main__':
    refine_all()
