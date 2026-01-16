from typing import Dict, List 

def full_name(person: Dict[str, str]) -> str: # added stricter typization 
    if not person.get("first") or not person.get("last"): # ensured presence of both names
        raise ValueError("First and last name cannot be empty!")
    return f"{person['first']} {person['last']}"

def average(student: Dict[str, List[float]]) -> float:
    if not student["grades"]:
        raise ValueError("Grades are absent!")
    return sum(student["grades"]) / len(student["grades"])

def add_grade(student: Dict[str, List[float]], grade: float) -> None: # void function
    if not 0 <= grade <= 100:
        raise ValueError("Grade must be between 0 and 100!")
    student["grades"].append(grade) 

person = {"first": "John", "last": "Doe"}
student = {"grades": []}

add_grade(student, 80) # added input example
add_grade(student, 90)
add_grade(student, 85)

print(full_name(person))
print(average(student))