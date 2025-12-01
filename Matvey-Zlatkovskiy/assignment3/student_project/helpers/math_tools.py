# Helper to perform math calculations

import math
def circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2

def circle_circumference(radius):
    """Calculate the circumference of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * math.pi * radius