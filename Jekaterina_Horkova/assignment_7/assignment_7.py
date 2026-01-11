def process_students(students):
    with open("students_results.txt", "w") as file:
        file.write("*================*\n")
        file.write("Student Results\n")
        file.write("*================*\n")

        for student in students:
            name = student["name"]
            grades = student["grades"]
            average = sum(grades) / len(grades)

            file.write(f"Name: {name}\n")
            file.write(f"Grades: {grades}\n")
            file.write(f"Average: {average:.2f}\n")
            file.write("\n")


students_data = [
    {"name": "Angel", "grades": [20, 20, 10]},
    {"name": "Charlie", "grades": [30, 75, 80]},
    {"name": "Has", "grades": [75, 80, 9]},
]

process_students(students_data)
