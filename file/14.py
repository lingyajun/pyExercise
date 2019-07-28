file2 = 'test-new.txt'
file1 = 'test.txt'

with open(file1, 'r') as f1, open(file2, 'r') as f2:
    for l1,l2 in zip(f1, f2):
        print( l1+l2 )
