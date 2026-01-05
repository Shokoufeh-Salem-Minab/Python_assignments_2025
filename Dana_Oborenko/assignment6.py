from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

# Functional approach
def build_full_name(first: str, last: str) -> str:
    """Generate a full name from first and last names."""
    return f"{first.strip().title()} {last.strip().title()}"


def calculate_average(grades: List[float]) -> float:
    """Calculate average grade."""
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def functional_demo() -> None:
    print("\n--- Functional approach ---")
    full_name = build_full_name(" dana ", " oborenko ")
    grades = [9, 10, 8, 7, 10]

    print("Full name:", full_name)
    print("Grades:", grades)
    print("Average grade:", round(calculate_average(grades), 2))

# Function-based approach
def create_student_record(first: str, last: str, grades: List[float]) -> Dict[str, object]:
    """Store student data in a dictionary."""
    return {
        "full_name": build_full_name(first, last),
        "grades": grades,
        "average": round(calculate_average(grades), 2),
    }

def procedural_demo() -> None:
    print("\n--- Function-based (procedural) approach ---")
    record = create_student_record("Ivan", "Doska", [6, 7, 8, 9])

    print("Student record:", record)
    print(f"{record['full_name']} average grade = {record['average']}")

# Object-Oriented Programming (OOP)
@dataclass
class Student:
    first_name: str
    last_name: str
    grades: List[float]

    def full_name(self) -> str:
        return build_full_name(self.first_name, self.last_name)

    def add_grade(self, grade: float) -> None:
        self.grades.append(grade)

    def average(self) -> float:
        return round(calculate_average(self.grades), 2)

    def summary(self) -> str:
        return (
            f"Student: {self.full_name()} | "
            f"Grades: {self.grades} | "
            f"Average: {self.average()}"
        )

def oop_demo() -> None:
    print("\n--- OOP approach ---")
    student = Student("Maria", "Lee", [10, 9, 9])
    student.add_grade(8)
    print(student.summary())

def main() -> None:
    print("Assignment 6: Functional vs Procedural vs OOP approaches")
    functional_demo()
    procedural_demo()
    oop_demo()


if __name__ == "__main__":
    main()
