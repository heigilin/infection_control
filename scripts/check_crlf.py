with open('感控不踩雷網站/presentation.html', 'rb') as f:
    sample = f.read(2000)
    print("CRLF" if b'\r\n' in sample else "LF")
