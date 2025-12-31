def full_name(first, last):
    return first + " " + last


def average_grade(grades):
    return sum(grades) / len(grades)


# Usage
name = full_name("Ivan", "Doska")
grades = [80, 90, 75]

print("Full name:", name)
print("Average grade:", average_grade(grades))
