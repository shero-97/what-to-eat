import json, re

# All identified dishes with their image grid positions
# Format: dish_name -> grid_pos (for dedup, keep first occurrence)
dishes_map = {}

grids = {
    0: ["芹菜炒五花肉", "酸菜炒腊肠", "鹿草菇炒腊肉", "干豆角炒肉"],
    1: ["咖喱牛肉", "腊肠炒芹菜", "青椒火腿炒鸡蛋", "黄豆芽炒牛肉"],
    2: ["糖醋排骨", "香辣鸡翅", "蒜苗回锅肉", "肉沫茄子"],
    3: ["葱爆五花肉", "茄汁虾球", "土豆烧牛肉丸", "口蘑蒸蛋"],
    4: ["洋葱肉沫炒鸡蛋", "粉条炒芹菜", "香菇炒火腿肠", "平菇炒鸡蛋"],
    5: ["肉沫腐竹", "辣白菜炒年糕", "番茄焖牛肉丸", "咖喱鸡"],
    6: ["娃娃菜焖油豆泡", "香辣土豆片", "鱼豆腐炒火腿", "家常豆腐"],
    7: ["芹菜炒虾仁", "鸡毛菜炒香菇", "沙葱炒鸡蛋", "芹菜炒香干"],
    # 8=dup of 0, 9 partial dup
    9: ["油爆大虾", "香菇滑鸡", "蒜香口蘑鸡", "麻婆豆腐"],
    10: ["辣白菜炒五花肉", "土豆炒蒜苔", "土豆炒鸡肉", "辣白菜炒土豆片"],
    11: ["香菇烧豆腐", "鱼香西葫芦", "香菇炒青菜", "茄汁包菜"],
    12: ["鸡蛋炒粉条", "火腿鸡蛋炒豆芽", "牛肉丸炒鸡蛋", "番茄肉沫炒蛋"],
    13: ["鱼香鸡蛋", "外婆菜炒鸡蛋", "午餐肉炒土豆丝", "番茄焖菜花"],
    14: ["肉沫豆腐煲", "酸汤小酥肉", "香辣手撕鸡", "腐竹焖荷包蛋"],
    15: ["凉拌卤牛肉", "凉拌油豆皮", "凉拌包菜", "炝拌香干丝"],
}

for gid, names in grids.items():
    for pi, name in enumerate(names):
        if name not in dishes_map:
            dishes_map[name] = f"images/grid_{gid:02d}_{pi+1}.jpg"

# Categorize dishes
def categorize(name):
    n = name
    # 凉拌菜
    if '凉拌' in n or '炝拌' in n:
        return '凉拌菜'
    # 荤菜 - mainly meat, no vegetables in name
    if n in ['糖醋排骨','香辣鸡翅','咖喱牛肉','油爆大虾','咖喱鸡','酸汤小酥肉','香辣手撕鸡','茄汁虾球',
             '蒜苗回锅肉','黄豆芽炒牛肉','葱爆五花肉']:
        return '荤菜'
    if ('排骨' in n or '鸡翅' in n or '牛肉' in n or '大虾' in n or '小酥肉' in n or '手撕鸡' in n):
        return '荤菜'
    # 素菜
    if '肉' not in n and '鸡' not in n and '虾' not in n and '蛋' not in n and '肠' not in n and '鱼' not in n:
        if '豆腐' in n or '土豆' in n or '茄汁' in n or '香菇' in n or '娃娃菜' in n or '鱼香' in n or '麻婆' in n:
            return '素菜'
    # Default: 荤素结合
    return '荤素结合'

# Build dish entries
dishes = []
for name, img in dishes_map.items():
    cat = categorize(name)
    dishes.append({
        'n': name,
        'd': cat,
        'c': cat,
        'e': '🍽️',
        'img': img
    })

# Save mapping
with open(r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\dish_mapping.json', 'w', encoding='utf-8') as f:
    json.dump(dishes, f, ensure_ascii=False, indent=2)

# Print summary
cats = {}
for d in dishes:
    cats[d['c']] = cats.get(d['c'], 0) + 1
print(f"Total unique dishes: {len(dishes)}")
for c, n in sorted(cats.items()):
    print(f"  {c}: {n}")
print("\nSample dishes:")
for d in dishes[:5]:
    print(f"  {d['n']} -> {d['c']} -> {d['img']}")
