print("=== STUDENT MANAGEMENT SYSTEM ===\n")

class Student:
    def __init__(self, first_name, last_name):
        #Initialize student with first and last name
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []
    
    def get_full_name(self):
        #Return full name
        return self.first_name + " " + self.last_name
    
    def add_grade(self, grade):
        #Add a grade to the student
        self.grades.append(grade)
    
    def calculate_average(self):
        #Calculate average of all grades
        if len(self.grades) == 0:
            return 0
        total = 0
        for grade in self.grades:
            total = total + grade
        return total / len(self.grades)
    
    def display_info(self):
        #Display student information
        print("Student:", self.get_full_name())
        print("Grades:", self.grades)
        print("Average:", self.calculate_average())
        print()

# Create students
print("--- Creating Students ---\n")

student1 = Student("Jason", "Statham")
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)
student1.add_grade(90)
student1.add_grade(88)

student2 = Student("Dwayne", "Johnson")
student2.add_grade(88)
student2.add_grade(95)
student2.add_grade(82)
student2.add_grade(91)
student2.add_grade(87)

student3 = Student("Tom", "Cruise")
student3.add_grade(90)
student3.add_grade(85)
student3.add_grade(88)
student3.add_grade(92)
student3.add_grade(87)

student4 = Student("Scarlett", "Johansson")
student4.add_grade(95)
student4.add_grade(89)
student4.add_grade(93)
student4.add_grade(91)
student4.add_grade(94)

# Display all students
print("--- All Students ---\n")
student1.display_info()
student2.display_info()
student3.display_info()
student4.display_info()

# Find best student
print("--- Finding Best Student ---")
students = [student1, student2, student3, student4]
best_student = students[0]
for student in students:
    if student.calculate_average() > best_student.calculate_average():
        best_student = student

print("Best Student:", best_student.get_full_name())
print("Average:", best_student.calculate_average())

print("\n=== END OF PROGRAM ===")