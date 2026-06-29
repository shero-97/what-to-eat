import os, re
from PIL import Image

temp = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\temp_new'
outdir = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\images'

# Process 菜单 grid images (9 grids x 4 = 36 potential dishes)
for fname in sorted(os.listdir(temp)):
    if not fname.startswith('菜单_') and not fname.startswith('水果_'): 
        continue
    
    src = os.path.join(temp, fname)
    img = Image.open(src)
    w, h = img.size
    print(f'{fname}: {w}x{h}')
    
    if fname.startswith('菜单_'):
        # Grid - crop 2x2
        grid_num = int(re.findall(r'(\d+)', fname)[0])
        hw, hh = w // 2, h // 2
        positions = [(0,0,hw,hh), (hw,0,w,hh), (0,hh,hw,h), (hw,hh,w,h)]
        for pi, box in enumerate(positions):
            crop = img.crop(box)
            ratio = 300 / crop.size[0]
            crop = crop.resize((300, int(crop.size[1]*ratio)), Image.LANCZOS)
            out = os.path.join(outdir, f'new_menu_{grid_num:02d}_{pi+1}.jpg')
            crop.save(out, 'JPEG', quality=85)
            print(f'  -> new_menu_{grid_num:02d}_{pi+1}.jpg ({crop.size})')
    
    elif fname.startswith('水果_'):
        # Fruit composite - might need different handling
        # For now, save as single image with fruit_ prefix
        ratio = 300 / w
        crop = img.resize((300, int(h*ratio)), Image.LANCZOS)
        out = os.path.join(outdir, f'fruit_raw_{fname}')
        crop.save(out, 'JPEG', quality=85)
        print(f'  -> fruit_raw_{fname} ({crop.size})')

print('\nDone!')
