import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "results.txt") # ensure file is in same folder

def process_students():
    students = {}
    n = int(input("Number of students: "))
    for _ in range(n):
        name = input("Student name: ")
        grades = list(map(float, input("Enter grades separated by space: ").split()))
        students[name] = grades

    with open(file_path, "w") as file:
        for name, grades in students.items():
            avg = sum(grades) / len(grades)
            file.write(f"{name} | Grades: {grades} | Average: {avg:.2f}\n")

process_students()

