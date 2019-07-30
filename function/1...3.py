#1.
def maxNumbers(*nums):
    maxNum = 0
    for n in nums:
        if n>maxNum:
            maxNum = n
    return maxNum

#print(maxNumbers(7,8,9))

#2.
def sumNumbers(*nums):
    sum = 0
    for n in nums:
        sum+=n
    return sum

data = (8, 2, 3, 0, 7)
#print(sumNumbers(*data))

#3.
def multiplyNumbers(*nums):
    r = 1
    for n in nums:
        r *=n
    return r

data2 = (8, 2, 3, -1, 7)
print(multiplyNumbers(*data2))


