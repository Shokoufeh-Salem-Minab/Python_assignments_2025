# Jānis Sniedze
# js23127
# Homework 7
# Final edit date: 30/12/2025


import random  # random used to generate grades when none are provided
import os  # os used to produce an absolute path for the output file
from typing import List, Dict, Union, Optional  # typing helpers for signatures


def processStudents(
	students: List[Union[str, Dict]],
	gradesPerStudent: int = 5,
	minGrade: int = 0,
	maxGrade: int = 100,
	outputFile: str = "results.txt",
	seed: Optional[int] = None,
) -> str:  # assign grades, compute averages, and write CSV returning absolute path
	if seed is not None:
		random.seed(seed)  # seed random for reproducible demo results when requested

	results: List[Dict] = []  # collect processed student records as simple dicts
	for item in students:
		if isinstance(item, dict):
			name = item.get("name") or str(item.get("id", "Unknown"))  # prefer explicit name, fall back to id or Unknown
			grades = item.get("grades")  # may be None indicating we should generate random grades
			if grades is None:
				grades = [random.randint(minGrade, maxGrade) for _ in range(gradesPerStudent)]  # generate random integer grades
		else:
			name = str(item)  # coerce non-dict entries to string to use as a student name
			grades = [random.randint(minGrade, maxGrade) for _ in range(gradesPerStudent)]  # generate default set of grades

		average = sum(grades) / len(grades) if grades else 0.0  # compute average with safe empty handling
		results.append({"name": name, "grades": grades, "average": average})  # keep name, raw grades list, and computed average

	with open(outputFile, "w", encoding="utf-8") as fh:
		fh.write("name,grades,average\n")  # header row using comma-separated values
		for rec in results:
			gradesStr = ";".join(str(g) for g in rec["grades"]) if rec["grades"] else ""  # join grades with semicolon to keep CSV stable
			fh.write(f"{rec['name']},{gradesStr},{rec['average']:.2f}\n")  # write a simple CSV line per student

	return os.path.abspath(outputFile)  # return the absolute path for convenience to callers


if __name__ == "__main__":
	demoStudents = [
		"Alice",
		"Bob",
		{"name": "Charlie", "grades": [88, 90, 92]},
		{"name": "Dana"},
	]
	outPath = processStudents(demoStudents, gradesPerStudent=4, seed=42, outputFile="results.txt")  # run demo and get output path
	print(f"Wrote results to {outPath}")  # inform user where results were written

