import random

first_name = ["James", "Michael", "John", "Robert", "David"]
second_name = ["Abrahall", "Ideson", "Fairbras", "Ralfe"]

# Functional Approach

# Task 1 generate name
def fun_full_name():
    return f"{random.choice(first_name)} {random.choice(second_name)}"

fun_person = {}

#Task 2 grades
def fun_add_grade(name, grade):
    if name not in fun_person:
        fun_person[name] = []
    fun_person[name].append(grade)

def avg_grade(name):
    return sum(fun_person[name]) / len(fun_person[name])

print("Task 1")
name = fun_full_name()
fun_add_grade(name, 10)
fun_add_grade(name, 9)
fun_add_grade(name, 8)
print(fun_person)
print(avg_grade(name))

# Functional-based Approach

# Task 1 generate name
def funb_full_name():
    return f"{random.choice(first_name)} {random.choice(second_name)}"

fun_person = {}

#Task 2 grades
def funb_add_grade(name, grade):
    if name not in fun_person:
        fun_person[name] = []
    fun_person[name].append(grade)
    print(fun_person)

def avg_grade(name):
    print(sum(fun_person[name]) / len(fun_person[name]))

print("Task 2")
name = funb_full_name()
funb_add_grade(name, 10)
funb_add_grade(name, 9)
funb_add_grade(name, 8)
avg_grade(name)

#OOP Approache


# Task 1
class student_name:
    def full_name():
        return f"{random.choice(first_name)} {random.choice(second_name)}"

# Task 2
class student_grade:
    def __init__(self, name):
        self.grades = []
        self.name = name

    def add_grade(self, grade):
        self.grades.append(grade)
    
    def avg_grade(self):
        return sum(self.grades) / len(self.grades)
    
student = student_name().full_name

student_grade = student_grade(student)

print("Task 3")
student_grade.add_grade(10)
student_grade.add_grade(9)
student_grade.add_grade(8)
print(student_grade.avg_grade())



