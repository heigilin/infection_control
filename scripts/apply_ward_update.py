import sys

sys.stdout.reconfigure(encoding='utf-8')

# --- 1. Modify 感控不踩雷網站/index.html ---
with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# 1a. Add playerWard to sidebar profile panel
old_nick_row = '''        <div class="form-row">
          <label for="playerNick">守護神暱稱 / 姓名</label>
          <input type="text" id="playerNick" class="text-input" maxlength="12" placeholder="請輸入姓名（例如：雅琪）" value="">
        </div>'''

new_nick_and_ward_rows = '''        <div class="form-row">
          <label for="playerNick">守護神暱稱 / 姓名</label>
          <input type="text" id="playerNick" class="text-input" maxlength="12" placeholder="請輸入姓名（例如：雅琪）" value="">
        </div>

        <div class="form-row">
          <label for="playerWard">🏥 所屬病房 / 單位</label>
          <input type="text" id="playerWard" class="text-input" maxlength="20" placeholder="請輸入病房（例如：5B 病房、7D、加護病房）" value="">
        </div>'''

if old_nick_row in idx_content:
    idx_content = idx_content.replace(old_nick_row, new_nick_and_ward_rows)
    print("1a. playerWard added to sidebar")

# 1b. Add stepRoleWard to stepRole pane
old_step_head = '''          <!-- Step 2: 選身分 (護理師 / 醫師 / 清潔人員 / 其他) -->
          <div id="stepRole" class="step-pane" style="display:none;">
            <div class="picker-head">
              <h2><span>👤</span> 選擇您的臨床職別身分</h2>
              <p>不同崗位，一樣優雅！系統將根據職別動態適配防護策略與專屬考點：</p>
            </div>'''

new_step_head = '''          <!-- Step 2: 選身分 (護理師 / 醫師 / 清潔人員 / 其他) -->
          <div id="stepRole" class="step-pane" style="display:none;">
            <div class="picker-head">
              <h2><span>👤</span> 登入身分與所屬病房</h2>
              <p>不同崗位，一樣優雅！系統將根據您的單位與職別動態適配防護策略與專屬考點：</p>
            </div>

            <!-- 病房單位填寫 -->
            <div style="margin-bottom:1.25rem; background:rgba(16, 185, 129, 0.08); border:1.5px solid rgba(16, 185, 129, 0.35); padding:1rem; border-radius:12px;">
              <label for="stepRoleWard" style="display:flex; align-items:center; gap:6px; font-weight:800; font-size:14px; margin-bottom:0.4rem; color:var(--mint);">
                <span>🏥</span> 請填寫您的所屬病房 / 臨床單位名稱：
              </label>
              <input type="text" id="stepRoleWard" class="text-input" maxlength="20" placeholder="例如：5B 病房、7D 病房、內科加護病房、急診醫學部..." style="width:100%; font-size:14px; padding:0.6rem 0.8rem; background:var(--card-bg, #1a2234); color:inherit; border:1px solid var(--border); border-radius:8px;">
            </div>'''

if old_step_head in idx_content:
    idx_content = idx_content.replace(old_step_head, new_step_head)
    print("1b. stepRoleWard added to stepRole")
else:
    print("WARNING: old_step_head not found")

# 1c. Update state definition to include ward
old_state = '''    const state = {
      step: 1,
      field: 'ward',
      role: '護理師',
      customRole: '',
      mode: 'full',
      nick: localStorage.getItem('ntuh_guardian_nick') || '',
      theme: localStorage.getItem('ntuh_guardian_theme') || 'night',
      auraColor: localStorage.getItem('ntuh_guardian_aura') || '#ffd166',
      currentQ: 0,
      score: 0,
      shield: 100,
      mistakes: [],
      answered: false
    };'''

new_state = '''    const state = {
      step: 1,
      field: 'ward',
      role: '護理師',
      customRole: '',
      mode: 'full',
      nick: localStorage.getItem('ntuh_guardian_nick') || '',
      ward: localStorage.getItem('ntuh_guardian_ward') || '',
      theme: localStorage.getItem('ntuh_guardian_theme') || 'night',
      auraColor: localStorage.getItem('ntuh_guardian_aura') || '#ffd166',
      currentQ: 0,
      score: 0,
      shield: 100,
      mistakes: [],
      answered: false
    };'''

if old_state in idx_content:
    idx_content = idx_content.replace(old_state, new_state)
    print("1c. state.ward added")
else:
    print("WARNING: old_state not found")

# 1d. Add input sync for ward in script setup
old_nick_init = '''    // 暱稱
    const playerNickInput = document.getElementById('playerNick');
    playerNickInput.value = state.nick;
    playerNickInput.addEventListener('input', () => {
      state.nick = playerNickInput.value.trim();
    });'''

new_nick_and_ward_init = '''    // 暱稱與病房單位
    const playerNickInput = document.getElementById('playerNick');
    const playerWardInput = document.getElementById('playerWard');
    const stepRoleWardInput = document.getElementById('stepRoleWard');

    playerNickInput.value = state.nick;
    if (state.ward) {
      if (playerWardInput) playerWardInput.value = state.ward;
      if (stepRoleWardInput) stepRoleWardInput.value = state.ward;
    }

    playerNickInput.addEventListener('input', () => {
      state.nick = playerNickInput.value.trim();
    });

    // 雙向同步病房輸入
    if (playerWardInput && stepRoleWardInput) {
      playerWardInput.addEventListener('input', () => {
        state.ward = playerWardInput.value.trim();
        stepRoleWardInput.value = playerWardInput.value;
        localStorage.setItem('ntuh_guardian_ward', state.ward);
      });
      stepRoleWardInput.addEventListener('input', () => {
        state.ward = stepRoleWardInput.value.trim();
        playerWardInput.value = stepRoleWardInput.value;
        localStorage.setItem('ntuh_guardian_ward', state.ward);
      });
    }'''

if old_nick_init in idx_content:
    idx_content = idx_content.replace(old_nick_init, new_nick_and_ward_init)
    print("1d. nick & ward init wired")
else:
    print("WARNING: old_nick_init not found")

# 1e. Update startAdventure to read and store ward, and display in HUD
old_start_adventure = '''    function startAdventure() {
      state.nick = playerNickInput.value.trim() || '雅琪';
      if (state.role === '其他') {
        state.customRole = customRoleInput.value.trim() || '醫事同仁';
      }
      localStorage.setItem('ntuh_guardian_nick', state.nick);

      const displayRole = state.role === '其他' && state.customRole ? state.customRole : state.role;
      hudPlayerName.textContent = `${state.nick} (${displayRole})`;'''

new_start_adventure = '''    function startAdventure() {
      state.nick = playerNickInput.value.trim() || '雅琪';
      const inputWard = (playerWardInput ? playerWardInput.value.trim() : '') || (stepRoleWardInput ? stepRoleWardInput.value.trim() : '');
      state.ward = inputWard || state.ward || '一般病房';
      if (state.role === '其他') {
        state.customRole = customRoleInput.value.trim() || '醫事同仁';
      }
      localStorage.setItem('ntuh_guardian_nick', state.nick);
      localStorage.setItem('ntuh_guardian_ward', state.ward);

      const displayRole = state.role === '其他' && state.customRole ? state.customRole : state.role;
      hudPlayerName.textContent = `${state.nick} · ${state.ward} (${displayRole})`;'''

if old_start_adventure in idx_content:
    idx_content = idx_content.replace(old_start_adventure, new_start_adventure)
    print("1e. startAdventure updated")
else:
    print("WARNING: old_start_adventure not found")

# 1f. Update record creation and certificate in finishDuels
old_record = '''      const record = {
        id: 'REC-' + Date.now(),
        name: state.nick || '未填寫',
        role: displayRole,
        field: state.field,
        score: state.score,
        shield: state.shield,
        serial: serial,
        date: `${dateStr} ${timeStr}`,
        timestamp: now.toISOString(),
        passed: state.score >= 80,
        mistakesCount: (state.mistakes || []).length,
        mistakes: state.mistakes || []
      };'''

new_record = '''      const record = {
        id: 'REC-' + Date.now(),
        name: state.nick || '未填寫',
        ward: state.ward || '一般病房',
        role: displayRole,
        field: state.field,
        score: state.score,
        shield: state.shield,
        serial: serial,
        date: `${dateStr} ${timeStr}`,
        timestamp: now.toISOString(),
        passed: state.score >= 80,
        mistakesCount: (state.mistakes || []).length,
        mistakes: state.mistakes || []
      };'''

if old_record in idx_content:
    idx_content = idx_content.replace(old_record, new_record)
    print("1f. record updated with ward")
else:
    print("WARNING: old_record not found")

old_cert_user = '''          <div class="cert-user">${state.nick} (${displayRole})</div>'''
new_cert_user = '''          <div class="cert-user">${state.nick} · ${state.ward} (${displayRole})</div>'''
if old_cert_user in idx_content:
    idx_content = idx_content.replace(old_cert_user, new_cert_user)
    print("1g. cert_user updated")

old_cert_meta = '''          <div class="cert-meta-row">
            <div>認證編號：<strong>${serial}</strong></div>
            <div>認證日期：<strong>${dateStr}</strong></div>
            <div>頒發單位：<strong>臺大醫院感染管制中心</strong></div>
          </div>'''

new_cert_meta = '''          <div class="cert-meta-row">
            <div>所屬病房：<strong>${state.ward}</strong></div>
            <div>認證編號：<strong>${serial}</strong></div>
            <div>認證日期：<strong>${dateStr}</strong></div>
            <div>頒發單位：<strong>臺大醫院感染管制中心</strong></div>
          </div>'''

if old_cert_meta in idx_content:
    idx_content = idx_content.replace(old_cert_meta, new_cert_meta)
    print("1h. cert_meta updated")

with open('感控不踩雷網站/index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("Successfully written 感控不踩雷網站/index.html")

# --- 2. Modify 感控不踩雷網站/admin.html ---
with open('感控不踩雷網站/admin.html', 'r', encoding='utf-8') as f:
    adm_content = f.read()

# 2a. Update thead
old_thead = '''          <thead>
            <tr>
              <th>序號</th>
              <th>同仁姓名</th>
              <th>職別身分</th>
              <th>施測時間</th>
              <th>測驗得分</th>
              <th>合格狀態</th>
              <th>踩雷題數</th>
              <th>認證流水號</th>
              <th>操作</th>
            </tr>
          </thead>'''

new_thead = '''          <thead>
            <tr>
              <th>序號</th>
              <th>同仁姓名</th>
              <th>所屬病房</th>
              <th>職別身分</th>
              <th>施測時間</th>
              <th>測驗得分</th>
              <th>合格狀態</th>
              <th>踩雷題數</th>
              <th>認證流水號</th>
              <th>操作</th>
            </tr>
          </thead>'''

if old_thead in adm_content:
    adm_content = adm_content.replace(old_thead, new_thead)
    print("2a. admin thead updated")

# 2b. Update colspan when 0 records
old_colspan = 'tbody.innerHTML = `<tr><td colspan="9" style="text-align:center; padding:2rem; color:var(--ink-subtle);">查無相符紀錄</td></tr>`;'
new_colspan = 'tbody.innerHTML = `<tr><td colspan="10" style="text-align:center; padding:2rem; color:var(--ink-subtle);">查無相符紀錄</td></tr>`;'
if old_colspan in adm_content:
    adm_content = adm_content.replace(old_colspan, new_colspan)
    print("2b. admin colspan updated")

# 2c. Update search filter to include ward
old_search_logic = '''        // Keyword
        if (search) {
          const matchName = (r.name || '').toLowerCase().includes(search);
          const matchSerial = (r.serial || '').toLowerCase().includes(search);
          if (!matchName && !matchSerial) return false;
        }'''

new_search_logic = '''        // Keyword (支援姓名、病房、流水號搜尋)
        if (search) {
          const matchName = (r.name || '').toLowerCase().includes(search);
          const matchWard = (r.ward || '').toLowerCase().includes(search);
          const matchSerial = (r.serial || '').toLowerCase().includes(search);
          if (!matchName && !matchWard && !matchSerial) return false;
        }'''

if old_search_logic in adm_content:
    adm_content = adm_content.replace(old_search_logic, new_search_logic)
    print("2c. admin search logic updated")

# 2d. Update renderTable rows to add ward column
old_row_gen = '''        return `
          <tr>
            <td><strong>#${idx + 1}</strong></td>
            <td><strong>${r.name || '未填寫'}</strong></td>
            <td><span class="status-badge" style="background:#f1f5f9; color:var(--ink);">${r.role || '護理師'}</span></td>'''

new_row_gen = '''        return `
          <tr>
            <td><strong>#${idx + 1}</strong></td>
            <td><strong>${r.name || '未填寫'}</strong></td>
            <td><span class="status-badge" style="background:#e0f2fe; color:#0369a1; font-weight:700;">${r.ward || '一般病房'}</span></td>
            <td><span class="status-badge" style="background:#f1f5f9; color:var(--ink);">${r.role || '護理師'}</span></td>'''

if old_row_gen in adm_content:
    adm_content = adm_content.replace(old_row_gen, new_row_gen)
    print("2d. admin row generation updated")

# 2e. Update viewDetail title and summary
old_detail_title = '''      title.innerHTML = `<span>👤</span> ${r.name}（${r.role}）作答明細`;'''
new_detail_title = '''      title.innerHTML = `<span>👤</span> ${r.name} · ${r.ward || '一般病房'}（${r.role}）作答明細`;'''
if old_detail_title in adm_content:
    adm_content = adm_content.replace(old_detail_title, new_detail_title)
    print("2e. admin detail title updated")

old_detail_meta = '''          <div>施測時間：${r.date}</div>
          <div>證書流水號：<code>${r.serial}</code></div>'''

new_detail_meta = '''          <div>所屬病房：<strong>${r.ward || '一般病房'}</strong></div>
          <div>施測時間：${r.date}</div>
          <div>證書流水號：<code>${r.serial}</code></div>'''
if old_detail_meta in adm_content:
    adm_content = adm_content.replace(old_detail_meta, new_detail_meta)
    print("2f. admin detail meta updated")

# 2f. Update export CSV
old_csv_head = '''      let csv = '\\uFEFF序號,姓名,職別,測驗得分,合格狀態,施測時間,踩雷題數,證書編號\\n';
      records.forEach((r, idx) => {
        const passed = r.score >= 80 ? '合格' : '待加強';
        const mistakeCount = (r.mistakes && r.mistakes.length) || 0;
        csv += `"${idx + 1}","${r.name || ''}","${r.role || ''}","${r.score}","${passed}","${r.date || ''}","${mistakeCount}","${r.serial || ''}"\\n`;
      });'''

new_csv_head = '''      let csv = '\\uFEFF序號,姓名,所屬病房,職別,測驗得分,合格狀態,施測時間,踩雷題數,證書編號\\n';
      records.forEach((r, idx) => {
        const passed = r.score >= 80 ? '合格' : '待加強';
        const mistakeCount = (r.mistakes && r.mistakes.length) || 0;
        csv += `"${idx + 1}","${r.name || ''}","${r.ward || '一般病房'}","${r.role || ''}","${r.score}","${passed}","${r.date || ''}","${mistakeCount}","${r.serial || ''}"\\n`;
      });'''

if old_csv_head in adm_content:
    adm_content = adm_content.replace(old_csv_head, new_csv_head)
    print("2g. admin csv export updated")

# 2g. Update inject sample data
old_sample_inject = '''      const sampleNames = ['陳淑芬', '林志遠', '張雅涵', '黃國榮', '李佩珊', '王大明', '蔡美玲', '許育誠', '吳俊彥', '鄭雅萍'];
      const sampleRoles = ['護理師', '護理師', '護理師', '醫師', '醫師', '清潔人員', '清潔人員', '其他', '護理師', '護理師'];
      const sampleScores = [100, 80, 100, 80, 60, 80, 60, 100, 80, 100];'''

new_sample_inject = '''      const sampleNames = ['陳淑芬', '林志遠', '張雅涵', '黃國榮', '李佩珊', '王大明', '蔡美玲', '許育誠', '吳俊彥', '鄭雅萍'];
      const sampleWards = ['5B 病房', '7D 病房', '內科加護病房', '8A 病房', '急診醫學部', '6C 病房', '外科加護病房', '9B 病房', '門診部', '5B 病房'];
      const sampleRoles = ['護理師', '護理師', '護理師', '醫師', '醫師', '清潔人員', '清潔人員', '其他', '護理師', '護理師'];
      const sampleScores = [100, 80, 100, 80, 60, 80, 60, 100, 80, 100];'''

if old_sample_inject in adm_content:
    adm_content = adm_content.replace(old_sample_inject, new_sample_inject)
    print("2h. admin sample data arrays updated")

old_sample_record = '''        current.push({
          id: 'REC-' + (Date.now() + i),
          name: name,
          role: sampleRoles[i],
          field: 'ward',
          score: score,'''

new_sample_record = '''        current.push({
          id: 'REC-' + (Date.now() + i),
          name: name,
          ward: sampleWards[i],
          role: sampleRoles[i],
          field: 'ward',
          score: score,'''

if old_sample_record in adm_content:
    adm_content = adm_content.replace(old_sample_record, new_sample_record)
    print("2i. admin sample push updated")

with open('感控不踩雷網站/admin.html', 'w', encoding='utf-8') as f:
    f.write(adm_content)
print("Successfully written 感控不踩雷網站/admin.html")
