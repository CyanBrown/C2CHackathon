import math


class CircleSphere:
    def __init__(self, radius):
        self.circumference = 2 * math.pi * radius
        self.area = math.pi * (radius ** 2)
        self.surface_area = 4 * math.pi * (radius ** 2)
        self.volume = (4 / 3) * math.pi * (radius ** 3)


class SquareRect:
    def __init__(self, side1, side2):
        self.perimeter = 2 * (side1 + side2)
        self.area = side1 * side2


class CubeRect:
    def __init__(self, l, w, h):
        self.volume = l * w * h
        self.surface_area = ((l * h) * 4) + (h * w) * 2


class Trapezoid:
    def __init__(self, base1, base2, height):
        self.area = ((base1 + base2) / 2) * height


class Cone:
    def __init__(self, radius, height):
        self.surface_area = math.pi * radius * height
        self.volume = (1 / 3) * math.pi * (radius ** 2) * height


class Cylinder:
    def __init__(self, radius, height):
        self.surface_area = 2 * math.pi * radius * height + (2 * math.pi * (radius ** 2))
        self.volume = math.pi * (radius ** 2) * height


class NthPolygon:
    def __init__(self, side_length, side_count):
        self.perimeter = side_length * side_count
        self.area = self.perimeter * .5 * (side_length / (2 * math.tan(math.radians(180 / side_count))))


class Triangle:
    def __init__(self, base=None, height=None, A=None, B=None, C=None, a=None, b=None, c=None):
        self.base = base
        self.height = height
        self.A = A
        self.B = B
        self.C = C
        self.a = a
        self.b = b
        self.c = c
