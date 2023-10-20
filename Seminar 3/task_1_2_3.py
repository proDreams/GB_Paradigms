import math


# Task 1
class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass


# Task 2
class Circle(Shape):
    def __init__(self, r):
        self._radius = r
        self.pi = math.pi

    def get_area(self):
        return self.pi * self._radius ** 2

    def get_perimeter(self):
        return 2 * (self.pi * self._radius)

    def get_radius(self):
        return self._radius

    @property
    def radius1(self):
        return self._radius

    @radius1.setter
    def radius1(self, value):
        self._radius = value


# Task 3
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        return (self.a * self.b) / 2

    def get_perimeter(self):
        return self.a + self.b + self.c
