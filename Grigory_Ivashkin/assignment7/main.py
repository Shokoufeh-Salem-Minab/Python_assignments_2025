
# this function calculates the average (mean) value of a list of grades.
# grades is expected to be a list of numbers, for example: [8, 9, 10]
def calculate_average(grades):

    # if the list is empty, we cannot divide by 0.
    # so, if there are no grades, we return 0 as the average.
    if len(grades) == 0:
        return 0

    # sum(grades) calculates the total of all numbers in the list.
    # len(grades) gives the count of grades.
    # average = total / count
    return sum(grades) / len(grades)


# this function processes students info, assigns grades, calculates averages, and saves everything into a file.
# filename is the file name where we save the results.
# by default it will be "results.txt" if we do not pass a different name.
def process_students_and_save(filename="results.txt"):

    # here we store students data as a list of dictionaries.
    # a dictionary is used because it lets us store data using keys, like:
    # {"first_name": "Ivan", "last_name": "Doska"}
    students = [
        {"first_name": "Ivan", "last_name": "Doska"},
        {"first_name": "Grigory", "last_name": "Ivashkin"},
        {"first_name": "Anna", "last_name": "Petrova"}
    ]

    # here we store grades in a dictionary:
    # key - full name of student (string)
    # value - list of grades (list of numbers)
    # e.g. "Ivan Doska": [8, 9, 10]
    grades_by_student = {
        "Ivan Doska": [8, 9, 10],
        "Grigory Ivashkin": [7, 6, 8, 9],
        "Anna Petrova": [10, 10, 9]
    }

    # here we calculate averages and build output lines
    # lines is a list of strings.
    # each string will be one line in the output file.
    lines = []

    # we go through students list one by one.
    # s is a dictionary for a single student.
    for s in students:

        # create full name from first_name and last_name.
        # we use s["first_name"] and s["last_name"] because s is a dictionary.
        full_name = s["first_name"] + " " + s["last_name"]

        # create an empty grades list.
        # we will fill it if we find grades for this student.
        grades = []

        # check if this full name exists as a key in grades_by_student dictionary.
        # if yes, we take grades from the dictionary.
        if full_name in grades_by_student:
            grades = grades_by_student[full_name]

        # calculate average grade for this student using our function.
        avg = calculate_average(grades)

        # create a text line for the file.
        # f"..." is an f-string (formatted string).
        # it allows to put variables inside { } directly in the text.
        # {avg:.2f} means: print avg with 2 digits after the decimal point.
        lines.append(f"Student: {full_name} | Grades: {grades} | Average: {avg:.2f}")

    # here we write results to a file
    # open(filename, "w") means open file in write mode:
    # - if file does not exist -> it will be created
    # - if file exists -> it will be overwritten
    # encoding="utf-8" is used so non-English letters work correctly.
    with open(filename, "w", encoding="utf-8") as f:

        # write each line into the file.
        # "\n" is added so every result is on a new line.
        for line in lines:
            f.write(line + "\n")

    # print a confirmation message in console
    print("Saved results to:", filename)


# after we run the program
# this calls the function and creates the output file results.txt
process_students_and_save()
