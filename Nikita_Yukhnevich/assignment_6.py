# comparing functional, function-based, and oop approaches

print("-- approach 1: functional (procedural) --\n")

# generate full name (functional)
first_name = "nikita"
last_name = "yukhnevich"
full_name = first_name + " " + last_name
print(f"full name: {full_name}")

#store grades and compute average (functional)
grades = [55, 22, 68, 90, 58]
total = 0
for grade in grades:
    total += grade
average = total / len(grades)
print(f"grades: {grades}")
print(f"average: {average}\n")

print("-- approach 2: function-based --\n")

#generate full name (function)
def create_full_name(first, last):
    return f"{first} {last}"

#compute average (function)
def calculate_average(grades_list):
    return sum(grades_list) / len(grades_list)

def display_grades(name, grades_list):
    avg = calculate_average(grades_list)
    print(f"student: {name}")
    print(f"grades: {grades_list}")
    print(f"average: {avg}")

student_name = create_full_name("nikita", "yukhnevich")
student_grades = [55, 22, 68, 90, 58]
display_grades(student_name, student_grades)
print()

print("-- approach 3: oop (object-oriented) --\n")

#OOP
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []
    
    # get full name
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    # add a grade
    def add_grade(self, grade):
        self.grades.append(grade)
    
    # calculate average
    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    # display student info
    def display_info(self):
        print(f"student: {self.get_full_name()}")
        print(f"grades: {self.grades}")
        print(f"average: {self.get_average()}")

# create student object
student = Student("nikita", "yukhnevich")
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
student.add_grade(90)
student.add_grade(88)
student.display_info()
print()

print("-- comparison summary --\n")
print("functional:its super simple and good for small tasks")
print("function-based: a little more complicated but more organized, easier to test")
print("oop: bundles data with methods, good for complex systems")
print("\neach approach has its place depending on the problem!")