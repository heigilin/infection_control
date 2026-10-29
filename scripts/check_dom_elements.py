with open('感控不踩雷網站/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

elements = [
    'btnOpenDex',
    'btnHudDex',
    'btnHudExit',
    'btnCloseDialog',
    'dialogOverlay',
    'btnAudioToggle',
    'btnHudAudio',
    'btnCloseNpcDialog',
    'btnNpcDialogOk',
    'btnQuestGo',
    'btnWardCompass',
    'btnWardDex',
    'btnWardSound',
    'btnWardExit',
    'btnChangeScene',
    'btnStartAdventure',
    'btnCloseArenaDuel',
    'btnNextDuel'
]

for el in elements:
    found = f'id="{el}"' in text
    print(f"{el}: {'FOUND' if found else 'MISSING'}")
