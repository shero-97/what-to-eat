import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Step 1: Remove staple dishes from the wrong location (inside deleteDish function)
# The broken insert:  if(selected[d.n]){delete selected[d.n  + staple entries
html = re.sub(
    r"(if\(selected\[d\.n\]\)\{delete selected\[d\.n)\n  \{n:'白米饭'[\s\S]*?staple_烤红薯\.jpg'\},\n",
    r"\1",
    html
)

# Step 2: Add them correctly to the DISHES array (before its closing ];)
# Find the last dish in DISHES array and insert after it
staple_entries = """  {n:'白米饭',d:'粒粒晶莹，百搭之王',c:'主食',e:'🍚',img:'images/staple_白米饭.jpg'},
  {n:'蛋炒饭',d:'粒粒分明，香气扑鼻',c:'主食',e:'🍚',img:'images/staple_蛋炒饭.jpg'},
  {n:'炒河粉',d:'河粉油亮，牛肉嫩滑',c:'主食',e:'🍜',img:'images/staple_炒河粉.jpg'},
  {n:'阳春面',d:'清汤细面，葱花飘香',c:'主食',e:'🍜',img:'images/staple_阳春面.jpg'},
  {n:'小米粥',d:'金黄浓稠，养胃暖身',c:'主食',e:'🥣',img:'images/staple_小米粥.jpg'},
  {n:'小笼包',d:'皮薄馅大，热气腾腾',c:'主食',e:'🥟',img:'images/staple_小笼包.jpg'},
  {n:'水饺',d:'皮薄馅大，蘸醋更香',c:'主食',e:'🥟',img:'images/staple_水饺.jpg'},
  {n:'煮玉米',d:'金黄饱满，粗粮健康',c:'主食',e:'🌽',img:'images/staple_煮玉米.jpg'},
  {n:'葱油饼',d:'外酥里软，葱香扑鼻',c:'主食',e:'🫓',img:'images/staple_葱油饼.jpg'},
  {n:'烤红薯',d:'外焦里糯，香甜暖心',c:'主食',e:'🍠',img:'images/staple_烤红薯.jpg'},"""

# Find the end of DISHES array - the ]; right after 炝拌香干丝
pattern = r"(炝拌香干丝',d:'凉拌菜',c:'凉拌菜',e:'🍽️',img:'images/grid_15_4.jpg'},\s*\n)(\s*\];)"
replacement = r"\1" + staple_entries + r"\n\2"
html = re.sub(pattern, replacement, html)
if 'staple_白米饭' in html.split('];')[0]:
    print('Fixed: staples now in DISHES array')
else:
    print('WARNING: may not be fixed')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
