def methods():
    a = 1
    b = 100
    c = 'msg'
    print(c, b-a)

code = methods.__code__
x = methods.__code__.co_nlocals

print(methods)
print(code)
print(x)
