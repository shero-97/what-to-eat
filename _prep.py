import os
import shutil

src_dir = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\hotpot_new_212745'
tmp_dir = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\temp_hotpot'

os.makedirs(tmp_dir, exist_ok=True)

files = sorted(os.listdir(src_dir))
for i, f in enumerate(files):
    src = os.path.join(src_dir, f)
    # Copy to temp with simple name
    dst = os.path.join(tmp_dir, f'hotpot_{i:02d}.jpg')
    shutil.copy2(src, dst)
    print(f'{i:02d} -> hotpot_{i:02d}.jpg ({os.path.getsize(src)} bytes)')
