class TestPython:
    def __init__(self):
        print('__init__')
    def testFun(self):
        print('testFun')

test = TestPython()
d = dir(test)
print(d)
'''
name = test.__class__
print(name)
print(test)
print(TestPython)
'''

t = type(test)
print(t)
name = type(test).__name__
print(name)

name = test.__class__.__name__
print(name)
