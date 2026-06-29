import re, os

WORKDIR = r"D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat"

with open(os.path.join(WORKDIR, "index.html"), "r", encoding="utf-8") as f:
    content = f.read()

# Find all drink entries
pattern = re.compile(r"\{n:'([^']*)',d:'([^']*)',c:'([^']*)',e:'([^']*)',img:'([^']*)'\}")
count = 0
for m in pattern.finditer(content):
    if m.group(3) == '\u996e\u6599':
        count += 1
        print("%2d. %-20s | %s | %s" % (count, m.group(1), m.group(3), m.group(5)))

print()
print("Total drink entries:", count)

# Also verify all image files
imgs_dir = os.path.join(WORKDIR, "images")
drink_files = [f for f in os.listdir(imgs_dir) if f.startswith("drink_")]
print("Drink image files:", len(drink_files))
for f in sorted(drink_files):
    sz = os.path.getsize(os.path.join(imgs_dir, f))
    print("  %s (%d bytes)" % (f, sz))
