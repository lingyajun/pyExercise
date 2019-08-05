class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


s = Rectangle(3,4).area()
print(s)
s = Rectangle(55,4).area()
print(s)

from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        s =  (self.radius ** 2) * pi
        return s

    def perimeter(self):
        l =  self.radius * 2 * pi
        return l

r = 1
circle = Circle(r)
print(r, circle.area(), circle.perimeter())

