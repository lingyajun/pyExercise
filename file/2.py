def read_first_lines(dir1, n):
    data = list()
    with open(dir1, 'r') as f:
        lines = f.readlines()
        data = lines[:n]
    return data

dir1 = 'test.txt'
n = 5
print(read_first_lines(dir1, n))

from itertools import islice
def read_first_lines2(dir1, n):
    with open(dir1, 'r') as f:
        for line in islice(f, n):
            print(line)

read_first_lines2(dir1, n)

