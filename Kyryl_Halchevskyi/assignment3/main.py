import os
import datetime
import random

import student_utils

print("=== STUDENT MANAGEMENT SYSTEM ===\n")

# Create directory structure
print("--- Setting up directories ---")
if not os.path.exists("data"):
    os.mkdir("data")
    print("Created 'data' directory")
else:
    print("'data' directory already exists")

if not os.path.exists("reports"):
    os.mkdir("reports")
    print("Created 'reports' directory")
else:
    print("'reports' directory already exists")

# Check if student file exists, if not create it
if not os.path.exists("data/students.txt"):
    with open("data/students.txt", "w") as file:
        pass
    print("Created 'students.txt' file")

# Add some students
print("\n--- Adding Students ---")
student_utils.add_student("101", "Micheal Jordan", "85")
student_utils.add_student("102", "Ema Watson", "92")
student_utils.add_student("103", "Jason Statham", "78")
student_utils.add_student("104", "John Dear", "88")

# View all students
student_utils.view_all_students()

# Search for a student
print("\n--- Searching for Student ---")
student_utils.search_student("102")

# Calculate average grade
student_utils.calculate_average()

# Use random library to pick a random student
print("\n--- Random Student Selection ---")
with open("data/students.txt", "r") as file:
    lines = file.readlines()
    if len(lines) > 0:
        random_line = random.choice(lines)
        sid, name, grade = random_line.strip().split(",")
        print(f"Randomly selected: {name} (ID: {sid})")

# Use datetime library
print("\n--- System Information ---")
current_time = datetime.datetime.now()
print(f"Current Date & Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

# List files in data directory
print("\n--- Files in 'data' directory ---")
files = os.listdir("data")
for file in files:
    print(f"- {file}")

# Generate report
print("\n--- Generating Report ---")
student_utils.save_report()

# Check if report was created
print("\n--- Files in 'reports' directory ---")
report_files = os.listdir("reports")
for file in report_files:
    print(f"- {file}")

print("\n=== END OF PROGRAM ===")
