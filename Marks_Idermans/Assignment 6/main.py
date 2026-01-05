#Marks Idermans
#mi24027

#I made a fun spin on this one, please try to type in the your name and the students name the same

grades = []

#get names
def get_name(prompt):
    return input(prompt).strip()

#add a grade
def add_grade(grade):
    grades.append(grade)

#compute average
def compute_average():
    return sum(grades) / len(grades) if grades else 0

#User login
user_name = get_name("Enter your full name: ")

#student's name
student_name = get_name("Enter the student's full name: ")

#validating acces eligibility
if user_name.lower() == student_name.lower():
    print("Access Denied. You cannot access your own record.")
    exit()

#grade entry
print(f"Welcome! You can now enter grades for {student_name}.")

while True:
    grade_input = input("Enter a grade (or type 'done' to finish): ")
    if grade_input.lower() == "done":
        break
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
            add_grade(grade)
        else:
            print("Please enter a valid grade between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

#results
print(f"\nStudent: {student_name}")
print(f"Grades: {grades}")
print(f"Average Grade: {compute_average():.2f}")
