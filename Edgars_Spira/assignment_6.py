# Comparing Functional, Function-Based, and OOP Approaches
# 1. Generate a person’s full name.
# 2. Store student grades and compute the average.

# OOP approach:
class Student:
    def __init__(self, first_name, last_name, grades):
        self.first = first_name
        self.last = last_name
        self.grades = grades

    def full_name(self):
        return f"{self.first} {self.last}"

    def average(self):
        return sum(self.grades) / len(self.grades)

# Function based approach:
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

def average(grades):
    return sum(grades) / len(grades)


# Functional programming approach:
full_name = lambda first_name, last_name: f"{first_name} {last_name}"
avg = lambda grades: sum(grades) / len(grades)
