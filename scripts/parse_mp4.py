import sys
import struct
sys.stdout.reconfigure(encoding='utf-8')

def parse_mp4(filepath):
    with open(filepath, 'rb') as f:
        while True:
            header = f.read(8)
            if len(header) < 8:
                break
            size, atom_type = struct.unpack('>I4s', header)
            atom_type = atom_type.decode('ascii', errors='ignore')
            print(f"Atom: {atom_type}, size: {size}")
            if size == 1:
                # 64-bit size
                size = struct.unpack('>Q', f.read(8))[0] - 16
                f.seek(size, 1)
            elif size == 0:
                break
            else:
                if atom_type in ['moov', 'trak', 'mdia', 'minf', 'stbl']:
                    pass # descend
                else:
                    f.seek(size - 8, 1)

parse_mp4('感控不踩雷網站/assets/videos/溼洗手.mp4')
