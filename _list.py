import os
d = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\hotpot_new_212745'
files = sorted(os.listdir(d))
for i, f in enumerate(files):
    # The filenames seem garbled, let's try to extract the number
    import re
    # Try to find the number pattern in the filename
    print(f'{i}: [{repr(f)}]')
