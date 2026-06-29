import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    ("images/staple_白米饭.jpg", "images/staple_rice.jpg"),
    ("images/staple_蛋炒饭.jpg", "images/staple_fried_rice.jpg"),
    ("images/staple_炒河粉.jpg", "images/staple_rice_noodle.jpg"),
    ("images/staple_阳春面.jpg", "images/staple_noodle.jpg"),
    ("images/staple_小米粥.jpg", "images/staple_porridge.jpg"),
    ("images/staple_小笼包.jpg", "images/staple_dumpling.jpg"),
    ("images/staple_水饺.jpg", "images/staple_boiled_dumpling.jpg"),
    ("images/staple_煮玉米.jpg", "images/staple_corn.jpg"),
    ("images/staple_葱油饼.jpg", "images/staple_pancake.jpg"),
    ("images/staple_烤红薯.jpg", "images/staple_sweet_potato.jpg"),
]

for old, new in replacements:
    html = html.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated 10 staple image references')
print(f'Check: staple_rice in HTML: {"staple_rice.jpg" in html}')
print(f'Check: staple_白米饭 NOT in HTML: {"staple_白米饭.jpg" not in html}')
