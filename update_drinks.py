import re, os

WORKDIR = r"D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat"
HTML_PATH = os.path.join(WORKDIR, "index.html")

with open(HTML_PATH, "r", encoding="utf-8") as f:
    content = f.read()

new_imgs = [
    "images/drink_coca_cola.jpg",
    "images/drink_fanta.jpg",
    "images/drink_sprite.jpg",
    "images/drink_beibingyang.jpg",
    "images/drink_watsons.jpg",
    "images/drink_wangzai_milk.jpg",
    "images/drink_mirinda.jpg",
    "images/drink_pepsi.jpg",
    "images/drink_iced_lemon_tea.jpg",
    "images/drink_tongyi_peach.jpg",
    "images/drink_snow_beer.jpg",
    "images/drink_qoo.jpg",
    "images/drink_vita_sparkling_tea.jpg",
    "images/drink_7up.jpg",
    "images/drink_costa_coffee.jpg",
    "images/drink_wanglaoji.jpg",
    "images/drink_tongyi_green_tea.jpg",
    "images/drink_hpp_orange_juice.jpg",
    "images/drink_dongfang_oolong_tea.jpg",
    "images/drink_fanta_orange.jpg",
    "images/drink_dongfang_jasmine_tea.jpg",
    "images/drink_dayao_orange.jpg",
    "images/drink_genki_forest_orange.jpg",
    "images/drink_lamei_black_tea.jpg",
    "images/drink_xiaoxiang_apple_juice.jpg",
    "images/drink_yashixiang_lemon_tea.jpg",
    "images/drink_nfc_orange_juice.jpg",
    "images/drink_beibingyang_orange.jpg",
]

# Find all DISHES entries. Each entry is like: {n:'...',d:'...',c:'...',e:'...',img:'...'}
# We'll split on '},{' boundaries to isolate entries
# First find the DISHES block
dish_start = content.find("let DISHES = [")
dish_end = content.find("];", dish_start)

if dish_start < 0 or dish_end < 0:
    print("ERROR: Could not find DISHES block")
    exit(1)

dishes_block = content[dish_start:dish_end+2]
print(f"DISHES block: {dish_start} to {dish_end}")

# Find all entries with c:'饮料'
# Each entry is on its own line or similar format
# Let's use a regex to find each full entry
entry_pattern = re.compile(r"\{n:'([^']*)',d:'([^']*)',c:'([^']*)',e:'([^']*)',img:'([^']*)'\}")

entries = list(entry_pattern.finditer(content))
print(f"Total DISHES entries found: {len(entries)}")

# Find drink entries
drink_entries = []
for i, m in enumerate(entries):
    cat = m.group(3)
    if cat == '\u996e\u6599':  # 饮料
        drink_entries.append((i, m))

print(f"Drink entries: {len(drink_entries)}")

if len(drink_entries) != len(new_imgs):
    print(f"WARNING: {len(drink_entries)} drink entries vs {len(new_imgs)} new images")

# Replace from end to start (preserve positions)
result = content
n = min(len(drink_entries), len(new_imgs))

for j in range(n - 1, -1, -1):
    idx, m = drink_entries[j]
    old_entry = m.group(0)
    name = m.group(1)
    desc = m.group(2)
    cat = m.group(3)
    emoji = m.group(4)
    new_img = new_imgs[j]
    
    new_entry = "{n:'%s',d:'%s',c:'%s',e:'%s',img:'%s'}" % (name, desc, cat, emoji, new_img)
    
    start = m.start()
    end = m.end()
    result = result[:start] + new_entry + result[end:]
    
    print("[%d] %s -> %s" % (j, name, new_img))

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(result)

print("\nindex.html updated!")

# === VERIFICATION ===
with open(HTML_PATH, "r", encoding="utf-8") as f:
    verify = f.read()

all_ok = True
for img in new_imgs:
    fpath = os.path.join(WORKDIR, img)
    file_exists = os.path.exists(fpath)
    html_ref = img in verify
    if not file_exists:
        print("FILE MISSING: %s" % img)
        all_ok = False
    if not html_ref:
        print("HTML MISSING: %s" % img)
        all_ok = False

# Check no old references remain
old = len(re.findall(r"fruitdrink_", verify))
print("Old fruitdrink_ refs remaining: %d" % old)

if all_ok and old == 0:
    print("\n=== ALL 28 DRINK IMAGES VERIFIED: Files exist + HTML references correct ===")
else:
    print("\n=== ISSUES FOUND ===")
