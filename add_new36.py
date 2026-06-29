import re

new_dishes = [
    # Grid 01
    ("清炒老南瓜","清淡香甜，软糯可口","素菜","🎃","new_menu_01_1"),
    ("香菇炒肉","菌香肉嫩，下饭好菜","荤素结合","🍄","new_menu_01_2"),
    ("甜椒炒生菜","清脆爽口，色彩诱人","素菜","🫑","new_menu_01_3"),
    ("胡萝卜炒佛手瓜","清甜脆嫩，健康素食","素菜","🥕","new_menu_01_4"),
    # Grid 02
    ("毛豆炒肉沫","豆香肉香，拌饭绝配","荤素结合","🫘","new_menu_02_1"),
    ("素炒空心菜","清脆碧绿，蒜香四溢","素菜","🥬","new_menu_02_2"),
    ("酸辣白菜","酸辣开胃，爽脆可口","素菜","🥬","new_menu_02_3"),
    ("丝瓜炒肉","丝瓜清甜，肉片嫩滑","荤素结合","🥒","new_menu_02_4"),
    # Grid 03
    ("午餐肉炒娃娃菜","娃娃菜鲜甜，午餐肉咸香","荤素结合","🥬","new_menu_03_1"),
    ("西葫芦炒鸡蛋","嫩滑鲜美，快手家常","荤素结合","🥒","new_menu_03_2"),
    ("素炒菠菜","碧绿鲜嫩，营养丰富","素菜","🥬","new_menu_03_3"),
    ("川芹炒肉","芹菜脆嫩，肉香浓郁","荤素结合","🥬","new_menu_03_4"),
    # Grid 04
    ("清炒小白菜","清淡鲜嫩，原汁原味","素菜","🥬","new_menu_04_1"),
    ("甜椒炒豆芽","清脆爽口，色彩缤纷","素菜","🫑","new_menu_04_2"),
    ("糖醋里脊","外酥里嫩，酸甜可口","荤菜","🥩","new_menu_04_3"),
    ("丝瓜炒蛋","嫩滑鲜美，清淡可口","荤素结合","🥒","new_menu_04_4"),
    # Grid 05
    ("腐竹青椒","腐竹吸汁，青椒脆爽","素菜","🫑","new_menu_05_1"),
    ("素炒茄子","软烂入味，酱香浓郁","素菜","🍆","new_menu_05_2"),
    ("双椒炒蛋","双椒鲜辣，蛋香浓郁","荤素结合","🫑","new_menu_05_3"),
    ("白菜炒肉","家常味道，温暖舒心","荤素结合","🥬","new_menu_05_4"),
    # Grid 06
    ("鸡丝黄瓜","清爽鲜嫩，低脂健康","荤素结合","🥒","new_menu_06_1"),
    ("青椒土豆丝","经典搭配，爽脆下饭","荤素结合","🥔","new_menu_06_2"),
    ("白菜豆腐","清淡鲜美，素雅健康","素菜","🥬","new_menu_06_3"),
    ("清炒莲藕","脆嫩清甜，口感独特","素菜","🪷","new_menu_06_4"),
    # Grid 07
    ("火腿肠炒小瓜","小瓜清甜，火腿咸香","荤素结合","🥒","new_menu_07_1"),
    ("焖板栗南瓜","粉糯香甜，板栗增香","素菜","🎃","new_menu_07_2"),
    ("干焙洋芋丝","外酥里软，土豆新吃法","素菜","🥔","new_menu_07_3"),
    ("清炒油麦菜","清脆碧绿，蒜香十足","素菜","🥬","new_menu_07_4"),
    # Grid 08
    ("豆豉炒蕨菜","豉香浓郁，蕨菜脆嫩","素菜","🌿","new_menu_08_1"),
    ("青椒炒平菇","菌香四溢，青椒提味","素菜","🍄","new_menu_08_2"),
    ("青椒炒肉","家常经典，下饭神器","荤素结合","🫑","new_menu_08_3"),
    ("土豆焖鸡","土豆软糯，鸡肉入味","荤素结合","🍗","new_menu_08_4"),
    # Grid 09
    ("爆炒猪肝","嫩滑鲜香，补血佳品","荤菜","🥩","new_menu_09_1"),
    ("素炒上海青","清脆碧绿，原汁原味","素菜","🥬","new_menu_09_2"),
    ("炒土豆","朴实无华，家常味道","素菜","🥔","new_menu_09_3"),
    ("秋葵炒蛋","滑嫩清爽，营养丰富","荤素结合","🥚","new_menu_09_4"),
]

# Build entries
entries = []
for n, d, c, e, img_id in new_dishes:
    entries.append(f"  {{n:'{n}',d:'{d}',c:'{c}',e:'{e}',img:'images/{img_id}.jpg'}},")

# Read HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the closing of DISHES array (after staple_烤红薯)
# Search for the pattern: staple_烤红薯.jpg'},\n];
pattern = r"(staple_烤红薯\.jpg'},\n)(\s*\];)"
replacement = r"\1" + '\n'.join(entries) + r"\n\2"
html = re.sub(pattern, replacement, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Added {len(new_dishes)} new dishes')
print(f'Total DISHES references: {html.count("img:")}')

# Verify
cats = {}
for n, d, c, e, _ in new_dishes:
    cats[c] = cats.get(c, 0) + 1
for c, n in sorted(cats.items()):
    print(f'  {c}: {n}')
