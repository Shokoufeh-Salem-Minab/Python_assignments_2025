"""
# task
**Comparing Functional, Function-Based, and OOP Approache**
1. Generate a person’s full name.
2. Store student grades and compute the average.
"""

import random
from pathlib import Path

FIRST_NAME = ["John", "Jane", "Jack", "Joe", "Giorno"]
LAST_NAME = ["Doe", "Dick", "Sparrow", "Swanson", "Giovanna"]


# Functional
def generate_full_name(first_name_list: list[str], last_name_list: list[str]) -> str:
    return random.choice(first_name_list) + " " + random.choice(last_name_list)


def compute_average(grades: list[int]) -> float:
    return sum(grades) / len(grades)


def store_grade(file: Path, full_name: str, average_grade: float):
    with open(file, "a") as grades_file:
        grades_file.write(f"{full_name}\t{average_grade}\n")


# OOP
class Student:
    def __init__(self, first_name: str, last_name: str, grades: list[int]):
        if grades is None:
            grades = []
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    @staticmethod
    def random_student_full_name(
        first_name_list: list[str], last_name_list: list[str]
    ) -> "Student":
        return Student(
            random.choice(first_name_list), random.choice(last_name_list), []
        )

    def add_grade(self, grade: int):
        self.grades.append(grade)
        return grade

    def compute_average(self) -> float:
        return sum(self.grades) / len(self.grades)

    def save_grade(self, file: Path):
        with open(file, "a") as grades_file:
            grades_file.write(f"{self.first_name}\t{self.last_name}\n")


# Function based (procedural)
def main():
    first_name = random.choice(FIRST_NAME)
    last_name = random.choice(LAST_NAME)
    full_name = first_name + " " + last_name

    grades = []
    grades.append(85)
    grades.append(90)
    grades.append(78)

    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)

    file = open("grades.txt", "a")
    file.write(f"{full_name}\t{average}\n")
    file.close()

    print(f"Saved: {full_name} with average {average}")
