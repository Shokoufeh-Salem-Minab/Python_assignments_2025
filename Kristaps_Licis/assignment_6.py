import statistics

print("="*70)
print("COMPARING FUNCTIONAL, FUNCTION-BASED, AND OOP APPROACHES")
print("="*70)

# TASK 1: GENERATE A PERSON'S FULL NAME

print("\n" + "-"*70)
print("TASK 1: GENERATE A PERSON'S FULL NAME")
print("-"*70)

# APPROACH 1: FUNCTIONAL (Direct/Inline)
print("\n[APPROACH 1: FUNCTIONAL]")
first_name_1 = "Jānis"
last_name_1 = "Bērziņš"
full_name_1 = first_name_1 + " " + last_name_1
print(f"Full Name: {full_name_1}")

# APPROACH 2: FUNCTION-BASED
print("\n[APPROACH 2: FUNCTION-BASED]")

def get_full_name(first, last):
    """Return full name by combining first and last name."""
    return f"{first} {last}"

full_name_2 = get_full_name("Ilze", "Gaļitskaja")
print(f"Full Name: {full_name_2}")

# APPROACH 3: OOP (Object-Oriented Programming)
print("\n[APPROACH 3: OOP]")

class Person:
    """Class representing a person with first and last name."""
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_full_name(self):
        """Return full name."""
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.get_full_name()

person = Person("Andris", "Kalniņš")
print(f"Full Name: {person.get_full_name()}")

# TASK 2: STORE STUDENT GRADES AND COMPUTE AVERAGE

print("\n" + "-"*70)
print("TASK 2: STORE STUDENT GRADES AND COMPUTE AVERAGE")
print("-"*70)

# APPROACH 1: FUNCTIONAL (Direct/Inline)
print("\n[APPROACH 1: FUNCTIONAL]")
grades_1 = [85, 90, 78, 92, 88]
average_1 = sum(grades_1) / len(grades_1)
print(f"Grades: {grades_1}")
print(f"Average: {average_1:.2f}")

# APPROACH 2: FUNCTION-BASED
print("\n[APPROACH 2: FUNCTION-BASED]")

def calculate_average(grades):
    """Calculate average of grades."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def add_grade(grades, grade):
    """Add a grade to the list."""
    grades.append(grade)
    return grades

def get_statistics(grades):
    """Get statistics for grades."""
    if not grades:
        return None
    return {
        'average': calculate_average(grades),
        'min': min(grades),
        'max': max(grades),
        'median': statistics.median(grades)
    }

grades_2 = [88, 91, 85, 89, 93]
print(f"Grades: {grades_2}")
print(f"Average: {calculate_average(grades_2):.2f}")

add_grade(grades_2, 95)
print(f"After adding grade 95: {grades_2}")
print(f"New Average: {calculate_average(grades_2):.2f}")

stats = get_statistics(grades_2)
print(f"Statistics: Min={stats['min']}, Max={stats['max']}, Median={stats['median']}")

# APPROACH 3: OOP (Object-Oriented Programming)
print("\n[APPROACH 3: OOP]")

class Student:
    """Class representing a student with grades."""
    
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades else []
    
    def add_grade(self, grade):
        """Add a grade to student's record."""
        self.grades.append(grade)
    
    def get_average(self):
        """Calculate and return average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_statistics(self):
        """Get statistics for all grades."""
        if not self.grades:
            return None
        return {
            'average': self.get_average(),
            'min': min(self.grades),
            'max': max(self.grades),
            'median': statistics.median(self.grades)
        }
    
    def __str__(self):
        return f"Student: {self.name}, Grades: {self.grades}, Average: {self.get_average():.2f}"

student = Student("Dace Celmiņa", [92, 88, 95, 90])
print(f"Student Name: {student.name}")
print(f"Grades: {student.grades}")
print(f"Average: {student.get_average():.2f}")

student.add_grade(87)
print(f"After adding grade 87: {student.grades}")
print(f"New Average: {student.get_average():.2f}")

stats = student.get_statistics()
print(f"Statistics: Min={stats['min']}, Max={stats['max']}, Median={stats['median']}")

# PRACTICAL DEMONSTRATION

print("\n" + "="*70)
print("PRACTICAL DEMONSTRATION: MANAGING MULTIPLE STUDENTS")
print("="*70)

students = [
    Student("Kristofers Sīmans", [88, 92, 85, 90]),
    Student("Ieva Ošeniece", [95, 93, 97, 91]),
    Student("Raimonds Vaidere", [78, 82, 80, 85])
]

for student in students:
    print(f"\n{student.name}:")
    print(f"  Grades: {student.grades}")
    print(f"  Average: {student.get_average():.2f}")

# Find best student
best_student = max(students, key=lambda s: s.get_average())
print(f"\nBest Student: {best_student.name} with average {best_student.get_average():.2f}")
