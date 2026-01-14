# Functional approach
def fullName(firstName, lastName):
    return firstName + " " + lastName

def averageGrade(grades):
    return sum(grades) / len(grades)

print(fullName("Patriks", "Krastins"))
print(averageGrade([8, 9, 7, 10]))

# Function based
firstName = "Patriks"
lastName = "Krastins"
grades = [8, 9, 7, 10]

fullName = firstName + " " + lastName
avg = sum(grades) / len(grades)

print(fullName)
print(avg)

# OOP approach
class Student:
    def __init__(self, firstName, lastName, grades):
        self.firstName = firstName
        self.lastName = lastName
        self.grades = grades

    def fullName(self):
        return self.firstName + " " + self.lastName

    def averageGrade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Patriks", "Krastins", [8, 9, 7, 10])
print(student.fullName())
print(student.averageGrade())