import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

html_files = [
    '感控不踩雷網站/index.html',
    '感控不踩雷網站/learning.html',
    '感控不踩雷網站/presentation.html',
    '感控不踩雷網站/admin.html',
    './index.html',
    './learning.html',
    './presentation.html',
    './admin.html'
]

errors = []
successes = []

# 1. Check constraints on all files
for file_path in html_files:
    if not os.path.exists(file_path):
        errors.append(f"File missing: {file_path}")
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Disallowed terms
    for term in ['Y:\\', 'E:\\', 'IFC_V', '50300', '免密碼', '致命', '權威', '感管護理長', 'ANN', '可愛']:
        count = content.count(term)
        if count > 0:
            errors.append(f"{file_path} contains forbidden term '{term}' ({count} times)")

# 2. Check asset files existence
asset_files = [
    '感控不踩雷網站/assets/videos/handwashing_training_web.mp4',
    'assets/videos/handwashing_training_web.mp4',
    '感控不踩雷網站/assets/images/hand_hygiene/01_hand_hygiene_cover.png',
    '感控不踩雷網站/assets/images/hand_hygiene/02_step1_wet_soap_up.png',
    '感控不踩雷網站/assets/images/hand_hygiene/03_step2_scrub_20_seconds.png',
    '感控不踩雷網站/assets/images/hand_hygiene/04_step3_rinse_thoroughly.png',
    '感控不踩雷網站/assets/images/hand_hygiene/05_step4_dry_gently.png',
    '感控不踩雷網站/assets/images/hand_hygiene/HH (1).png',
    '感控不踩雷網站/assets/images/hand_hygiene/HH (5).png'
]

for af in asset_files:
    if os.path.exists(af) and os.path.getsize(af) > 0:
        successes.append(f"Asset file exists: {af} ({os.path.getsize(af)} bytes)")
    else:
        errors.append(f"Asset file missing or empty: {af}")

# 3. Check presentation.html specifics
for path in ['感控不踩雷網站/presentation.html', './presentation.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    p_checks = [
        ('https://heigilin.github.io/HH/handwashing_training_web.mp4', 'presentation video player src (cdn)'),
        ('assets/videos/handwashing_training_web.mp4', 'presentation video player src (local)'),
        ('02_step1_wet_soap_up.png', 'presentation step 1 image'),
        ('03_step2_scrub_20_seconds.png', 'presentation step 2 image'),
        ('04_step3_rinse_thoroughly.png', 'presentation step 3 image'),
        ('05_step4_dry_gently.png', 'presentation step 4 image'),
        ('HH (1).png', 'presentation HH 5 moments image 1'),
        ('HH (5).png', 'presentation HH 5 moments image 5'),
        ('openSlide(4)', 'slide 4 quick navigation')
    ]

    for needle, label in p_checks:
        if needle in content:
            successes.append(f"[{path}] PASS: {label}")
        else:
            errors.append(f"[{path}] FAIL: {label} not found")

# 4. Check index.html specifics
for path in ['感控不踩雷網站/index.html', './index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    checks = [
        ('id="playerWard"', 'playerWard in sidebar input'),
        ('id="stepRoleWard"', 'stepRoleWard in step 2 input'),
        ("ward: localStorage.getItem('ntuh_guardian_ward')", 'state.ward storage reading'),
        ("localStorage.setItem('ntuh_guardian_ward', state.ward)", 'state.ward storage saving'),
        ("${state.nick} · ${state.ward} (${displayRole})", 'HUD / Cert player format'),
        ("ward: state.ward || '一般病房'", 'record ward field saving'),
        ("所屬病房：<strong>${state.ward}</strong>", 'Certificate ward metadata display'),
        ("瀰漫性帶狀疱疹 (>=3個神經節)", 'Disseminated zoster updated wording'),
        ("0.06% (600 ppm，約 1:100 稀釋)", 'Bleach 0.06% dilution ratio'),
        ("0.1% (1,000 ppm，約 1:50 稀釋)", 'Bleach 0.1% dilution ratio'),
        ("手套 ＋ 防水隔離衣", 'Contact precautions PPE wording'),
        ("病房護理長 淑芬", 'Ward Nurse Head Shufen title'),
        ("有效移除暫時性菌叢", 'Microbial flora wording instead of sterilization'),
        ('https://heigilin.github.io/HH/handwashing_training_web.mp4', 'index video player src (cdn)'),
        ('openHhModal', 'openHhModal function in index'),
        ('assets/videos/handwashing_training_web.mp4', 'index video player src (local)'),
        ('02_step1_wet_soap_up.png', 'index step 1 image')
    ]

    for needle, label in checks:
        if needle in content:
            successes.append(f"[{path}] PASS: {label}")
        else:
            errors.append(f"[{path}] FAIL: {label} not found")

# 5. Check admin.html specifics
for path in ['感控不踩雷網站/admin.html', './admin.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    adm_checks = [
        ('<th>所屬病房</th>', 'admin table header ward column'),
        ('${r.ward || \'一般病房\'}', 'admin table cell ward rendering'),
        ('const matchWard = (r.ward || \'\').toLowerCase().includes(search);', 'admin search filter by ward'),
        ('序號,姓名,所屬病房,職別,測驗得分', 'admin CSV header with ward'),
        ('"${r.ward || \'一般病房\'}"', 'admin CSV data row with ward'),
        ('所屬病房：<strong>${r.ward || \'一般病房\'}</strong>', 'admin detail modal ward display'),
        ('sampleWards', 'admin sample test data wards array')
    ]

    for needle, label in adm_checks:
        if needle in content:
            successes.append(f"[{path}] PASS: {label}")
        else:
            errors.append(f"[{path}] FAIL: {label} not found")

print(f"=== SUMMARY ===")
print(f"Total passes: {len(successes)}")
print(f"Total errors: {len(errors)}")

if errors:
    print("\n--- ERRORS FOUND ---")
    for err in errors:
        print("❌", err)
    sys.exit(1)
else:
    print("\n✅ ALL VERIFICATION CHECKS PASSED PERFECTLY!")
