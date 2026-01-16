class Person:
    def __init__(self, first: str, last: str) -> None:
        if not first or not last:
            raise ValueError("First and last name cannot be empty!")
        self.first = first
        self.last = last

    def full_name(self) -> str:
        return f"{self.first} {self.last}"


class Student(Person):
    grades: List[float]

    def __init__(self, first: str, last: str) -> None:
        super().__init__(first, last)
        self.grades = [] 

    def average(self) -> float:
        if not self.grades:
            raise ValueError("Grades are absent!")
        return sum(self.grades) / len(self.grades)

    def add_grade(self, grade: float) -> None:
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100!")
        self.grades.append(grade)


student = Student("John", "Doe")
student.add_grade(80)
student.add_grade(90)
student.add_grade(85)

print(student.full_name())
print(student.average())