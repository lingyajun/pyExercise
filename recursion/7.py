'''
def f(x):
    if x<0:
        return 0
'''

#f1=y  f2=y-2  f3=y-4..fx = y-2**(x-1)，fx+1 = y-2**(x)

def sum_series(n):
    sun = 0
    def f(x):
        #r = n-2**(x-1)
        pows = 2**(x-1)
        if n<pows:
            return 0
        r = f(x+1)+pows
        print(x, r, sep=' : ')
        if r <0:
            return 0
        return r
    sun += f(1)
    return sun
'''
s = sum_series(6)
print(s)
s = sum_series(10)
print(s)
'''

# a1 = y; ax= n-2**(x-1)<=0
# a1 = y, a2= y-2 ... ax = y-2**(x-1)
# sum(x) = sum(x-1) + ax
# sum（t）=sum（t+1） + 2**(t-1)
'''
def sum_series2(n):
    sun = 0
    def a(x):
        r = n-2**(x-1)
        if r<0:
            r=0
        return r

    def sum(x):
        s = sum（x-1） + a(x)
    sun += f(1)
    return sun
'''
import math
def sum_series3(n):
    t = int(math.sqrt(n))+1
    print('-sqrt--',n, t, sep=' : ')
    def a(x):
        r = n-2**(x-1)
        print('[ax]',x, r, sep=' : ')
        if r<0:
            r=0
        return r

    def sums(x):
        if x <2:
            return n
        s = sums(x-1) + a(x)
        return s
    return sums(t)

s = sum_series3(6)
print(s)
s = sum_series3(10)
print(s)
