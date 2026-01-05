# student_grades.py
# Writes results.txt in the same folder as this script

import os

def process_student(name, grades):
    average = sum(grades) / len(grades)

    # Get the directory of this Python file
    folder = os.path.dirname(__file__)
    file_path = os.path.join(folder, "results.txt")

    with open(file_path, "w") as file:
        file.write(f"Student Name: {name}\n")
        file.write(f"Grades: {grades}\n")
        file.write(f"Average Grade: {average:.2f}\n")


def main():
    student_name = "Yangli Deng"
    student_grades = [80, 85, 90]

    process_student(student_name, student_grades)
    print("Results saved to results.txt")


if __name__ == "__main__":
    main()
