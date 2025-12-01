"""
Student Gradebook

Interactive program to manage student records and grades.

Features:
* Add students with name and ID
* Add grades to students
* Compute average and pass/fail status
* Display student report
* Save report to a text file
* Handles invalid inputs and limits incorrect attempts

Demonstrates:
* Classes and objects
* Functions and modules
* File handling
* Input validation and simple user interaction
"""

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    # Add a grade to the student
    def add_grade(self, grade):
        self.grades.append(grade)
        
    # Calculate average grade
    def average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0
    
    # Determine pass/fail status
    def status(self):
        return "Passed" if self.average() >= 10 else "Failed"


students = [] # List to hold all student objects

# Search for a student by ID
def find_student(student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None

# Save report to file
def save_report(filename="studentreport.txt"):
    with open(filename, "a") as file:
        for student in students:
            file.write(f"{student.name}, Average: {student.average():.2f}, Status: {student.status()}\n")
    print(f"Report saved to {filename}")

# Main Program and Interface
print("Student Gradebook")
count = 0 # Counter for invalid inputs
save_path = "assignment4/studentreport.txt"
def main():
    while True:
        print("1. Add student")
        print("2. Add grade")
        print("3. Show report")
        print("4. Save & Exit")
        choice = input("Choose an option (1-4): ").strip()

        # Handle user choices
        # Add student
        if choice == "1":
            name = input("Student name: ")
            sid = input("Student ID: ")
            students.append(Student(name, sid))
            print(f"Student {name} added.")
            count = 0
        # Add grade to student
        elif choice == "2":
            sid = input("Enter student ID to add grade: ")
            student = find_student(sid)
            if student:
                try:
                    grade = float(input("Enter grade: "))
                    student.add_grade(grade)
                    print(f"Grade added to {student.name}.")
                except ValueError:
                    print("Invalid grade input.")
            else:
                print("Student not found.")
            count = 0
        # Show report
        elif choice == "3":
            if not students:
                print("No students added yet.")
            else:
                print("=" * 40)
                print("Student Report")
                for s in students:
                    print(f"{s.name} ({s.student_id}) - Average: {s.average():.2f} - Status: {s.status()}")
                print("=" * 40)
                count = 0
        # Save and exit
        elif choice == "4":
            save_report(save_path)
            print("Goodbye!")
            break
        # Incorrect input handling
        else:
            print("Invalid choice. Please select 1-4.")
            count += 1
            if count >= 5:
                print("Limit exceeded, terminating session.")
                save_report(save_path)
                break

if __name__ == "__main__":
    main()
