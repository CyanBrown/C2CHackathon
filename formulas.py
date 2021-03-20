import math
from trigFuncs import *

class CircleSphere:
    def __init__(self, radius):
        self.circumference = 2 * math.pi * radius
        self.area = math.pi * (radius ** 2)
        self.surface_area = 4 * math.pi * (radius ** 2)
        self.volume = (4 / 3) * math.pi * (radius ** 3)

    def __str__(self):
        return f"\nCircumference: {self.circumference}\nArea: {self.area}\nSurface Area: {self.surface_area}\nVolume: {self.volume}\n"


class SquareRect:
    def __init__(self, side1, side2):
        self.perimeter = 2 * (side1 + side2)
        self.area = side1 * side2

    def __str__(self):
        return f"\nPerimeter: {self.perimeter}\nArea: {self.area}"


class CubeRect:
    def __init__(self, length, width, height):
        l=length
        w = width
        h = height
        self.volume = l * w * h
        self.surface_area = ((l * h) * 4) + (h * w) * 2

    def __str__(self):
        return f"\nSurface Area: {self.surface_area}\nVolume: {self.volume}\n"

class Trapezoid:
    def __init__(self, base1, base2, height):
        self.area = ((base1 + base2) / 2) * height

    def __str__(self):
        return f"\nArea: {self.area}\n"

class Cone:
    def __init__(self, radius, height):
        self.surface_area = math.pi * radius * height
        self.volume = (1 / 3) * math.pi * (radius ** 2) * height

    def __str__(self):
        return f"\nSurface Area: {self.surface_area}\nVolume: {self.volume}\n"
class Cylinder:
    def __init__(self, radius, height):
        self.surface_area = 2 * math.pi * radius * height + (2 * math.pi * (radius ** 2))
        self.volume = math.pi * (radius ** 2) * height

    def __str__(self):
        return f"\nSurface Area: {self.surface_area}\nVolume: {self.volume}\n"

class NthPolygon:
    def __init__(self, side_length, side_count):
        self.perimeter = side_length * side_count
        self.area = self.perimeter * .5 * (side_length / (2 * math.tan(math.radians(180 / side_count))))

    def __str__(self):
        return f"\nPerimeter: {self.perimeter}\nArea: {self.area}\n"


# class Triangle:
#     def __init__(self, measure, base=None, height=None, A=None, B=None, C=None, a=None, b=None, c=None):
#         self.error_code = "valid"

#         self.base = base
#         self.height = height

#         self.angles = [A,B,C]
#         self.sides = [a,b,c]

#         angle_size = 0

#         for ang in range(len(self.angles)):
#             if self.angles[ang] is not None:
#                 angle_size+=self.angles[ang]

#         if angle_size >= 180:
#             if self.angles.count(None)>=1:
#                 self.error_code = "invalid"
#                 return

#             elif angle_size>180:
#                 self.error_code  = "invalid"
#                 return

#         if self.angles.count(None) == 1:
#             idx = self.angles.index(None)
#             l = self.angles.copy()
#             l.remove(None)
#             self.angles[idx] = 180 - math.fsum(l)

#         if base and height:
#             self.area = base*height*.5

#         working_idx = 0

#         for i in range(3):
#             if self.angles[i] and self.sides[i]:
#                 working_idx = i
#                 break

#         if 90 in [A,B,C]:
#             pass

#         wside = self.sides[working_idx]
#         wangle = self.angles[working_idx]

#         self.angles.pop(working_idx)
#         self.sides.pop(working_idx)

#         los_const = sin(wangle,measure)/wside

#         for _ in range(3):
#             for i in range(2):
#                 if self.angles[i] and self.sides[i] is None:
#                     self.sides[i] = sin(self.angles[i],measure)/los_const

#                 elif self.angles[i] is None and self.sides[i]:
#                     self.angles[i] = arcsin((los_const*self.sides[i]), measure)

#             if self.angles.count(None) ==1:
#                 idx = [0,1].remove(self.angles.index(None))
#                 self.angles[self.angles.index(None)] = 180-wangle-self.angles[idx[0]]

#         self.angles.insert(working_idx,wangle)
#         self.sides.insert(working_idx, wside)

#         self.A = self.angles[0]
#         self.B = self.angles[1]
#         self.C = self.angles[2]
#         self.a = self.sides[0]
#         self.b = self.sides[1]
#         self.c = self.sides[2]



