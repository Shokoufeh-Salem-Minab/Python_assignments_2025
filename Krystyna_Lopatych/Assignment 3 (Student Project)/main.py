from helpers import math_tools, file_tools
from datetime import datetime
    
r = 5
area = math_tools.circle_area(r)
circum = math_tools.circle_circumference(r)

text = f"[{datetime.now()}] Radius={r}, Area={area:.2f}, Circumference={circum:.2f}"

file_tools.save_to_file("data/results.txt", text)

print("File contents:")
print(file_tools.read_file("data/results.txt"))
