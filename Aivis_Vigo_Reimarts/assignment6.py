"""
Homework #6: Comparing Functional, Function-Based, and OOP Approaches

Tasks:
1. Generate a person's full name
2. Store student grades and compute the average
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List


# ==============================================================================
# FUNCTIONAL APPROACH
# ==============================================================================
def build_full_name(first: str, last: str) -> str:
    """Generate a full name from first and last names."""
    return f"{first.strip().title()} {last.strip().title()}"


def calculate_average(grades: List[float]) -> float:
    """Calculate average grade."""
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def functional_demo() -> None:
    print("\n" + "=" * 70)
    print("APPROACH 1: FUNCTIONAL")
    print("=" * 70)
    print("• Pure functions with no side effects")
    print("• Functions take input and return output")
    print("• No state modification")
    print("-" * 70)
    
    full_name = build_full_name(" dana ", " oborenko ")
    grades = [9, 10, 8, 7, 10]
    avg = round(calculate_average(grades), 2)
    
    print(f"Full name: {full_name}")
    print(f"Grades: {grades}")
    print(f"Average grade: {avg}")
    
    print("\n✓ Advantages: Predictable, testable, no side effects")
    print("✗ Disadvantages: Multiple separate function calls needed")


# ==============================================================================
# FUNCTION-BASED (PROCEDURAL) APPROACH
# ==============================================================================
def create_student_record(first: str, last: str, grades: List[float]) -> Dict[str, object]:
    """Store student data in a dictionary."""
    return {
        "full_name": build_full_name(first, last),
        "grades": grades,
        "average": round(calculate_average(grades), 2),
    }


def procedural_demo() -> None:
    print("\n" + "=" * 70)
    print("APPROACH 2: FUNCTION-BASED (PROCEDURAL)")
    print("=" * 70)
    print("• Functions that work with data structures (dicts)")
    print("• Data grouped together in dictionary")
    print("• Functions operate on data structures")
    print("-" * 70)
    
    record = create_student_record("Ivan", "Doska", [6, 7, 8, 9])
    
    print(f"Student record: {record}")
    print(f"{record['full_name']} average grade = {record['average']}")
    
    print("\n✓ Advantages: Simple, data grouped together")
    print("✗ Disadvantages: Data and functions separate, no encapsulation")


# ==============================================================================
# OBJECT-ORIENTED PROGRAMMING (OOP)
# ==============================================================================
@dataclass
class Student:
    """Student class encapsulating data and methods."""
    first_name: str
    last_name: str
    grades: List[float]
    
    def full_name(self) -> str:
        """Get full name."""
        return build_full_name(self.first_name, self.last_name)
    
    def add_grade(self, grade: float) -> None:
        """Add a grade to the student's record."""
        self.grades.append(grade)
    
    def average(self) -> float:
        """Calculate average grade."""
        return round(calculate_average(self.grades), 2)
    
    def summary(self) -> str:
        """Get complete student summary."""
        return (
            f"Student: {self.full_name()} | "
            f"Grades: {self.grades} | "
            f"Average: {self.average()}"
        )


def oop_demo() -> None:
    print("\n" + "=" * 70)
    print("APPROACH 3: OBJECT-ORIENTED PROGRAMMING (OOP)")
    print("=" * 70)
    print("• Data and methods bundled together in a class")
    print("• Each student is an independent object")
    print("• Encapsulation: data + behavior in one place")
    print("-" * 70)
    
    student = Student("Maria", "Lee", [10, 9, 9])
    student.add_grade(8)
    
    print(student.summary())
    
    # Create multiple students
    print("\nMultiple students:")
    student2 = Student("John", "Smith", [7, 8, 9])
    student3 = Student("Alice", "Johnson", [10, 10, 9, 10])
    
    print(f"  • {student2.full_name()}: {student2.average()}")
    print(f"  • {student3.full_name()}: {student3.average()}")
    
    print("\n✓ Advantages: Encapsulation, multiple instances, extensible")
    print("✗ Disadvantages: More code/boilerplate")


# ==============================================================================
# MAIN
# ==============================================================================
def main() -> None:
    print("=" * 70)
    print("HOMEWORK #6: Functional vs Function-Based vs OOP")
    print("=" * 70)
    
    functional_demo()
    procedural_demo()
    oop_demo()


if __name__ == "__main__":
    main()