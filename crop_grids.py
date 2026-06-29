import os, re
from PIL import Image

src_dir = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\img_155600'
out_dir = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\images'

# Clean old crops
for f in os.listdir(out_dir):
    if f.startswith('grid_'):
        os.remove(os.path.join(out_dir, f))

# Sort by the number after the first underscore (_2, _3, ..., _17)
def extract_num(fname):
    parts = fname.split('_')
    for p in parts:
        if p.isdigit():
            return int(p)
    return 0

files = sorted(os.listdir(src_dir), key=extract_num)
# files: _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13, _14, _15, _16, _17

for i, fname in enumerate(files):
    if fname.startswith('grid_'): continue
    img = Image.open(os.path.join(src_dir, fname))
    w, h = img.size
    hw, hh = w // 2, h // 2
    
    positions = [(0,0,hw,hh), (hw,0,w,hh), (0,hh,hw,h), (hw,hh,w,h)]
    
    for pi, box in enumerate(positions):
        crop = img.crop(box)
        w2, h2 = crop.size
        ratio = 300 / w2
        crop = crop.resize((300, int(h2*ratio)), Image.LANCZOS)
        
        out_name = f'grid_{i:02d}_{pi+1}.jpg'
        crop.save(os.path.join(out_dir, out_name), 'JPEG', quality=85)
        print(f'{out_name}  ({crop.size})')

print(f'\nDone! {i+1} grids -> 64 images')
print('Actual file mapping:')
for i, f in enumerate(files):
    parts = f.split('_')
    num = [p for p in parts if p.isdigit()][0]
    print(f'  grid_{i:02d}  <-  original file _#{num}')
