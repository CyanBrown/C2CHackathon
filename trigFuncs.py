import math


def sin(angle, measure):
    if measure == "deg":
        return math.sin(math.radians(angle))

    elif measure == "rad":
        return math.sin(angle)


def cos(angle, measure):
    if measure == "deg":
        return math.cos(math.radians(angle))

    elif measure == "rad":
        return math.cos(angle)


def tan(angle, measure):
    if measure == "deg":
        return math.tan(math.radians(angle))

    elif measure == "rad":
        return math.tan(angle)


def arcsin(l, measure):
    if measure == "deg":
        return math.degrees(math.asin(l))

    elif measure == "rad":
        return math.asin(l)


def arccos(l, measure):
    if measure == "deg":
        return math.degrees(math.acos(l))

    elif measure == "rad":
        return math.acos(l)


def arctan(l, measure):
    if measure == "deg":
        return math.degrees(math.atan(l))

    elif measure == "rad":
        return math.atan(l)
