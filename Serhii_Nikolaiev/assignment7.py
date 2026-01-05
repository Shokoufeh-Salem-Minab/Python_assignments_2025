"""
**requirements**

Write a program(function) that takes students information

Assign a series of grades to each student

Calculate average

Write results in a file
"""

from pathlib import Path
from typing import TypeVar

K = TypeVar("K")


def assign_save_grades(student_infos: list[K], file: Path):
    results = []
    grade_series = [1, 2, 3, 4, 5]

    for student_info in student_infos:
        results.append(
            {
                "student_info": student_info,
                "average": sum(grade_series) / len(grade_series),
            }
        )

    with open(file, "w") as f:
        f.write(str(results))
