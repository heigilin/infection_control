import struct
import shutil
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def faststart(in_path, out_path):
    with open(in_path, 'rb') as f:
        # Read atoms at root
        atoms = []
        while True:
            pos = f.tell()
            header = f.read(8)
            if len(header) < 8:
                break
            size, atom_type = struct.unpack('>I4s', header)
            atom_type = atom_type.decode('ascii', errors='ignore')
            if size == 1:
                size = struct.unpack('>Q', f.read(8))[0]
            elif size == 0:
                f.seek(0, 2)
                size = f.tell() - pos
            atoms.append((atom_type, pos, size))
            f.seek(pos + size)

    print("Root atoms:", [(a[0], a[2]) for a in atoms])
    
    moov_info = next((a for a in atoms if a[0] == 'moov'), None)
    mdat_info = next((a for a in atoms if a[0] == 'mdat'), None)
    
    if not moov_info or not mdat_info:
        print("Error: moov or mdat missing")
        return False
        
    moov_pos, moov_size = moov_info[1], moov_info[2]
    mdat_pos, mdat_size = mdat_info[1], mdat_info[2]
    
    if moov_pos < mdat_pos:
        print("moov is already before mdat!")
        return True

    print(f"Moving moov (size {moov_size}) before mdat (pos {mdat_pos})...")
    
    with open(in_path, 'rb') as f:
        f.seek(moov_pos)
        moov_data = bytearray(f.read(moov_size))

    # Adjust stco/co64 in moov_data
    # In moov_data, find 'stco' and 'co64'
    offset_shift = moov_size
    
    idx = 0
    while idx < len(moov_data) - 8:
        if moov_data[idx+4:idx+8] == b'stco':
            stco_size = struct.unpack('>I', moov_data[idx:idx+4])[0]
            entry_count = struct.unpack('>I', moov_data[idx+12:idx+16])[0]
            print(f"Found stco at offset {idx}, entries: {entry_count}")
            entry_offset = idx + 16
            for _ in range(entry_count):
                curr_off = struct.unpack('>I', moov_data[entry_offset:entry_offset+4])[0]
                new_off = curr_off + offset_shift
                struct.pack_into('>I', moov_data, entry_offset, new_off)
                entry_offset += 4
            idx += stco_size
        elif moov_data[idx+4:idx+8] == b'co64':
            co64_size = struct.unpack('>I', moov_data[idx:idx+4])[0]
            entry_count = struct.unpack('>I', moov_data[idx+12:idx+16])[0]
            print(f"Found co64 at offset {idx}, entries: {entry_count}")
            entry_offset = idx + 16
            for _ in range(entry_count):
                curr_off = struct.unpack('>Q', moov_data[entry_offset:entry_offset+8])[0]
                new_off = curr_off + offset_shift
                struct.pack_into('>Q', moov_data, entry_offset, new_off)
                entry_offset += 8
            idx += co64_size
        else:
            idx += 1

    # Write output: ftyp (and any atom before mdat), then moov, then mdat
    with open(in_path, 'rb') as fin, open(out_path, 'wb') as fout:
        for a in atoms:
            if a[0] not in ('moov', 'mdat'):
                fin.seek(a[1])
                fout.write(fin.read(a[2]))
        # Write modified moov
        fout.write(moov_data)
        # Write mdat
        fin.seek(mdat_pos)
        # Stream mdat in chunks of 4MB
        remaining = mdat_size
        chunk_size = 4 * 1024 * 1024
        while remaining > 0:
            to_read = min(remaining, chunk_size)
            buf = fin.read(to_read)
            if not buf:
                break
            fout.write(buf)
            remaining -= len(buf)

    print(f"Successfully generated {out_path} with size {os.path.getsize(out_path)}")
    return True

faststart('感控不踩雷網站/assets/videos/溼洗手.mp4', '感控不踩雷網站/assets/videos/溼洗手_faststart.mp4')
