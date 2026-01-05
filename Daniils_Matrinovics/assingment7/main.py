import pandas as pd
import os

def with_logging(func):
    def wrapper(*args, **kwargs):
        base_dir = os.path.dirname(__file__)    # current directory path (so that code still works when executed from the student folder)
        with open(f"{base_dir}/student_log.txt", "a")as file:
            file.write(func(*args, **kwargs))
    return wrapper

@with_logging
def student_averages(students):
    averages = ""
    for name, grades in students.items():
        averages += f"{name}: {grades.mean():.2f}\n"
    return averages

students = {
    "John Smith": pd.Series([2,5,3,5,5,7]),
    "Jane Doe": pd.Series([9,5,3,6,6,7]),
    "Elon Musk": pd.Series([9,10,8,10,10,9]),
    "Lewis Brown": pd.Series([6,7,3,2,10,6]),
}

student_averages(students)