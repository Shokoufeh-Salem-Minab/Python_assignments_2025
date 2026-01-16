from typing import List

def full_name(first: str, last: str) -> str: # added stricter typization 
    if not first or not last: # ensured presence of both names
        raise ValueError("First and last name cannot be empty!")
    return f"{first} {last}"

def average(grades: List[float]) -> float: # added stricter typization 
    if not grades:
        raise ValueError("Grades are absent!")
    return sum(grades) / len(grades)

def add_grade(grades: List[float], grade: float) -> List[float]: # added this function for input validation
    if not 0 <= grade <= 100:
        raise ValueError("Grade must be between 0 and 100!")
    return grades + [grade] 

name = full_name("John", "Doe")

grades = [] # added input example
grades = add_grade(grades, 80)
grades = add_grade(grades, 90)
grades = add_grade(grades, 85)

print(name)
avg = average(grades)
print(avg)