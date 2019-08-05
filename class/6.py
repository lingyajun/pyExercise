class Sum:
    def sumArray(self, array):
        result = []
        #i, j = 0, 0
        size = len(array)
        for i in range(size-2):
            for j in range(i+1, size-1):
                x0,x1 = array[i], array[j]
                x2 = - x0 - x1
                if x2 in array[j:]:
                    result.append([x0,x1,x2])
        return result

array = [-25, -10, -7, -3, 2, 4, 8, 10]
opt = Sum().sumArray(array)
print(opt)
