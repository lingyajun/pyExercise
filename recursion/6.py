def sumDigits(n):
    if n <10:
        return n

    mod = n % 10
    k = n//10

    sum = mod + sumDigits(k)
    return sum

s= sumDigits(345) 
print(s)
s= sumDigits(45) 
print(s)
s= sumDigits(12) 
print(s)
