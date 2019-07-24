import random
def generatelist():
    n = 30
    array = list()
    for i in range(n):
        data=0
        if i < 5 or i > n-6 :
            data = randrange(1,30) ** 2
        else:
            data = random()
        array.append(data)
    return array


def generatelist2():
    array = list()
    for i in range(1,31):
        array.append(i**2)
    return array

array = generatelist2()
print(array[:5])
print(array[-5:])

