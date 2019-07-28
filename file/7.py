def file_read_array(dir1):
    arr = []
    with open(dir1, 'r') as f:
        for line in f:
            arr.append(line)
    return arr

dir1 = 'test.txt'
arr = file_read_array(dir1)
print(arr)
