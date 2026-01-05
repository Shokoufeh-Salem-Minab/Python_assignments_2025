#Marks Idermans
#mi24027

#I used assign 6 for a few functional parts here

import os

def get_name(prompt):
    #user input
    return input(prompt).strip()

def get_student_grades():
    #grades from user
    grades = []
    while True:
        grade_input = input("Enter a grade (or type 'done' to finish): ")
        if grade_input.lower() == "done":
            break
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Please enter a valid grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return grades

def calculate_average(grades):
    #average of grades
    return sum(grades) / len(grades) if grades else 0

def save_results_to_file(students, filename="student_results.txt"):
    #grades and averages to file
    with open(filename, "w") as file:
        for student in students:
            name = student["name"]
            grades = student["grades"]
            avg = student["average"]
            grades_str = ", ".join(f"{g:.2f}" for g in grades)
            file.write(f"Student: {name}\nGrades: {grades_str}\nAverage: {avg:.2f}\n\n")
    print(f"\nResults saved to {filename}")

def main():
    
    #User login
    user_name = get_name("Enter your full name: ")
    
    students = []
    
    while True:
        #student name
        student_name = get_name("Enter the student's full name: ")

        #validating acces eligibility
        if user_name.lower() == student_name.lower():
            print("Access Denied. You cannot enter grades for yourself.")
            exit()

        #Enter grades
        grades = get_student_grades()
        avg = calculate_average(grades)

        #store student data
        students.append({
            "name": student_name,
            "grades": grades,
            "average": avg
        })

        #add another student
        cont = input("Add another student? (yes/no): ").strip().lower()
        if cont != "yes":
            break

    #results to file
    save_results_to_file(students)
    print("Saved to:", os.path.abspath("student_results.txt"))

if __name__ == "__main__":
    main()
