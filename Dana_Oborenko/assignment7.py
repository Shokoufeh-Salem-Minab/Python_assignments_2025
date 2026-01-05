from __future__ import annotations

from typing import Dict, List
from pathlib import Path


# to run
# python3 Dana_Oborenko/assignment7.py

def process_students(students: Dict[str, List[int]], output_file: str) -> None:
    """
    Takes students information with grades,
    calculates averages and writes results to a file.
    """
    lines = []

    for name, grades in students.items():
        if grades:
            average = sum(grades) / len(grades)
        else:
            average = 0.0

        line = f"{name}: grades={grades}, average={round(average, 2)}"
        lines.append(line)

    path = Path(output_file)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    students_data = {
        "Dana Oborenko": [9, 10, 8, 9],
        "Robert Smith": [7, 8, 6, 7],
        "Maria Stone": [10, 9, 9, 10],
    }

    output_file = "students_results.txt"
    process_students(students_data, output_file)

    print(f"Results saved to '{output_file}'")


if __name__ == "__main__":
    main()
