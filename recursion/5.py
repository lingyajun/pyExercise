def fib(n):
    r = 1
    if n < 3:
        r=1
    else:
        r = fib(n-2)+fib(n-1)
#    print(r)
    return r

print('fib(10):', fib(10))
#fib(10)

