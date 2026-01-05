class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def full_name(self):
        return self.first_name + " " + self.last_name

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Yangli", "Deng", [80, 90, 85])

print("Full name:", student.full_name())
print("Average grade:", student.average_grade())
