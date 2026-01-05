# function to calculate average of grades
def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

# function to process student info and write to file
def process_students(students_data, filename="student_results.txt"):
    # open file for writing
    with open(filename, 'w') as f:
        f.write("student grades report\n")
        f.write("=" * 50 + "\n\n")
        
        # process each student
        for student in students_data:
            name = student['name']
            grades = student['grades']
            average = calculate_average(grades)
            
            # write to file
            f.write(f"student: {name}\n")
            f.write(f"grades: {grades}\n")
            f.write(f"average: {average:.2f}\n")
            f.write("-" * 50 + "\n")
            
            # also print to console
            print(f"processed: {name} with the average: {average:.2f}")
    
    print(f"\nresults saved to {filename}")

# main program
print("-- student grades manager --\n")

# collect student information
students = [
    {
        'name': 'nikita yukhnevich',
        'grades': [55, 42, 18, 95, 38]
    },
    {
        'name': 'Albert Evans',
        'grades': [76, 55, 91, 28, 79]
    },
    {
        'name': 'Viktor Choukchoukov',
        'grades': [11, 89, 43, 97, 12]
    },
    {
        'name': 'Mei Lau',
        'grades': [2, 78, 25, 12, 87]
    }
]

# process all students and write to file
process_students(students)

print("\ndone!")