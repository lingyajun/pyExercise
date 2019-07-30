# 递归
def pascal_triangle(n):
    if n <2 :
        p = [1]
        print(p)
        return p
    px = pascal_triangle(n-1)
    p=list()
    p.append(1)

    if n>2:
        for i in range(n-2):
            a = px[i]+px[i+1]
            p.append(a)

    p.append(1)

#    print(px)
    print(p)

    return p

pascal_triangle(6)
#print(pascal_triangle(6))
'''
print(pascal_triangle(1))
print(pascal_triangle(2))
print(pascal_triangle(3))
print(pascal_triangle(4))
print(pascal_triangle(5))
print(pascal_triangle(10))
print(pascal_triangle(7))
'''

# 空位补0 ， zip 循环
def pascal_triangle2(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
 #  return n>=1

print('--------')
pascal_triangle2(6) 

