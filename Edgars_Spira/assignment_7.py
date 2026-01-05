import assignment_3.file_operations as fo
# Write a program(function) that takes students information

# Assign a series of grades to each student

# Calculate average

# Write results in a file

def process_students(students):
    # students: dict -> {"Name": [grades]}
    # filename: str -> output file name

    base_directory = fo.os.path.dirname(fo.os.path.abspath(__file__)) # Path to the current file
    file_path = fo.os.path.join(base_directory, "student_grades.txt") # Add exact location of student_grades file

    # Iterate through each student and write students' full name, grades and average grade
    for name, grades in students.items():
        average = sum(grades) / len(grades)
        fo.write_message(
            f"Student: {name}\n"
            f"Grades: {grades}\n"
            f"Average: {average:.2f}\n\n"
        , file_path)

# Test data:
students = {
    "Alice Johnson": [9, 10, 8, 9],
    "Bob Smith": [7, 6, 8, 7],
    "Charlie Brown": [10, 9, 10, 10],
    "Diana Evans": [8, 9, 7, 8],
    "Ethan Clark": [6, 7, 6, 7]
}

# Execute function:
process_students(students)