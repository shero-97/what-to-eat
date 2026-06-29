import os, json
from PIL import Image

tmp = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\temp_new'
out = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\images'

# All identified dishes with grid layout info
# Format: (source_file, grid_rows, grid_cols, header_ratio, dish_list)
# dish_list: list of (name, description, category, emoji)

fruit_data = [
    ("水果_01.jpg", 3, 3, 0.13, [
        ("黄河蜜瓜","口感甜蜜，11kcal/100g","水果","🍈"),
        ("白兰瓜","不含脂肪，热量低","水果","🍈"),
        ("圣女果","红番茄素，降低热量摄取","水果","🍅"),
        ("白凤桃","低热量低胆固醇","水果","🍑"),
        ("黄心西瓜","低热量高含水量","水果","🍉"),
        ("青木瓜","水分足膳食纤维丰富","水果","🫒"),
        ("杨梅","热量低脂肪少","水果","🍒"),
        ("杨桃","富含膳食纤维","水果","⭐"),
        ("草莓","纤维素高饱腹感强","水果","🍓"),
    ]),
    ("水果_02.jpg", 3, 3, 0.13, [
        ("西柚","低卡高纤维","水果","🍊"),
        ("芭乐","维C之王低热量","水果","🫒"),
        ("哈密瓜","清甜爽口水分足","水果","🍈"),
        ("网纹瓜","香甜软糯","水果","🍈"),
        ("芒果","香甜浓郁热带风味","水果","🥭"),
        ("丑橘","清甜多汁不上火","水果","🍊"),
        ("柠檬","维C丰富清爽解腻","水果","🍋"),
        ("李子","酸甜可口","水果","🫐"),
        ("杏子","酸甜多汁","水果","🍑"),
    ]),
    ("水果_03.jpg", 3, 3, 0.13, [
        ("红心柚","红肉清甜低热量","水果","🍊"),
        ("葡萄柚","微苦回甘燃脂佳品","水果","🍊"),
        ("莲雾","清脆多汁低糖分","水果","🍎"),
        ("枇杷","润肺止咳清甜","水果","🍑"),
        ("西梅","通便润肠低脂","水果","🫐"),
        ("黑莓","花青素之王抗氧化","水果","🫐"),
        ("青枣","维C丰富清脆可口","水果","🫒"),
        ("油桃","光滑无毛清甜","水果","🍑"),
        ("菠萝","酸甜多汁助消化","水果","🍍"),
    ]),
    ("水果_04.jpg", 3, 3, 0.13, [
        ("沃柑","热量低水分充足","水果","🍊"),
        ("樱桃","膳食纤维饱腹感强","水果","🍒"),
        ("梨子","膳食纤维维C丰富","水果","🍐"),
        ("覆盆子","富含膳食纤维","水果","🫐"),
        ("苹果","含水量高增强饱腹","水果","🍎"),
        ("火龙果","富含水分及纤维素","水果","🐉"),
        ("黄桃","热量低脂肪少","水果","🍑"),
        ("蓝莓","低热量含糖低","水果","🫐"),
        ("猕猴桃","膳食纤维维C丰富","水果","🥝"),
    ]),
    ("水果_05.jpg", 4, 4, 0.12, [
        ("椰子肉","热带风味能量足","水果","🥥"),
        ("干红枣","补血养颜天然甜","水果","🫘"),
        ("牛油果","健康脂肪营养密","水果","🥑"),
        ("榴莲","水果之王浓郁香","水果","🫒"),
        ("蛋黄果","粉糯香甜","水果","🥚"),
        ("沙棘","维C炸弹酸爽","水果","🫐"),
        ("芭蕉","软糯香甜能量足","水果","🍌"),
        ("冬枣","脆甜可口维C高","水果","🫒"),
        ("菠萝蜜","热带巨果甜蜜蜜","水果","🫒"),
        ("山楂","酸甜开胃助消化","水果","🍒"),
        ("百香果","芳香四溢维C多","水果","🟣"),
        ("人生果","清甜多汁低糖","水果","🍈"),
        ("释迦","奶香甜蜜热带果","水果","🫒"),
        ("柿子","软糯甜蜜秋之味","水果","🟠"),
        ("山竹","果中皇后清甜","水果","🍑"),
        ("荔枝","甜美多汁岭南佳","水果","🍒"),
    ]),
]

drink_data = [
    ("饮料_01.jpg", 4, 4, 0.10, [
        ("可口可乐","冰爽刺激经典永流传","饮料","🥤"),
        ("芬达","橙味气泡青春记忆","饮料","🧃"),
        ("雪碧","透心凉柠檬味","饮料","🥤"),
        ("北冰洋","老北京桔子汽水","饮料","🍊"),
        ("屈臣氏","苏打水清爽零卡","饮料","💧"),
        ("旺仔牛奶","香甜浓郁童年味道","饮料","🥛"),
        ("美年达","果味汽水缤纷多彩","饮料","🧃"),
        ("百事可乐","经典可乐年轻选择","饮料","🥤"),
        ("冻柠茶","冰爽柠檬茶港式风味","饮料","🍋"),
        ("统一蜜桃多","蜜桃香甜清爽","饮料","🍑"),
        ("雪花啤酒","清凉畅爽","饮料","🍺"),
        ("酷儿","Q萌橙汁童年回忆","饮料","🧃"),
        ("维他气泡茶","茶香气泡新体验","饮料","🍵"),
        ("七喜","柠檬汽水清爽","饮料","🥤"),
        ("COSTA咖啡","英伦咖啡醇香","饮料","☕"),
        ("王老吉","怕上火喝王老吉","饮料","🧃"),
    ]),
    ("饮料_02.jpg", 3, 4, 0.10, [
        ("统一春拂绿茶","清新绿茶回甘","饮料","🍵"),
        ("HPP沃柑汁","鲜榨冷压工艺","饮料","🍊"),
        ("东方树叶乌龙茶","醇厚乌龙回甘","饮料","🍵"),
        ("芬达橙味汽水","经典橙味气泡足","饮料","🧃"),
        ("东方树叶茉莉花茶","茉莉清香淡雅","饮料","🍵"),
        ("大窑橙诺","橙味汽水怀旧风","饮料","🍊"),
        ("元气森林气泡水","零糖零卡橙味","饮料","🥤"),
        ("腊梅红茶","红茶醇香暖心","饮料","🍵"),
        ("小象NFC苹果汁","纯鲜榨不加糖","饮料","🧃"),
        ("鸭屎香柠檬茶","茶香柠檬新潮","饮料","🍋"),
        ("NFC橙汁","鲜榨纯橙汁无添加","饮料","🍊"),
        ("北冰洋橙味汽水","老牌橙味汽水","饮料","🍊"),
    ]),
]

all_dishes = []

for src_file, rows, cols, header_ratio, dishes in fruit_data + drink_data:
    src_path = os.path.join(tmp, src_file)
    if not os.path.exists(src_path):
        # Try to find by encoding
        for f in os.listdir(tmp):
            if src_file[:3] in f and src_file[-4:] in f:
                src_path = os.path.join(tmp, f)
                break
        else:
            print(f"NOT FOUND: {src_file}")
            continue
    
    img = Image.open(src_path)
    w, h = img.size
    header_h = int(h * header_ratio)
    
    for idx, (name, desc, cat, emoji) in enumerate(dishes):
        row = idx // cols
        col = idx % cols
        
        cell_w = w // cols
        cell_h = (h - header_h) // rows
        
        x1 = col * cell_w
        y1 = header_h + row * cell_h
        x2 = min(x1 + cell_w, w)
        y2 = min(y1 + cell_h, h)
        
        crop = img.crop((x1, y1, x2, y2))
        ratio = 300 / crop.size[0]
        crop = crop.resize((300, int(crop.size[1] * ratio)), Image.LANCZOS)
        
        fname = f"fruitdrink_{src_file[:-4]}_{idx:02d}.jpg".replace(' ', '_')
        fpath = os.path.join(out, fname)
        crop.save(fpath, 'JPEG', quality=85)
        
        all_dishes.append({
            'n': name, 'd': desc, 'c': cat, 'e': emoji,
            'img': f'images/{fname}'
        })
        print(f'  {name} -> {fname}')

print(f'\nTotal new dishes: {len(all_dishes)}')

# Save mapping
with open(os.path.join(out, '..', 'fruitdrink_dishes.json'), 'w', encoding='utf-8') as f:
    json.dump(all_dishes, f, ensure_ascii=False, indent=2)
