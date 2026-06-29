import os
d = r'D:\openclaw-autoclaw\.openclaw-autoclaw\agents\agent-gcglc\workspace\what-to-eat\hotpot_new_212745'
files = sorted(os.listdir(d))
for i, f in enumerate(files):
    print(os.path.join(d, f))
