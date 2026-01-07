class Student:
    """Represents a student with their information and grades."""
    
    def __init__(self, student_id, name, age):
        """
        Initialize a student with basic information.
        
        Args:
            student_id (int): Unique identifier for the student
            name (str): Student's full name
            age (int): Student's age
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, grade):
        """
        Add a single grade to the student's record.
        
        Args:
            grade (float): Grade to add (1-10)
        """
        if 1 <= grade <= 10:
            self.grades.append(grade)
        else:
            print(f"Warning: Grade {grade} is out of range (1-10). Not added.")
    
    def add_grades(self, grades_list):
        """
        Add multiple grades to the student's record.
        
        Args:
            grades_list (list): List of grades to add
        """
        for grade in grades_list:
            self.add_grade(grade)
    
    def calculate_average(self):
        """
        Calculate the average of all grades.
        
        Returns:
            float: Average grade, or 0 if no grades exist
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self):
        """
        Get letter grade based on average (1-10 scale).
        
        Returns:
            str: Letter grade (A, B, C, D, or F)
        """
        average = self.calculate_average()
        if average >= 9:
            return 'A'
        elif average >= 7:
            return 'B'
        elif average >= 5:
            return 'C'
        elif average >= 3:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        """String representation of the student."""
        return f"Student(ID: {self.student_id}, Name: {self.name}, Age: {self.age})"


class GradeManager:
    """Manages multiple students and their grade records."""
    
    def __init__(self):
        """Initialize the grade manager with an empty student list."""
        self.students = []
    
    def add_student(self, student):
        """
        Add a student to the manager.
        
        Args:
            student (Student): Student object to add
        """
        self.students.append(student)
    
    def create_student(self, student_id, name, age):
        """
        Create and add a new student.
        
        Args:
            student_id (int): Unique identifier for the student
            name (str): Student's full name
            age (int): Student's age
            
        Returns:
            Student: The newly created student object
        """
        student = Student(student_id, name, age)
        self.add_student(student)
        return student
    
    def find_student(self, student_id):
        """
        Find a student by their ID.
        
        Args:
            student_id (int): ID of the student to find
            
        Returns:
            Student: Student object if found, None otherwise
        """
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def write_results_to_file(self, filename="grades_report.txt"):
        """
        Write all student results to a file.
        
        Args:
            filename (str): Name of the output file
        """
        try:
            with open(filename, 'w') as file:
                file.write("=" * 70 + "\n")
                file.write("STUDENT GRADES REPORT\n")
                file.write("=" * 70 + "\n\n")
                
                for student in self.students:
                    file.write(f"Student ID: {student.student_id}\n")
                    file.write(f"Name: {student.name}\n")
                    file.write(f"Age: {student.age}\n")
                    file.write(f"Grades: {student.grades}\n")
                    file.write(f"Average Grade: {student.calculate_average():.2f}\n")
                    file.write(f"Letter Grade: {student.get_letter_grade()}\n")
                    file.write("-" * 70 + "\n\n")
                
                file.write("=" * 70 + "\n")
                file.write("END OF REPORT\n")
                file.write("=" * 70 + "\n")
            
            print(f"Results successfully written to {filename}")
        
        except Exception as e:
            print(f"Error writing to file: {e}")
    
    def display_summary(self):
        """Display a summary of all students to the console."""
        print("\n" + "=" * 70)
        print("STUDENT GRADES SUMMARY")
        print("=" * 70)
        
        for student in self.students:
            print(f"\n{student}")
            print(f"  Grades: {student.grades}")
            print(f"  Average: {student.calculate_average():.2f}")
            print(f"  Letter Grade: {student.get_letter_grade()}")
        
        print("\n" + "=" * 70 + "\n")


def main():
    """Main function to demonstrate the student grade management system."""
    
    # Create a grade manager
    manager = GradeManager()
    
    # Create students and assign grades
    student1 = manager.create_student(101, "Alice Johnson", 20)
    student1.add_grades([8.5, 9.2, 8.8, 9.0, 8.7])
    
    student2 = manager.create_student(102, "Bob Smith", 21)
    student2.add_grades([7.8, 8.2, 7.5, 8.0, 7.9])
    
    student3 = manager.create_student(103, "Carol Williams", 19)
    student3.add_grades([9.5, 9.8, 9.2, 9.6, 9.4])
    
    student4 = manager.create_student(104, "David Brown", 22)
    student4.add_grades([6.5, 7.0, 6.8, 7.2, 6.9])
    
    student5 = manager.create_student(105, "Emma Davis", 20)
    student5.add_grades([4.5, 5.0, 4.8, 5.2, 4.9])
    
    # Display summary to console
    manager.display_summary()
    
    # Write results to file
    manager.write_results_to_file("grades_report.txt")
    
    print("Program completed successfully!")


if __name__ == "__main__":
    main()