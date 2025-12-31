def process_students(students):
    

    with open("results.txt", "w") as file:
        for name, grades in students.items():
            average = sum(grades) / len(grades)

            line = f"Student: {name}, Grades: {grades}, Average: {average:.2f}\n"
            file.write(line)

            print(line.strip())



students_data = {
    "Ivan Doska": [85, 90, 78],
    "Anna Petrova": [92, 88, 95],
    "Mark Smith": [70, 75, 80]
}

process_students(students_data)
