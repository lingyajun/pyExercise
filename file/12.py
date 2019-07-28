dir1 = 'test-new.txt'
data = [22,33,44,55,99]

with open(dir1, 'w') as f:
    #f.write(data)
    for m in data:
        f.write(f'{ str(m)}\n')

