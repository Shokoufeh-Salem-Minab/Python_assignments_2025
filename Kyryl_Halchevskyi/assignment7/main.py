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

def process_students(students_data):
    # Takes students information, assigns grades, calculates average, and writes results to a file
    students = []
    
    # Create student objects and add grades
    for student_info in students_data:
        first_name = student_info["first_name"]
        last_name = student_info["last_name"]
        grades = student_info["grades"]
        
        student = Student(first_name, last_name)
        
        for grade in grades:
            student.add_grade(grade)
        
        students.append(student)
    
    # Write results to file
    with open("student_results.txt", "w") as file:
        file.write("=== STUDENT GRADE REPORT ===\n\n")
        
        for student in students:
            file.write(f"Student: {student.get_full_name()}\n")
            file.write(f"Grades: {student.grades}\n")
            file.write(f"Average: {student.calculate_average():.2f}\n")
            file.write("-" * 40 + "\n")
    
    print("Results written to 'student_results.txt'")
    
    # Display results on screen
    print("\n=== STUDENT GRADE REPORT ===\n")
    for student in students:
        print(f"Student: {student.get_full_name()}")
        print(f"Grades: {student.grades}")
        print(f"Average: {student.calculate_average():.2f}")
        print("-" * 40)

# Main program
print("=== STUDENT GRADE MANAGEMENT ===\n")

# Student data
students_data = [
    {
        "first_name": "Jason",
        "last_name": "Statham",
        "grades": [85, 92, 78, 90, 88]
    },
    {
        "first_name": "Dwayne",
        "last_name": "Johnson",
        "grades": [88, 95, 82, 91, 87]
    },
    {
        "first_name": "Tom",
        "last_name": "Cruise",
        "grades": [90, 85, 88, 92, 87]
    },
    {
        "first_name": "Scarlett",
        "last_name": "Johansson",
        "grades": [95, 89, 93, 91, 94]
    }
]

# Process all students
process_students(students_data)

print("\n=== END OF PROGRAM ===")