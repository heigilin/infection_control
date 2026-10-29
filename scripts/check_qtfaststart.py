import sys
sys.stdout.reconfigure(encoding='utf-8')

try:
    import qtfaststart
    print("qtfaststart installed!")
except ImportError:
    print("qtfaststart not installed")
