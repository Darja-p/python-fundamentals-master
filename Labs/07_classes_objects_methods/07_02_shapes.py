'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math
from _decimal import getcontext, Decimal
getcontext().prec = 4
pi = Decimal(math.pi)

class Rectangle():
    """creating class rectabgle"""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"this is a rectangle with a width {self.width} and length {self.length}"

    def area(self):
        """method to calculate area"""
        area = self.length * self.width
        return area

    def perim(self):
        """method to calculate perimeter"""
        perim = self.width * self.length * 2
        return perim


class Circle():
    """creating calss circle"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """method to calculate are of the circle"""
        area = pi * self.radius ** 2
        return area

    def __str__(self):
        return f"this is circle with {self.radius} radius"

    def circum(self):
        """method to calculate circumference of the circle"""
        circum = self.radius * 2 * pi
        return circum


d = Rectangle(3, 5)
print(d)
print(f" area is {d.area()} and perimeter is {d.perim()}")

p = Circle(4)
print(p)
print(f"area of the circle is {p.area()}")
print(p.circum())