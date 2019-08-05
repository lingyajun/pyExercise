'''
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''
'''
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

链接：https://leetcode-cn.com/problems/integer-to-roman
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
    // IV, IX, XL, XC, CD, CM
'''

''' 
输入: 3
输出: "III"

输入: 4
输出: "IV"

输入: 9
输出: "IX"

输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
'''

class Num:
    #sybl = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        #  IV, IX, XL, XC, CD, CM
    __rs = ['M', 'CM', 'D','CD',
                'C', 'XC','L', 'XL',
                'X','IX', 'V', 'IV', 'I']
    __ns = [1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4, 1]

    def int2Roman(self, num):
        '''
        给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
        '''

        roman=''
        size = len(Num.__ns)
        for i in range(size):
            count = num // Num.__ns[i]
            num = num % Num.__ns[i]
            if count > 0:
                roman += Num.__rs[i] * count

        return roman

    def Roman2int(self, roman):
        num = 0
        size = len(Num.__rs)
        for i in range(size):
            syb = Num.__rs[i]
           # count = roman.count(syb)
            while roman != '':
                if roman.startswith(syb):
                    num += Num.__ns[i]
                    roman = roman[len(syb):]
                    #roman = roman.replace(syb, '')
                else:
                    break
            #if count > 0:
                #num += Num.__ns[i] * count
                #roman = roman.replace(syb, '')
        return num


n = 3
r = Num().int2Roman(n)
print(n, r)
n = 4
r = Num().int2Roman(n)
print(n, r)
n = 9
r = Num().int2Roman(n)
print(n, r)

n = 58
r = Num().int2Roman(n)
print(n, r)
n = 1994
r = Num().int2Roman(n)
print(n, r)

r = 'MCMXCIV'
n = Num().Roman2int(r)
print(r, n)
r = 'LVIII'
n = Num().Roman2int(r)
print(r, n)
r = 'IX'
n = Num().Roman2int(r)
print(r, n)
r = 'IV'
n = Num().Roman2int(r)
print(r, n)
r = 'III'
n = Num().Roman2int(r)
print(r, n)
