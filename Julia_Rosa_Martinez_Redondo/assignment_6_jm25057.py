# ~~~~~~~~A C T I V I T Y 6 PYTHON to compare approaches~~~~~~~~
# By Julia Rosa Martinez Redondo jm25057

# context of activity asked, planning steps:
# make full name, grades, avg
# 3 ways: direct / functions / oop
# ~~~~~~~~INPUT~~~~~~~~
name = input("enter 1st name: ")
sur_name = input("enter surname: ")

# i ask grades as text & then convert to numbers (normal way lal)
g1 = float(input("enter grade 1: "))
g2 = float(input("enter grade 2: "))
g3 = float(input("enter grade 3: "))


# ~~~~~~~~APPROACH 1 - "FUNCTIONAL" (direct code)~~~~~~~~
# here i do it directly without making functions/classes
full_name1 = name.strip() + " " + sur_name.strip()   # join name + surname
grades1 = [g1, g2, g3]                               # list of grades
avg1 = sum(grades1) / len(grades1)                   # average = sum / amount

print("\n~~~~~~~~approach 1 aka DIRECT MODE~~~~~~~~")
print("full name:", full_name1)
print("grades:", grades1)
print("average:", avg1)


# ~~~~~~~~APPROACH 2 - FUNCTION BASED~~~~~~~~
# now i do same but with functions (so i can reuse)
def make_full_name(n, s):
    # clean spaces and put together
    return n.strip() + " " + s.strip()


def average_grades(grades_list):
    # get avg from list
    return sum(grades_list) / len(grades_list)


full_name2 = make_full_name(name, sur_name)
grades2 = [g1, g2, g3]
avg2 = average_grades(grades2)

print("\n~~~~~~~~approach 2 aka FUNCTIONS~~~~~~~~")
print("full name:", full_name2)
print("grades:", grades2)
print("average:", avg2)


# ~~~~~~~~APPROACH 3 - OOP (class)~~~~~~~~
# oop is like "pack" data + functions together
class Student:
    def __init__(self, n, s, grades_list):
        self.n = n
        self.s = s
        self.grades = grades_list

    def full_name(self):
        # return full name using the saved data
        return self.n.strip() + " " + self.s.strip()

    def average(self):
        # return avg using the saved grades
        return sum(self.grades) / len(self.grades)


student1 = Student(name, sur_name, [g1, g2, g3])

print("\n-~~~~~~~~approach 3 aka OOP~~~~~~~~")
print("full name:", student1.full_name())
print("grades:", student1.grades)
print("average:", student1.average())


# ~~~~~~~~cCOMPARISON OF RESULTS (OF THE DIFF METHODS)~~~~~~~~
# direct --> fastest but not reusable
# functions -->  reusable pieces
# oop --> data + methods together in 1 thing (student)
# but same results in all 3 obviously printed in the console
