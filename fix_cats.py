import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find and fix CATS
cats_pattern = re.compile(r"const CATS = \[.*?\];")
m = cats_pattern.search(html)
if m:
    old = m.group()
    new = "const CATS = ['荤菜','素菜','荤素结合','凉拌菜','汤','主食','火锅','水果','饮料','甜品零食'];"
    html = html.replace(old, new)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Fixed CATS: {old[:80]}...  ->  {new[:80]}...')
else:
    print('CATS not found!')
