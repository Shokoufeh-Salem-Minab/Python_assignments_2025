# Task 1
def generate_full_name(first, last):
    return first + " " + last

# Task 2
def calculate_average(grades):
    return sum(grades) / len(grades)

full_name = generate_full_name("Yangli", "Deng")
print("Full name:", full_name)

grades = [80, 90, 85]
average = calculate_average(grades)
print("Average grade:", average)
