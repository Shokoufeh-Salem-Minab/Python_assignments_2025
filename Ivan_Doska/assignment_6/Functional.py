def full_name(first, last):
    return f"{first} {last}"

def average(grades):
    return sum(grades) / len(grades)


name = full_name("John", "Doe")
avg = average([80, 90, 85])
print(name)
print(avg)
