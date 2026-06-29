import subprocess, json, os, time, urllib.request

script = r"D:\.openclaw-autoclaw\skills\autoglm-generate-image-seedream\generate-image-seedream.py"
outdir = r"D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\images"

dishes = [
    ("白米饭", "一碗热气腾腾的白米饭，白色陶瓷碗，粒粒晶莹，美食摄影，柔和自然光"),
    ("蛋炒饭", "一盘金黄色的蛋炒饭，粒粒分明，葱花点缀，中式美食摄影"),
    ("炒河粉", "一盘干炒牛河，河粉油亮，牛肉嫩滑，豆芽青翠，粤式美食"),
    ("阳春面", "一碗清汤阳春面，细面条，葱花飘香，中式面食摄影"),
    ("小米粥", "一碗金黄小米粥，浓稠细腻，配小菜，养胃早餐，美食摄影"),
    ("小笼包", "一笼热气腾腾的小笼包，皮薄馅大，蒸笼里冒着热气，中式早餐"),
    ("水饺", "一盘白胖的水饺，蘸醋，皮薄馅大，中式传统美食，俯拍"),
    ("煮玉米", "一根金黄色的煮玉米，粒粒饱满，冒着热气，粗粮美食"),
    ("葱油饼", "一张金黄酥脆的葱油饼，切块，层次分明，葱香四溢，中式面食"),
    ("烤红薯", "一个烤红薯，外皮焦香，掰开后金黄软糯，冒着热气，街边美食"),
]

images = {}

for i, (name, prompt) in enumerate(dishes):
    print(f"[{i+1}/10] Generating {name}...")
    result = subprocess.run(["python", script, prompt], capture_output=True, text=True, timeout=120)
    try:
        data = json.loads(result.stdout.strip())
        url = data["data"]["image_url"]
        # Download
        filename = f"staple_{name}.jpg"
        filepath = os.path.join(outdir, filename)
        urllib.request.urlretrieve(url, filepath)
        images[name] = f"images/{filename}"
        print(f"  OK: {filename} ({os.path.getsize(filepath)} bytes)")
    except Exception as e:
        print(f"  FAIL: {e}")
    time.sleep(1)

# Save mapping
with open(os.path.join(outdir, "..", "staple_dishes.json"), "w", encoding="utf-8") as f:
    json.dump(images, f, ensure_ascii=False, indent=2)

print(f"\nDone! {len(images)}/10 images generated")
