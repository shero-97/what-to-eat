import os, shutil

imgdir = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\images'

# Staple dish names -> safe ASCII filenames
staple_map = {
    'staple_白米饭.jpg': 'staple_rice.jpg',
    'staple_蛋炒饭.jpg': 'staple_fried_rice.jpg',
    'staple_炒河粉.jpg': 'staple_rice_noodle.jpg',
    'staple_阳春面.jpg': 'staple_noodle.jpg',
    'staple_小米粥.jpg': 'staple_porridge.jpg',
    'staple_小笼包.jpg': 'staple_dumpling.jpg',
    'staple_水饺.jpg': 'staple_boiled_dumpling.jpg',
    'staple_煮玉米.jpg': 'staple_corn.jpg',
    'staple_葱油饼.jpg': 'staple_pancake.jpg',
    'staple_烤红薯.jpg': 'staple_sweet_potato.jpg',
}

# Rename files
for old, new in staple_map.items():
    old_path = os.path.join(imgdir, old)
    new_path = os.path.join(imgdir, new)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f'Renamed: {old} -> {new}')
    else:
        # Try to find by matching first 10 chars
        for f in os.listdir(imgdir):
            if f.startswith('staple_') and f.endswith('.jpg') and old[:12] in f:
                os.rename(os.path.join(imgdir,f), new_path)
                print(f'Renamed (fuzzy): {f} -> {new}')
                break
        else:
            print(f'NOT FOUND: {old}')

# Verify
print('\nFinal staple files:')
for f in sorted(os.listdir(imgdir)):
    if f.startswith('staple_'):
        print(f'  {f}')
