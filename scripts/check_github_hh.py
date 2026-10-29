import urllib.request
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://heigilin.github.io/HH/"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        print(f"Status: {resp.status}")
        print(f"Length: {len(content)}")
        print("First 1000 chars:")
        print(content[:1000])
except Exception as e:
    print(f"Error fetching {url}: {e}")
