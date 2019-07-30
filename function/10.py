#import math
def divisors(n):
    r = list()
    #sqrt = int(math.sqrt(n))
    maxRange = int(n/2+1)
    for i in range(1, maxRange):
        if n%i ==0:
            r.append(i)
    return r

def sumNumbers(*nums):
    sum = 0
    for n in nums:
        sum+=n
    return sum

def checkPerfect(n):
    r = divisors(n)
    sum = sumNumbers(*r)
    print('-----',n, r, sum, '-----',sep='\n')
    return n == sum

print(checkPerfect(6),checkPerfect(28),checkPerfect(496))


def perfectNum(n):
    sum = 0
    maxRange = int(n/2+1)
    for i in range(1, maxRange):
        if n%i ==0:
            sum += i
    return n == sum

print(perfectNum(6),perfectNum(28),perfectNum(496))


