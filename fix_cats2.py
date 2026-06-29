import re

with open('index.html', 'rb') as f:
    data = f.read()

# Find CATS line by searching for the ASCII prefix
prefix = b"const CATS = ["
pos = data.find(prefix)
if pos >= 0:
    # Find end of this line
    end = data.find(b"\n", pos)
    old_line = data[pos:end]
    # Create correct CATS line
    new_line = "const CATS = ['荤菜','素菜','荤素结合','凉拌菜','汤','主食','火锅','水果','饮料','甜品零食'];".encode('utf-8')
    data = data[:pos] + new_line + data[end:]
    
    with open('index.html', 'wb') as f:
        f.write(data)
    print('Fixed CATS line in raw bytes')
    print(f'Old line bytes: {len(old_line)}')
    print(f'New line bytes: {len(new_line)}')
else:
    print('CATS not found!')
