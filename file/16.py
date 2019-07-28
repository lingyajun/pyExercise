file1 = 'test.txt'

f = open(file1, 'r')
print(f,'',f.closed,'', sep='\n')
f.close()

print(f,'',f.closed, sep='\n')

