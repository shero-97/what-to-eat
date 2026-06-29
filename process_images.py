#!/usr/bin/env python3
"""Step 1-2 v3: New output dir, internal tracking."""
import os, re, shutil, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from PIL import Image

BASE = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat'
SRC = os.path.join(BASE, 'img_new_171541')
TEMP = os.path.join(BASE, 'temp2')
IMAGES = os.path.join(BASE, 'images2')

os.makedirs(TEMP, exist_ok=True)
os.makedirs(IMAGES, exist_ok=True)

SINGLE_FOLDERS = {'火锅', '饮料'}

def extract_number(filename):
    nums = re.findall(r'(\d+)', filename)
    if nums:
        return int(nums[-1])
    return 0

def cut_grid(img_path, out_dir, basename):
    with Image.open(img_path) as img:
        w, h = img.size
        half_w, half_h = w // 2, h // 2
        pieces = [
            (0, 0, half_w, half_h),
            (half_w, 0, w, half_h),
            (0, half_h, half_w, h),
            (half_w, half_h, w, h),
        ]
        results = []
        for i, (left, upper, right, lower) in enumerate(pieces):
            piece = img.crop((left, upper, right, lower))
            out_name = f"{basename}_{i+1}.jpg"
            out_path = os.path.join(out_dir, out_name)
            piece.save(out_path, 'JPEG', quality=92)
            results.append(out_name)
        return results

def resize_single(img_path, out_dir, basename, size=(300, 400)):
    with Image.open(img_path) as img:
        img_resized = img.resize(size, Image.LANCZOS)
        out_name = f"{basename}.jpg"
        out_path = os.path.join(out_dir, out_name)
        img_resized.save(out_path, 'JPEG', quality=92)
        return [out_name]

print("=" * 60)
print("STEP 1: Copy and rename to temp2/")
print("=" * 60)

folder_data = {}
for folder_name in sorted(os.listdir(SRC)):
    folder_path = os.path.join(SRC, folder_name)
    if not os.path.isdir(folder_path):
        continue
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    files.sort(key=extract_number)
    is_single = folder_name in SINGLE_FOLDERS
    print(f"\n[{folder_name}] {len(files)} files ({'SINGLE' if is_single else 'GRID'}):")
    renamed = []
    for idx, f in enumerate(files, 1):
        src_path = os.path.join(folder_path, f)
        ext = os.path.splitext(f)[1]
        new_name = f"{folder_name}_{idx:03d}{ext}"
        dst_path = os.path.join(TEMP, new_name)
        shutil.copy2(src_path, dst_path)
        renamed.append((new_name, is_single))
        print(f"  {idx:02d}: {new_name}")
    folder_data[folder_name] = renamed

print("\n" + "=" * 60)
print("STEP 2: Process and save to images2/")
print("=" * 60)

folder_output = {}
total_in, total_out = 0, 0
for folder_name, renamed in folder_data.items():
    folder_out = 0
    print(f"\n[{folder_name}]")
    for new_name, is_single in renamed:
        base_name = os.path.splitext(new_name)[0]
        temp_path = os.path.join(TEMP, new_name)
        total_in += 1
        with Image.open(temp_path) as img:
            w, h = img.size
        if is_single:
            results = resize_single(temp_path, IMAGES, base_name)
            total_out += len(results)
            folder_out += len(results)
            print(f"  {new_name} ({w}x{h}) -> SINGLE 300x400: {results}")
        else:
            results = cut_grid(temp_path, IMAGES, base_name)
            total_out += len(results)
            folder_out += len(results)
            print(f"  {new_name} ({w}x{h}) -> GRID 4 pieces")
    folder_output[folder_name] = folder_out

print(f"\n{'=' * 60}")
print(f"FINAL SUMMARY")
print(f"{'=' * 60}")
print(f"  Total input:  {total_in}")
print(f"  Total output: {total_out}")
print(f"  Temp dir:     {TEMP}")
print(f"  Output dir:   {IMAGES}")
print()
for folder_name, renamed in folder_data.items():
    print(f"  {folder_name}: {len(renamed)} input -> {folder_output[folder_name]} output")
print(f"{'=' * 60}")
