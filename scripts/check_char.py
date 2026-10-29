import sys
sys.stdout.reconfigure(encoding='utf-8')

for code in [0x6EBC, 0x6FD5, 0x6E7F]:
    print(f"U+{code:04X}: {chr(code)}")
