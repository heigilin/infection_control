# -*- coding: utf-8 -*-
with open('.gitignore', 'r', encoding='utf-8') as f:
    text = f.read()

old_ignore = '''# Large video files (>100MB, hosted on https://heigilin.github.io/HH/)
assets/videos/*.mp4
感控不踩雷網站/assets/videos/*.mp4'''

new_ignore = '''# Large 339MB raw video files (hosted externally)
assets/videos/溼洗手.mp4
assets/videos/wet_handwash.mp4
感控不踩雷網站/assets/videos/溼洗手.mp4
感控不踩雷網站/assets/videos/wet_handwash.mp4'''

text = text.replace(old_ignore, new_ignore)
with open('.gitignore', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(text)

print("Updated .gitignore.")
