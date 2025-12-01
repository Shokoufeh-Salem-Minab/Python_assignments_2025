student_name = "John Marston"
student_id = "JM12345"
grades = [10, 11, 12]

print("Student name:", student_name)
print("Student id:", student_id)
print("Grades:", grades)

average = sum(grades) / len(grades)
print("Average:", average)

if average >= 10:
    print("Passed")
else:
    print("Failed")

students = {
    "JM12345": {"name": "John Marston", "grades": [10, 11, 12]},
    "AB12346": {"name": "Alice Brown", "grades": [18, 16, 17]}
}

print("\n All students:")
for student_id, info in students.items():
    print(f"id: {student_id}, Name: {info['name']}, Grades: {info['grades']}")

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def status(self):
        if self.average() >= 10:
            return "Passed"
        else:
            return "Failed"

def save_report(students_dict, filename="student_report.txt"):
    with open(filename, "w") as f:
        for student_id, info in students_dict.items():
            avg = sum(info["grades"]) / len(info["grades"])
            status = "Passed" if avg >= 10 else "Failed"
            f.write(f"{info['name']}, {avg:.2f}, {status}\n")
    print("Report saved to", filename)

students_dict = {}

while True:
    print("\n 1. Add student")
    print("2. Add grade")
    print("3. Show report")
    print("4. Save & Exit")
    
    choice = input("Choose option 1-4: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        student_id = input("Enter student id: ")
        students_dict[student_id] = {"name": name, "grades": []}
        
    elif choice == "2":
        student_id = input("Enter student id: ")
        if student_id in students_dict:
            grade = float(input("Enter grade: "))
            students_dict[student_id]["grades"].append(grade)
        else:
            print("Student not found!")
            
    elif choice == "3":
        for student_id, info in students_dict.items():
            avg = sum(info["grades"]) / len(info["grades"]) if info["grades"] else 0
            status = "Passed" if avg >= 10 else "Failed"
            print(f"Name: {info['name']}, Average: {avg:.2f}, Status: {status}")
            
    elif choice == "4":
        save_report(students_dict)
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
