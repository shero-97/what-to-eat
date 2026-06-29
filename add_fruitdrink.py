import json, re, os

with open('fruitdrink_dishes.json', 'r', encoding='utf-8') as f:
    new_dishes = json.load(f)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build entries - use ASCII-safe filenames 
entries = []
for d in new_dishes:
    entries.append(f"  {{n:'{d['n']}',d:'{d['d']}',c:'{d['c']}',e:'{d['e']}',img:'{d['img']}'}},")

# Insert before DISHES closing ];
# Find the last dish before ];
pattern = r"(秋葵炒蛋',d:'滑嫩清爽，营养丰富',c:'荤素结合',e:'🥚',img:'images/new_menu_09_4.jpg'},\s*\n)(\s*\];)"
replacement = r"\1" + '\n'.join(entries) + r"\n\2"

# Try fallback if not found
if '秋葵炒蛋' not in html:
    # Use rfind approach but more carefully
    dishes_end = html.find('let DISHES')
    closing = html.find('];', dishes_end + 300)
    if closing > 0:
        html = html[:closing] + '\n' + '\n'.join(entries) + '\n' + html[closing:]

html = re.sub(pattern, replacement, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Verify
total = html.count("img:'images/")
print(f'Added {len(new_dishes)} fruit+drink dishes')
print(f'Total img references: {total}')

# Category breakdown
cats = {}
for d in new_dishes:
    cats[d['c']] = cats.get(d['c'], 0) + 1
for c, n in sorted(cats.items()):
    print(f'  {c}: {n}')

# Verify images exist
missing = 0
for d in new_dishes:
    p = d['img'].replace('images/', 'images/')
    fp = os.path.join('images', d['img'].split('/')[-1])
    if not os.path.exists(fp):
        missing += 1
print(f'Missing images: {missing}')
