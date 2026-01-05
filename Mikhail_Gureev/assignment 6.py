"Functional Approach
# Full name
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Grades and average
grades = [80, 90, 85]
average = sum(grades) / len(grades)
print("Average Grade:", average)

#Function-Based Approach
# Function to create full name
def get_full_name(first, last):
    return first + " " + last

# Function to calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Using the functions
name = get_full_name("John", "Doe")
print("Full Name:", name)

grades = [80, 90, 85]
avg = calculate_average(grades)
print("Average Grade:", avg)

#Object-Oriented Programming (OOP) Approach
class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def full_name(self):
        return self.first_name + " " + self.last_name

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


# Creating an object
student = Student("John", "Doe", [80, 90, 85])

print("Full Name:", student.full_name())
print("Average Grade:", student.average_grade())
