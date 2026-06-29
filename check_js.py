import urllib.request, re

url = 'https://shero-97.github.io/what-to-eat/'
html = urllib.request.urlopen(url).read().decode('utf-8')

# Extract the render function and check for issues
script_start = html.find('<script>')
script = html[script_start:]

# Find potential JS issues
# 1. Check for unmatched quotes in dish data
dishes_start = script.find('let DISHES = [')
dishes_end = script.find('\n];', dishes_start)
dishes = script[dishes_start:dishes_end]

# Count open/close quotes
single_quotes = dishes.count("'")
print(f"Single quotes in DISHES: {single_quotes} (should be even: {single_quotes % 2 == 0})")

# 2. Check for common error patterns
if "undefined" in dishes.split("];")[0]:
    print("WARNING: 'undefined' found in dish data!")
if "null" in dishes.split("];")[0] and "'"+dishes.count("null"):
    print("WARNING: 'null' found in dish data!")

# 3. Check the filter function
filter_fn = script[script.find('function render'):script.find('function render')+500]
print("\nRender function found: " + ("function render" in filter_fn))

# 4. Check if buildCats references work
print("\nbuildCats found: " + ("function buildCats" in script))
print("filterCat found: " + ("function filterCat" in script))
