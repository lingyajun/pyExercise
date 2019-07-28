def file_length(dir1):
    with open(dir1, 'r') as f:
        for i, line in enumerate(f):
            print(i, line)
            pass
    return i+1

dir1 = 'test.txt'
arr = file_length(dir1)
print('lines number :', arr)
