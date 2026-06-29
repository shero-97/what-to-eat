import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove old hotpot dishes
html = re.sub(r"  \{n:'[^']+',d:'[^']+',c:'火锅',e:'[^']+',img:'[^']+'\},\n", '', html)

# New hotpot dishes
hotpot = [
    ("毛肚","七上八下，脆嫩爽口","火锅","🫕","images/hotpot_maodu.jpg"),
    ("牛肉卷","薄如蝉翼，入口即化","火锅","🥩","images/hotpot_beef_roll.jpg"),
    ("羊肉卷","鲜嫩不膻，涮三秒","火锅","🥩","images/hotpot_lamb_roll.jpg"),
    ("肥肠","Q弹劲道，越嚼越香","火锅","🥩","images/hotpot_intestine.jpg"),
    ("豆干","吸满汤汁，豆香浓郁","火锅","🫘","images/hotpot_dried_tofu.jpg"),
    ("鸭舌","鲜嫩入味，下酒好菜","火锅","🦆","images/hotpot_duck_tongue.jpg"),
    ("青笋","清脆甘甜，解腻佳品","火锅","🥬","images/hotpot_lettuce_stem.jpg"),
    ("龙虾球","Q弹鲜美，一口一个","火锅","🦞","images/hotpot_lobster_ball.jpg"),
    ("咖喱鱼圆","咖喱浓郁，鱼香弹牙","火锅","🍛","images/hotpot_curry_fish_ball.jpg"),
    ("午餐肉","火锅必备，老少皆宜","火锅","🥫","images/hotpot_luncheon_meat.jpg"),
    ("蟹柳","丝丝鲜甜，蟹味十足","火锅","🦀","images/hotpot_crab_stick.jpg"),
    ("海带结","爽滑脆嫩，海中珍品","火锅","🌿","images/hotpot_kelp_knot.jpg"),
    ("海带苗","嫩滑鲜美，营养丰富","火锅","🌿","images/hotpot_kelp_sprout.jpg"),
    ("鱼丸","弹牙多汁，鲜香四溢","火锅","🫕","images/hotpot_fish_ball.jpg"),
    ("巴沙鱼","细嫩无刺，入口即化","火锅","🐟","images/hotpot_basa_fish.jpg"),
    ("宽粉","Q弹爽滑，越煮越有味","火锅","🍜","images/hotpot_wide_noodle.jpg"),
    ("豆腐","嫩滑细腻，吸满汤汁","火锅","🧈","images/hotpot_tofu.jpg"),
    ("虎皮鸡爪","软糯入味，一吮脱骨","火锅","🍗","images/hotpot_chicken_feet.jpg"),
    ("鹌鹑蛋","小巧入味，营养满分","火锅","🥚","images/hotpot_quail_egg.jpg"),
    ("娃娃菜","鲜甜嫩滑，火锅绝配","火锅","🥬","images/hotpot_baby_cabbage.jpg"),
]

entries = '\n'.join(f"  {{n:'{n}',d:'{d}',c:'{c}',e:'{e}',img:'{img}'}}," for n,d,c,e,img in hotpot)

# Find DISHES closing
idx = html.rfind('];')
html = html[:idx] + '\n' + entries + '\n' + html[idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Verify
sq = html.count("'")
print(f"Quotes: {sq} (even: {sq % 2 == 0})")
count = html.count("images/hotpot_")
print(f"Hotpot refs: {count}")
