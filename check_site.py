import urllib.request, re, json
url = 'https://shero-97.github.io/what-to-eat/'
html = urllib.request.urlopen(url).read().decode('utf-8')

# Get CATS
m = re.search(r"const CATS = \[(.*?)\];", html)
if m:
    cats = [c.strip("' ") for c in m.group(1).split(",")]
    print("CATS:", cats)

# Get dish categories
dish_cats = set()
for m in re.finditer(r"c:'([^']+)'", html):
    dish_cats.add(m.group(1))
print()
print("Dish categories:", sorted(dish_cats))

# Do they match?
for c in cats:
    in_dish = c in dish_cats
    print(f"  {c}: {'OK' if in_dish else 'MISSING'}")

# Count dishes per category
from collections import Counter
counts = Counter()
for m in re.finditer(r"c:'([^']+)'", html):
    counts[m.group(1)] += 1
print(f"\nTotal dishes: {sum(counts.values())}")
for c, n in sorted(counts.items()):
    print(f"  {c}: {n}")
