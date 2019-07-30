def power(a,b):
    r = 1
    if b <1:
        r = 1
    else:
        r = a* power(a,b-1)
    return r

r = power(3,4)
print(r)
