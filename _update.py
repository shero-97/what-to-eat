import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Name → English filename mapping
name_map = {
    '黄河蜜瓜': 'fruit_yellow_river_melon.jpg',
    '白兰瓜': 'fruit_bailan_melon.jpg',
    '圣女果': 'fruit_cherry_tomato.jpg',
    '白凤桃': 'fruit_white_phoenix_peach.jpg',
    '黄心西瓜': 'fruit_yellow_watermelon.jpg',
    '青木瓜': 'fruit_green_papaya.jpg',
    '杨梅': 'fruit_bayberry.jpg',
    '杨桃': 'fruit_star_fruit.jpg',
    '草莓': 'fruit_strawberry.jpg',
    '西柚': 'fruit_grapefruit_2.jpg',
    '芭乐': 'fruit_guava.jpg',
    '哈密瓜': 'fruit_honeydew.jpg',
    '网纹瓜': 'fruit_netted_melon.jpg',
    '芒果': 'fruit_mango.jpg',
    '丑橘': 'fruit_ugly_orange.jpg',
    '柠檬': 'fruit_lemon.jpg',
    '李子': 'fruit_plum.jpg',
    '杏子': 'fruit_apricot.jpg',
    '红心柚': 'fruit_red_pomelo.jpg',
    '葡萄柚': 'fruit_grapefruit.jpg',
    '莲雾': 'fruit_wax_apple.jpg',
    '枇杷': 'fruit_loquat.jpg',
    '西梅': 'fruit_prune.jpg',
    '黑莓': 'fruit_blackberry.jpg',
    '青枣': 'fruit_green_jujube.jpg',
    '油桃': 'fruit_nectarine.jpg',
    '菠萝': 'fruit_pineapple.jpg',
    '沃柑': 'fruit_tangerine.jpg',
    '樱桃': 'fruit_cherry.jpg',
    '梨子': 'fruit_pear.jpg',
    '覆盆子': 'fruit_raspberry.jpg',
    '苹果': 'fruit_apple.jpg',
    '火龙果': 'fruit_dragon_fruit.jpg',
    '黄桃': 'fruit_yellow_peach.jpg',
    '蓝莓': 'fruit_blueberry.jpg',
    '猕猴桃': 'fruit_kiwi.jpg',
    '椰子肉': 'fruit_coconut_meat.jpg',
    '干红枣': 'fruit_dried_red_date.jpg',
    '牛油果': 'fruit_avocado.jpg',
    '榴莲': 'fruit_durian.jpg',
    '蛋黄果': 'fruit_egg_fruit.jpg',
    '沙棘': 'fruit_sea_buckthorn.jpg',
    '芭蕉': 'fruit_plantain.jpg',
    '冬枣': 'fruit_winter_jujube.jpg',
    '菠萝蜜': 'fruit_jackfruit.jpg',
    '山楂': 'fruit_hawthorn.jpg',
    '百香果': 'fruit_passion_fruit.jpg',
    '人生果': 'fruit_ginseng_fruit.jpg',
    '释迦': 'fruit_sugar_apple.jpg',
    '柿子': 'fruit_persimmon.jpg',
    '山竹': 'fruit_mangosteen.jpg',
    '荔枝': 'fruit_lychee.jpg',
}

count = 0
for cn_name, en_file in name_map.items():
    # Build pattern: n:'NAME',...,img:'OLD_PATH'
    # We need to find each dish entry and replace just the img part
    pattern = re.compile(
        r"(\{n:'" + re.escape(cn_name) + r"'[^}]*img:')" +
        r"[^']*" +
        r"(')",
        re.DOTALL
    )
    new_content = pattern.sub(r"\1images/" + en_file + r"\2", content)
    if new_content != content:
        count += 1
        content = new_content
        print(f'Updated: {cn_name} -> images/{en_file}')
    else:
        print(f'NOT FOUND: {cn_name}')

print(f'\nTotal updated: {count}/{len(name_map)}')

# Write back
with open(r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')
