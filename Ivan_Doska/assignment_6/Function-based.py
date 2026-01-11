def get_full_name(person):
    return person["first"] + " " + person["last"]

def get_average(student):
    return sum(student["grades"]) / len(student["grades"])


person = {"first": "John", "last": "Doe"}
student = {"grades": [80, 90, 85]}
print(get_full_name(person))
print(get_average(student))