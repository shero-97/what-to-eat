import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('let DISHES = [')
end = content.find('];', start)
segment = content[start:end+2]

print(f'DISHES from {start} to {end}, length={len(segment)} chars')

# Find all entries
pattern = re.compile(r"\{n:'([^']+)',d:'([^']*)',c:'([^']*)',e:'([^']*)',img:'([^']+)'\}")
entries = pattern.findall(segment)

fruit_count = 0
for n, d, c, e, img in entries:
    if '水果' in c:
        fruit_count += 1
        print(f'  {n} | cat={c} | img={img}')

print(f'\nTotal fruit entries: {fruit_count}')
print(f'Total entries: {len(entries)}')
