"""
Circle Computation & Logging

Interactive program to compute circle properties for a given radius.

Features:
* Compute area and circumference
* Log results with timestamp (API or local time) to a text file
* Allows repeated computations with input validation

Demonstrates:
* Functions and modules
* Working with files
* API requests and fallback to local time
"""

from helpers import math_tools, file_tools
import requests
from datetime import datetime

answer = 'y'

while answer.lower() == 'y':
    # Compute circle properties
    r = int(input("Enter the radius of the circle: "))
    area = math_tools.circle_area(r)
    circum = math_tools.circle_circumference(r)

    # Try fetching real-time data from API
    try:
        response = requests.get("http://worldtimeapi.org/api/ip", timeout=5)
        response.raise_for_status()
        data = response.json()
        current_time = data.get("datetime", "Time not available")[:19]  # YYYY-MM-DD HH:MM:SS
    except Exception:
        current_time = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (API unavailable)"

    # Prepare and save text
    text = f"[{current_time}] Circle with radius {r} | Area: {area:.2f} | Circumference: {circum:.2f}\n"
    file_tools.save_to_file("assignment3/student_project/data/results.txt", text)

    # Show clean output
    print("Computation complete! File contents:")
    print(text.strip())

    # Restart prompt with validation
    answer = input("Would you like to compute another circle? (y/n): ").strip().lower()
    while answer not in ['y', 'n']:
        answer = input("Please enter 'y' to continue or 'n' to quit: ").strip().lower()