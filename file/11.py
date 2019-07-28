import os
def file_info(dir1):
    info = os.stat(dir1)
    return info

dir1 = 'test.txt'
info = file_info(dir1)
print(info,'' ,info.st_size, sep = '\n')
