def processStudents(students):
    file = open("assignment7/student_results.txt", "w")
    for student in students:
        firstName = student[0]
        lastName = student[1]
        grades = student[2]
        fullName = firstName + " " + lastName
        avg = sum(grades) / len(grades)
        resultText = fullName + ": " + str(grades) + "\nAverage: " + str(round(avg, 2))
        file.write(resultText + "\n")
        print(resultText, "\n")
    file.close()

studentsData = [
    ("Patriks", "Krastins", [8, 9, 7, 10]),
    ("Someone", "Smith", [10, 9, 8, 9]),
    ("Dita", "Doe", [7, 6, 8, 7])
]

processStudents(studentsData)