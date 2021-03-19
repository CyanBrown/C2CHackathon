import math

def circumference_circle(radius):
    return 2*math.pi*radius

def area_circle(radius):
    return math.pi*(radius**2)

def surface_area_sphere(radius):
    return 4*math.pi*(radius**2)

def volume_sphere(radius):
    return (4/3)*math.pi*(radius**3)

def perimeter_square_or_rect(side1,side2):
    return 2*(side1+side2)

def area_square_or_rect(side1,side2):
    return side1*side2

#TODO: add surface area and volume cube and rectangular prism

def area_triangle(base, height):
    return .5*base*height

def area_trapezoid(base1,base2,height):
    return .5*(base1+base2)*height

def surface_area_cone(radius,height):
    return math.pi*radius*height

def volume_cone(radius, height):
    return (1/3)*math.pi*(radius**2)*height

def surface_area_cylinder(radius, height):
    return 2*math.pi*radius*height+(2*math.pi*(radius**2))

def volume_cylinder(radius, height):
    return math.pi*(radius**2)*height

def perimeter_nth_polygon(side_length, side_count):
    return side_length*side_count

def area_nth_polygon(apothem, side, side_count):
    return perimeter_nth_polygon(side, side_count)*.5*apothem

#TODO: maybe add non-apothem way of calculating area


