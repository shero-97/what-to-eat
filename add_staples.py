import re

# New dishes to add
staples = [
    ("白米饭", "粒粒晶莹，百搭之王", "主食", "🍚", "images/staple_白米饭.jpg"),
    ("蛋炒饭", "粒粒分明，香气扑鼻", "主食", "🍚", "images/staple_蛋炒饭.jpg"),
    ("炒河粉", "河粉油亮，牛肉嫩滑", "主食", "🍜", "images/staple_炒河粉.jpg"),
    ("阳春面", "清汤细面，葱花飘香", "主食", "🍜", "images/staple_阳春面.jpg"),
    ("小米粥", "金黄浓稠，养胃暖身", "主食", "🥣", "images/staple_小米粥.jpg"),
    ("小笼包", "皮薄馅大，热气腾腾", "主食", "🥟", "images/staple_小笼包.jpg"),
    ("水饺", "皮薄馅大，蘸醋更香", "主食", "🥟", "images/staple_水饺.jpg"),
    ("煮玉米", "金黄饱满，粗粮健康", "主食", "🌽", "images/staple_煮玉米.jpg"),
    ("葱油饼", "外酥里软，葱香扑鼻", "主食", "🫓", "images/staple_葱油饼.jpg"),
    ("烤红薯", "外焦里糯，香甜暖心", "主食", "🍠", "images/staple_烤红薯.jpg"),
]

with open(r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build new entries
entries = []
for n, d, c, e, img in staples:
    entries.append(f"  {{n:'{n}',d:'{d}',c:'{c}',e:'{e}',img:'{img}'}},")

# Insert before the closing ]; of the DISHES array
# Find the last ]; after DISHES
insert_point = html.rfind('];')
new_html = html[:insert_point] + '\n' + '\n'.join(entries) + '\n' + html[insert_point:]

with open(r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f'Added {len(staples)} staple dishes')

# Now check if the images exist
import os
imgdir = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\images'
for _, _, _, _, img in staples:
    fname = img.replace('images/', '')
    path = os.path.join(imgdir, fname)
    sz = os.path.getsize(path) if os.path.exists(path) else 0
    print(f'  {fname}: {"OK "+str(sz)+"B" if sz else "MISSING"}')
