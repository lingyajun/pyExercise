def read_first_lines(dir1, n):
    data = list()
    with open(dir1, 'r') as f:
        lines = f.readlines()
        data = lines[:n]
    return data

dir1 = 'test.txt'
n = 5
print(read_first_lines(dir1, n))

