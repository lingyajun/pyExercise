class Math:
    def pow(self,x, n):
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
        if n == 1:
            return x
        return self.pow(x, n-1) * x

x, n = 2,3
r = Math().pow(x, n)
print(x, n, r)

x, n = 1,3
r = Math().pow(x, n)
print(x, n, r)


x, n = 3,3
r = Math().pow(x, n)
print(x, n, r)


x, n = 3,4
r = Math().pow(x, n)
print(x, n, r)
