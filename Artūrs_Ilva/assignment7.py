def process_students():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input(f"\nEnter name of student {i + 1}: ")
        grades_input = input("Enter grades separated by spaces: ")

        grades = list(map(float, grades_input.split()))
        average = sum(grades) / len(grades)

        students.append({
            "name": name,
            "grades": grades,
            "average": average
        })

    with open("results.txt", "w") as file:
        for student in students:
            file.write(f"Name: {student['name']}\n")
            file.write(f"Grades: {student['grades']}\n")
            file.write(f"Average: {student['average']:.2f}\n")
            file.write("-" * 30 + "\n")

    print("\nResults saved to results.txt")

process_students()
