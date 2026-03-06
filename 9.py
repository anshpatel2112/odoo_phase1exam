import math

class Shape:
    def area(self):
        print("Area method of Shape")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


c = Circle(5)
r = Rectangle(4, 6)

print("Area of Circle:", c.area())
print("Area of Rectangle:", r.area())