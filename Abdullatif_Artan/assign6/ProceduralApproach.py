first_name = "Ivan"
last_name = "Doska"
grades = [80, 90, 75]


def print_full_name():
    print("Full name:", first_name, last_name)


def print_average():
    avg = sum(grades) / len(grades)
    print("Average grade:", avg)


# Usage
print_full_name()
print_average()
