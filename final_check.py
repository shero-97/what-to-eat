import re

with open(r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

ok = True

# Check basic structure
for label, needle in [
    ('DOCTYPE', '<!DOCTYPE html>'),
    ('DISHES start', 'let DISHES = ['),
    ('script close', '</script>'),
    ('html close', '</html>'),
]:
    if needle not in content:
        print('FAIL: %s' % label)
        ok = False

# Count braces in DISHES block
start = content.find('let DISHES = [')
end = content.find('];', start) + 2
dishes_section = content[start:end]
opens = dishes_section.count('{')
closes = dishes_section.count('}')
print('DISHES braces: {=%d }=%d %s' % (opens, closes, 'OK' if opens==closes else 'MISMATCH'))
if opens != closes:
    ok = False

# Count drink_ references
drink_count = content.count('images/drink_')
print('drink_ image refs: %d %s' % (drink_count, 'OK' if drink_count==28 else 'MISMATCH'))
if drink_count != 28:
    ok = False

# Check no old fruitdrink refs remain
old = content.count('fruitdrink_')
print('old fruitdrink_ refs: %d %s' % (old, 'OK' if old==0 else 'LEFTOVER'))
if old != 0:
    ok = False

# Check DISHES continues after drinks (not truncated)
end_idx = content.find('];', start)
next_line = content[end_idx:end_idx+20]
print('After DISHES: %s' % repr(next_line))

if ok:
    print('\n=== VALIDATION: ALL CHECKS PASSED ===')
else:
    print('\n=== VALIDATION: ISSUES FOUND ===')
