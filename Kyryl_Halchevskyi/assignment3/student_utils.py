def add_student(student_id, name, grade):
    """Add a student to the file"""
    with open("data/students.txt", "a") as file:
        file.write(f"{student_id},{name},{grade}\n")
    print(f"Student '{name}' added successfully!")

def view_all_students():
    """Read and display all students"""
    try:
        with open("data/students.txt", "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No students found!")
            else:
                print("\n--- All Students ---")
                for line in lines:
                    student_id, name, grade = line.strip().split(",")
                    print(f"ID: {student_id} | Name: {name} | Grade: {grade}")
    except FileNotFoundError:
        print("No student records found!")

def search_student(student_id):
    """Search for a student by ID"""
    try:
        with open("data/students.txt", "r") as file:
            lines = file.readlines()
            found = False
            for line in lines:
                sid, name, grade = line.strip().split(",")
                if sid == student_id:
                    print(f"\nStudent Found!")
                    print(f"ID: {sid} | Name: {name} | Grade: {grade}")
                    found = True
                    break
            if not found:
                print(f"Student with ID '{student_id}' not found!")
    except FileNotFoundError:
        print("No student records found!")

def calculate_average():
    """Calculate average grade of all students"""
    try:
        with open("data/students.txt", "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No students to calculate average!")
                return
            
            total = 0
            count = 0
            for line in lines:
                student_id, name, grade = line.strip().split(",")
                total = total + int(grade)
                count = count + 1
            
            average = total / count
            print(f"\nAverage Grade: {average:.2f}")
    except FileNotFoundError:
        print("No student records found!")

def save_report():
    """Generate a report file"""
    try:
        with open("data/students.txt", "r") as file:
            lines = file.readlines()
        
        with open("reports/student_report.txt", "w") as report:
            report.write("=== STUDENT REPORT ===\n\n")
            report.write(f"Total Students: {len(lines)}\n\n")
            
            total = 0
            for line in lines:
                student_id, name, grade = line.strip().split(",")
                report.write(f"ID: {student_id} | Name: {name} | Grade: {grade}\n")
                total = total + int(grade)
            
            if len(lines) > 0:
                average = total / len(lines)
                report.write(f"\nAverage Grade: {average:.2f}\n")
        
        print("Report saved to reports/student_report.txt")
    except FileNotFoundError:
        print("No student records found!")
