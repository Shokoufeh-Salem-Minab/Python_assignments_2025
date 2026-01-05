
import math

def circle_area(radius):
    """Calculate the area of a circle"""
    return math.pi * radius ** 2

def circle_circumference(radius):
    """Calculate the circumference of a circle"""
    return 2 * math.pi * radius

def rectangle_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

def rectangle_perimeter(length, width):
    """Calculate the perimeter of a rectangle"""
    return 2 * (length + width)

def triangle_area(base, height):
    """Calculate the area of a triangle"""
    return 0.5 * base * height