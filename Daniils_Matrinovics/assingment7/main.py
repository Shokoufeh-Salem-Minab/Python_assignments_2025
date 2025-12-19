import pandas as pd

def with_logging(func):
    def wrapper(*args, **kwargs):
        with open("assingment7/student_log.txt", "a")as file:
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