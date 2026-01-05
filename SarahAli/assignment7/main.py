import os

# File will be created in the same folder as this file
FILE = os.path.join(os.path.dirname(__file__), "student_results.txt")

# Function to get student information and grades
def get_student_info():
    student = {}
    student["name"] = input("Enter student name: ")

    grades = []
    n = int(input("How many grades? "))
    for i in range(n):
        grade = float(input("Enter grade: "))
        grades.append(grade)

    student["grades"] = grades
    return student

# Function to calculate average
def calculate_average(grades):
    total = 0
    for g in grades:
        total += g
    return total / len(grades)

# Function to write results to a file
def write_results_to_file(student):
    with open(FILE, "a") as file:
        file.write("\nStudent Name: " + student["name"] + "\n")
        file.write("Grades: " + str(student["grades"]) + "\n")
        file.write("Average: " + str(calculate_average(student["grades"])) + "\n")

    print("Results written to", FILE)

# Main program
student = get_student_info()
write_results_to_file(student)
