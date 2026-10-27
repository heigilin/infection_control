import sys
import shutil
import os

sys.stdout.reconfigure(encoding='utf-8')

src_dir = '感控不踩雷網站'
dest_dir = '.'

# 1. Sync index.html to learning.html inside 感控不踩雷網站
shutil.copy2(os.path.join(src_dir, 'index.html'), os.path.join(src_dir, 'learning.html'))
print(f"Copied {src_dir}/index.html -> {src_dir}/learning.html")

# 2. Copy all html files from 感控不踩雷網站 to workspace root
for filename in ['index.html', 'learning.html', 'presentation.html', 'admin.html']:
    src_file = os.path.join(src_dir, filename)
    dest_file = os.path.join(dest_dir, filename)
    if os.path.exists(src_file):
        shutil.copy2(src_file, dest_file)
        print(f"Copied {src_file} -> {dest_file} ({os.path.getsize(dest_file)} bytes)")
