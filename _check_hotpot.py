import re

with open(r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all hotpot entries
hotpot_matches = re.findall(r"\{n:'([^']+)',d:'([^']+)',c:'火锅',e:'([^']+)',img:'([^']+)'\}", content)
print(f"Total火锅 entries: {len(hotpot_matches)}")
for name, desc, emoji, img in hotpot_matches:
    print(f"  {name} | {desc} | {img}")

# Also find the line numbers
lines = content.split('\n')
for i, line in enumerate(lines):
    if "c:'火锅'" in line:
        print(f"  Line {i+1}: {line.strip()[:100]}")
