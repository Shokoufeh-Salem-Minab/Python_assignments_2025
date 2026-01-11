class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return f"{self.first} {self.last}"


class Student(Person):
    def __init__(self, first, last, grades):
        super().__init__(first, last)
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("John", "Doe", [80, 90, 85])
print(student.full_name())
print(student.average())
