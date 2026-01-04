# ~~~~~~~~A C T I V I T Y 7 PYTHON - Students grades~~~~~~~~
# By Julia Rosa Martinez Redondo jm25057

# what i had to do and steps here:
# pick up student info
# assign him grades
# do average of them
# to be putted into file
# ~~~~~~~~FUNCTION~~~~~~~~
def stdnt_avg(name, grades):
    # calculate average of grades list
    total = 0
    for g in grades:
        total = total + g   # sum grades one by one

    avg = total / len(grades)
    return avg


# ~~~~~~~~INPUT~~~~~~~~
stdnt_name = input("enter student name: ")
# ask grades one by one (basic way)
g1 = float(input("enter grade 1: "))
g2 = float(input("enter grade 2: "))
g3 = float(input("enter grade 3: "))

grades_list = [g1, g2, g3]   # list with all grades

# ~~~~~~~~PROCESS~~~~~~~~
stdnt_average = stdnt_avg(stdnt_name, grades_list)

# ~~~~~~~~OUTPUT~~~~~~~~
print("\nstudent:", stdnt_name)
print("grades:", grades_list)
print("average:", stdnt_average)

# ~~~~~~~~SAVE TO FILE~~~~~~~~
file = open("students_results.txt", "a")

file.write("student: " + stdnt_name + "\n")
file.write("grades: " + str(grades_list) + "\n")
file.write("average: " + str(stdnt_average) + "\n")

file.close()
