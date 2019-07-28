from collections import Counter

def read_frequency(dir1):
    words = list()
    with open(dir1, 'r') as f:
        words = f.read().split()
    print(words)
    return Counter(words)


dir1 = 'test.txt'
freq = read_frequency(dir1)
print('----frequency --- ')
print(freq)

