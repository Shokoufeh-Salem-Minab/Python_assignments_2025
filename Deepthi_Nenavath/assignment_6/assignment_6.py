from functools import reduce

#Function-Based
first_name = "John"
last_name = "Doe"

def get_full_name(fname, lname):
    return f"{fname} {lname}"  

grades = {"math": [85, 90, 88], "science": [92, 87, 95]}
def calc_average(grades_dict):
    all_grades = []
    for subject in grades_dict.values():
        all_grades.extend(subject)
    return sum(all_grades) / len(all_grades) if all_grades else 0

print(get_full_name(first_name, last_name))  
print(calc_average(grades)) 

#OOP (Object-Oriented)

class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.grades = {}  
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def add_grade(self, subject, grade):
        self.grades.setdefault(subject, []).append(grade)
    
    def get_average(self):
        all_grades = [g for subj in self.grades.values() for g in subj]
        return sum(all_grades)/len(all_grades) if all_grades else 0

s = Student("Jane", "Smith")
s.add_grade("math", 85)
s.add_grade("math", 90)
print(s.full_name())  
print(s.get_average()) 



#Functional
def full_name(first, last):
    return f"{first} {last}" 


def format_name(separator):
    return lambda first, last: f"{first}{separator}{last}"

def add_grade(grades_dict, subject, grade):
    new_dict = {k: v[:] for k, v in grades_dict.items()}  
    new_dict.setdefault(subject, []).append(grade)
    return new_dict  

def calc_avg(grades):
    total = reduce(lambda x, y: x + y, grades, 0)  
    return total/len(grades) if grades else 0

name_func = format_name("_")
print(name_func("John", "Doe"))  

grades = {"math": [85, 90]}
new_grades = add_grade(grades, "math", 95) 
print(calc_avg(new_grades["math"]))  