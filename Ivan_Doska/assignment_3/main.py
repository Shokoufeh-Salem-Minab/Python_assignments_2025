import os
import matplotlib.pyplot as plt

from grade import grade_value
from storage import save_grade, read_grades

BASE_DIR = os.path.dirname(__file__) # not pathlib as os module was already chosen
DATA_FILE = os.path.join(BASE_DIR, "data", "grades.txt") # data/grades.txt is created automatically
os.makedirs(os.path.dirname(DATA_FILE), exist_ok = True) # ensure exists

grade = input("Enter today's grade (A/B/C/D/F): ") # new program run = new day
value = grade_value(grade)
save_grade(grade, value, DATA_FILE)

values = read_grades(DATA_FILE)
average = sum(values) / len(values)
print(f"Average grade value: {average:.2f}")

plt.bar(range(len(values)), values)
plt.title("Grade History")
plt.ylabel("Grade Value")
plt.xlabel("Entry")
plt.show()