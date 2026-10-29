import sys
sys.stdout.reconfigure(encoding='utf-8')

# Check with ffprobe if ffmpeg is installed, or inspect mp4 atoms
import subprocess
try:
    res = subprocess.run(['ffprobe', '-version'], capture_output=True, text=True)
    print("ffprobe found!")
    probe = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration,size,bit_rate:stream=codec_name,width,height', '-of', 'default=noprint_wrappers=1', '感控不踩雷網站/assets/videos/wet_handwash.mp4'], capture_output=True, text=True)
    print(probe.stdout)
except Exception as e:
    print(f"ffprobe not available: {e}")
