
from helpers import math_tools, file_tools
from datetime import datetime
import random
import os

def demonstrate_circle_calculations():
    print("=" * 50)
    print("CIRCLE CALCULATIONS")
    print("=" * 50)
    
    # Generate random radii
    radii = [random.uniform(1, 10) for _ in range(3)]
    
    for i, radius in enumerate(radii, 1):
        area = math_tools.circle_area(radius)
        circumference = math_tools.circle_circumference(radius)
        
        print(f"Circle {i}:")
        print(f"  Radius: {radius:.2f}")
        print(f"  Area: {area:.2f}")
        print(f"  Circumference: {circumference:.2f}")
        
        # Save to file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result_text = f"[{timestamp}] Circle {i}: Radius={radius:.2f}, Area={area:.2f}, Circumference={circumference:.2f}"
        file_tools.save_to_file("data/results.txt", result_text)

def demonstrate_rectangle_calculations():
    print("\n" + "=" * 50)
    print("RECTANGLE CALCULATIONS")
    print("=" * 50)
    
    rectangles = [
        (5, 3),
        (7.5, 4.2),
        (10, 6)
    ]
    
    for i, (length, width) in enumerate(rectangles, 1):
        area = math_tools.rectangle_area(length, width)
        perimeter = math_tools.rectangle_perimeter(length, width)
        
        print(f"Rectangle {i}:")
        print(f"  Length: {length}, Width: {width}")
        print(f"  Area: {area:.2f}")
        print(f"  Perimeter: {perimeter:.2f}")
        
        # Save to file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result_text = f"[{timestamp}] Rectangle {i}: Length={length}, Width={width}, Area={area:.2f}, Perimeter={perimeter:.2f}"
        file_tools.save_to_file("data/results.txt", result_text)

def demonstrate_triangle_calculations():
    print("\n" + "=" * 50)
    print("TRIANGLE CALCULATIONS")
    print("=" * 50)
    
    triangles = [
        (6, 4),
        (8.5, 5.2),
        (12, 7)
    ]
    
    for i, (base, height) in enumerate(triangles, 1):
        area = math_tools.triangle_area(base, height)
        
        print(f"Triangle {i}:")
        print(f"  Base: {base}, Height: {height}")
        print(f"  Area: {area:.2f}")
        
        # Save to file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result_text = f"[{timestamp}] Triangle {i}: Base={base}, Height={height}, Area={area:.2f}"
        file_tools.save_to_file("data/results.txt", result_text)

def display_file_information():
    print("\n" + "=" * 50)
    print("FILE INFORMATION")
    print("=" * 50)
    
    stats = file_tools.get_file_stats("data/results.txt")
    print(f"File exists: {stats['exists']}")
    print(f"File size: {stats['size_bytes']} bytes")
    
    print("\nFILE CONTENTS:")
    print("-" * 30)
    contents = file_tools.read_file("data/results.txt")
    print(contents)

def main():
    print("STUDENT PROJECT: GEOMETRY CALCULATOR")
    print("Built-in libraries: datetime, random, os")
    print("Custom modules: math_tools, file_tools")
    print("File operations: Reading/Writing to data/results.txt")
    
    # file_tools.clear_file("data/results.txt")
    
    # Perform various calculations
    demonstrate_circle_calculations()
    demonstrate_rectangle_calculations()
    demonstrate_triangle_calculations()
    
    # Display file information
    display_file_information()
    
    print("\n" + "=" * 50)
    print("PROJECT COMPLETED SUCCESSFULLY!")
    print("=" * 50)

if __name__ == "__main__":
    main()