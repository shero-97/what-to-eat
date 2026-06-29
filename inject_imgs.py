import json, re

with open('img_urls.json', 'r', encoding='utf-8') as f:
    imgs = json.load(f)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

count = 0
for name, url in imgs.items():
    esc = re.escape(name)
    pattern = r"(n:'" + esc + r"'[^}]*e:'[^']*')(})"
    repl = r"\1,img:'" + url + r"'}";
    new_html = re.sub(pattern, repl, html)
    if new_html != html:
        html = new_html
        count += 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Updated {count} dishes with images')
