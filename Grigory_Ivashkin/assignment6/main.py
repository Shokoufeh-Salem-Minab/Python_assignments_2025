# Functional approach

def make_full_name_func(first_name, last_name):
    # no side effects, just returns a result
    return first_name.strip().title() + " " + last_name.strip().title()

def add_grade_func(grades_list, grade):
    # returns a NEW list (does not change the original one)
    new_list = grades_list.copy()
    new_list.append(grade)
    return new_list

def average_func(grades_list):
    if len(grades_list) == 0:
        return 0
    return sum(grades_list) / len(grades_list)


# Function-based approach

def make_full_name(first_name, last_name):
    return first_name.strip().title() + " " + last_name.strip().title()

def add_grade(student_dict, grade):
    # student_dict example:
    # {"full_name": "John Smith", "grades": [8, 9, 10]}
    student_dict["grades"].append(grade)

def average(student_dict):
    grades = student_dict["grades"]
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


# OOP approach

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()
        self.grades = []

    def full_name(self):
        return self.first_name + " " + self.last_name

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


# ---------------------------------------------------------------------------

print("\nFunctional approach")
fn = make_full_name_func("  ivan  ", " doska ")
grades_f = []
grades_f = add_grade_func(grades_f, 8)
grades_f = add_grade_func(grades_f, 10)
grades_f = add_grade_func(grades_f, 9)
print("Full name:", fn)
print("Grades:", grades_f)
print("Average:", average_func(grades_f))

# ---------------------------------------------------------------------------
print("\nFunction-based approach")
student = {"full_name": make_full_name("  ivan  ", " doska "), "grades": []}
add_grade(student, 8)
add_grade(student, 10)
add_grade(student, 9)
print("Full name:", student["full_name"])
print("Grades:", student["grades"])
print("Average:", average(student))

# ---------------------------------------------------------------------------
print("\nOOP approach")
s = Student("  ivan  ", " doska ")
s.add_grade(8)
s.add_grade(10)
s.add_grade(9)
print("Full name:", s.full_name())
print("Grades:", s.grades)
print("Average:", s.average(),"\n")
