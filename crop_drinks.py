"""
Crop beverage images from grid layouts and save with English names.
Image 1: 4x4 grid (16 drinks), 1080x1309
Image 2: 3x4 grid (12 drinks), 1080x1228
"""
import os
import json
from PIL import Image
import numpy as np

WORKDIR = r"D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat"
TEMPDIR = os.path.join(WORKDIR, "temp_new")
IMGDIR = os.path.join(WORKDIR, "images")
os.makedirs(IMGDIR, exist_ok=True)

# Find the beverage images by hex pattern
def find_file(hex_pattern):
    for f in os.listdir(TEMPDIR):
        b = f.encode('utf-8', errors='surrogateescape')
        if b.hex() == hex_pattern:
            return os.path.join(TEMPDIR, f)
    return None

# 饮料_01.jpg = e9a5aee696995f30312e6a7067
# 饮料_02.jpg = e9a5aee696995f30322e6a7067
img1_path = find_file("e9a5aee696995f30312e6a7067")
img2_path = find_file("e9a5aee696995f30322e6a7067")

print(f"Image 1: {img1_path}")
print(f"Image 2: {img2_path}")

# Drink names - Image 1 (4x4 grid, 16 drinks)
drinks_img1 = [
    "可口可乐", "芬达", "雪碧", "北冰洋",
    "Watson's", "旺仔牛奶", "美年达", "百事可乐",
    "凍檸茶", "统一蜜桃多", "雪花啤酒", "酷兒",
    "维他气泡茶", "七喜", "COSTA COFFEE", "王老吉"
]

# Drink names - Image 2 (3x4 grid, 12 drinks)
drinks_img2 = [
    "统一春拂绿茶", "HPP沃柑汁", "东方树叶乌龙茶", "芬达橙味汽水",
    "东方树叶茉莉花茶", "大窑橙诺", "元气森林橙味气泡水", "腊梅红茶",
    "小象NFC苹果汁", "鸭屎香双萃柠檬茶", "NFC橙汁", "北冰洋橙味汽水"
]

# English filename mapping
def to_english_name(cn_name):
    """Convert Chinese drink name to English filename"""
    mapping = {
        "可口可乐": "coca_cola",
        "芬达": "fanta",
        "雪碧": "sprite",
        "北冰洋": "beibingyang",
        "Watson's": "watsons",
        "旺仔牛奶": "wangzai_milk",
        "美年达": "mirinda",
        "百事可乐": "pepsi",
        "凍檸茶": "iced_lemon_tea",
        "统一蜜桃多": "tongyi_peach",
        "雪花啤酒": "snow_beer",
        "酷兒": "qoo",
        "维他气泡茶": "vita_sparkling_tea",
        "七喜": "7up",
        "COSTA COFFEE": "costa_coffee",
        "王老吉": "wanglaoji",
        "统一春拂绿茶": "tongyi_green_tea",
        "HPP沃柑汁": "hpp_orange_juice",
        "东方树叶乌龙茶": "dongfang_oolong_tea",
        "芬达橙味汽水": "fanta_orange",
        "东方树叶茉莉花茶": "dongfang_jasmine_tea",
        "大窑橙诺": "dayao_orange",
        "元气森林橙味气泡水": "genki_forest_orange",
        "腊梅红茶": "lamei_black_tea",
        "小象NFC苹果汁": "xiaoxiang_apple_juice",
        "鸭屎香双萃柠檬茶": "yashixiang_lemon_tea",
        "NFC橙汁": "nfc_orange_juice",
        "北冰洋橙味汽水": "beibingyang_orange",
    }
    return mapping.get(cn_name, cn_name.replace(" ", "_").lower())


def detect_grid_lines(img, rows, cols):
    """
    Detect grid lines by analyzing brightness transitions.
    Returns (col_positions, row_positions) - lists of (start, end) tuples for each cell.
    """
    arr = np.array(img.convert('L'))  # grayscale
    h, w = arr.shape
    
    # For vertical grid lines: look at column brightness profiles
    # Sum brightness along rows for each column
    col_profile = arr.mean(axis=0)  # avg brightness per column
    
    # For horizontal grid lines: look at row brightness profiles
    row_profile = arr.mean(axis=1)  # avg brightness per row
    
    # Grid lines should be brighter (lighter) than content areas
    # Find peaks in the profile that correspond to grid lines
    
    # Smooth the profiles slightly
    def smooth(profile, window=3):
        kernel = np.ones(window) / window
        return np.convolve(profile, kernel, mode='same')
    
    col_smooth = smooth(col_profile, 5)
    row_smooth = smooth(row_profile, 5)
    
    # Find columns where brightness is above threshold (grid lines)
    col_threshold = np.percentile(col_smooth, 60)
    row_threshold = np.percentile(row_smooth, 60)
    
    # Find grid line regions (contiguous bright columns/rows)
    def find_bright_regions(profile, threshold, min_gap=10):
        """Find regions where profile > threshold, merge close ones"""
        above = profile > threshold
        regions = []
        start = None
        for i, val in enumerate(above):
            if val and start is None:
                start = i
            elif not val and start is not None:
                if i - start >= 2:  # at least 2px wide
                    regions.append((start, i))
                start = None
        if start is not None:
            if len(above) - start >= 2:
                regions.append((start, len(above)))
        
        # Merge close regions
        merged = []
        for r in regions:
            if not merged:
                merged.append(r)
            elif r[0] - merged[-1][1] < min_gap:
                merged[-1] = (merged[-1][0], r[1])
            else:
                merged.append(r)
        return merged
    
    col_lines = find_bright_regions(col_smooth, col_threshold)
    row_lines = find_bright_regions(row_smooth, row_threshold)
    
    print(f"  Detected {len(col_lines)} vertical grid regions, {len(row_lines)} horizontal grid regions")
    
    # Expected: (cols-1) interior vertical lines, (rows-1) interior horizontal lines
    # But we might also detect image borders as bright regions
    # Filter: keep only interior lines that divide the grid
    
    # If we have more lines than expected, keep the strongest ones
    # The grid lines should be roughly evenly spaced
    
    # For a 4x4 grid, we expect 3 vertical interior lines and 3 horizontal interior lines
    # The lines should divide the image into roughly equal sections
    
    # Simple approach: just divide evenly since grids are uniform
    # But let's try to detect the actual positions
    
    # For each set of lines, find the middle of each bright region
    col_centers = [(s+e)//2 for s, e in col_lines]
    row_centers = [(s+e)//2 for s, e in row_lines]
    
    # Expected spacing: w/cols, h/rows
    expected_col_spacing = w / cols
    expected_row_spacing = h / rows
    
    # Filter to find lines that are roughly at expected positions
    def filter_to_expected(centers, total_size, count, expected_spacing):
        """Select centers that best match expected grid positions"""
        expected = [expected_spacing * (i + 1) for i in range(count - 1)]
        # For each expected position, find closest detected center within tolerance
        tolerance = expected_spacing * 0.3
        selected = []
        for exp in expected:
            best = min(centers, key=lambda c: abs(c - exp), default=None)
            if best is not None and abs(best - exp) < tolerance:
                selected.append(best)
            else:
                selected.append(int(exp))  # fall back to expected position
        return selected
    
    selected_cols = filter_to_expected(col_centers, w, cols, expected_col_spacing)
    selected_rows = filter_to_expected(row_centers, h, rows, expected_row_spacing)
    
    print(f"  Selected col dividers: {selected_cols}")
    print(f"  Selected row dividers: {selected_rows}")
    
    # Build cell boundaries: (x1, y1, x2, y2) for each cell
    col_boundaries = [0] + selected_cols + [w]
    row_boundaries = [0] + selected_rows + [h]
    
    cells = []
    for r in range(rows):
        for c in range(cols):
            x1 = col_boundaries[c]
            y1 = row_boundaries[r]
            x2 = col_boundaries[c+1]
            y2 = row_boundaries[r+1]
            cells.append((x1, y1, x2, y2))
    
    return cells


def crop_and_save(img_path, drinks, rows, cols, prefix):
    """Crop grid image into individual drinks and save them."""
    img = Image.open(img_path)
    print(f"\nProcessing: {os.path.basename(img_path)}")
    print(f"  Size: {img.size}, Grid: {rows}x{cols}")
    
    cells = detect_grid_lines(img, rows, cols)
    print(f"  Got {len(cells)} cells")
    
    results = []
    for i, (name, (x1, y1, x2, y2)) in enumerate(zip(drinks, cells)):
        # Add small margin inside to avoid grid lines
        margin = 3
        crop_box = (x1 + margin, y1 + margin, x2 - margin, y2 - margin)
        cropped = img.crop(crop_box)
        
        # Resize to 300px wide, maintaining aspect ratio
        w, h = cropped.size
        new_w = 300
        new_h = int(h * 300 / w)
        resized = cropped.resize((new_w, new_h), Image.LANCZOS)
        
        # Generate filename
        eng = to_english_name(name)
        filename = f"drink_{eng}.jpg"
        filepath = os.path.join(IMGDIR, filename)
        resized.save(filepath, "JPEG", quality=90)
        
        print(f"  [{i}] {name} -> {filename} ({resized.size})")
        results.append((name, filename))
    
    return results


# Process both images
print("="*60)
print("CROPPING BEVERAGE IMAGES")
print("="*60)

results1 = crop_and_save(img1_path, drinks_img1, 4, 4, "01")
results2 = crop_and_save(img2_path, drinks_img2, 3, 4, "02")

# Combine all results
all_results = results1 + results2

# Save mapping for reference
mapping = {name: f"images/drink_{to_english_name(name)}.jpg" for name, _ in all_results}
with open(os.path.join(WORKDIR, "drink_mapping.json"), "w", encoding="utf-8") as f:
    json.dump(mapping, f, ensure_ascii=False, indent=2)

print(f"\n{'='*60}")
print(f"Done! {len(all_results)} images saved to {IMGDIR}")
print(f"Mapping saved to drink_mapping.json")

# Verify all files exist
print(f"\n{'='*60}")
print("VERIFYING ALL IMAGES")
print("="*60)
missing = []
for name, img_path in mapping.items():
    full = os.path.join(WORKDIR, img_path)
    if os.path.exists(full):
        sz = os.path.getsize(full)
        print(f"  OK: {img_path} ({sz} bytes)")
    else:
        print(f"  MISSING: {img_path}")
        missing.append(img_path)

if missing:
    print(f"\nWARNING: {len(missing)} files missing!")
else:
    print(f"\nAll {len(mapping)} images verified!")
