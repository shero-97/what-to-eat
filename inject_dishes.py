import json, re

with open(r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\dish_mapping.json', 'r', encoding='utf-8') as f:
    new_dishes = json.load(f)

with open(r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build new DISHES array
lines = []
for d in new_dishes:
    img = d['img']
    lines.append(f"  {{n:'{d['n']}',d:'{d['d']}',c:'{d['c']}',e:'{d['e']}',img:'{img}'}},")

new_array = 'let DISHES = [\n' + '\n'.join(lines) + '\n];'

# Replace the DISHES array in HTML
# Find the pattern: let DISHES = [...]
pattern = r'let DISHES = \[[\s\S]*?\n\];'
html = re.sub(pattern, new_array, html)

with open(r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Wrote {len(new_dishes)} dishes to index.html')
