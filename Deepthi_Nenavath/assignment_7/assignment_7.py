def process_student_grades(students):
    """
    Takes student info with grades, calculates averages,
    and writes results to a file.
    
    Args:
        students: List of dicts with 'name', 'id', and 'grades'
    """
    
    #averages
    for student in students:
        total_grades = []
        for subject, grades in student['grades'].items():
            #subject average
            subject_avg = sum(grades) / len(grades) if grades else 0
            student['grades'][subject + '_avg'] = subject_avg
            total_grades.extend(grades)
    
        student['overall_avg'] = sum(total_grades) / len(total_grades) if total_grades else 0
    
    # Write to file
    with open('student_grades.txt', 'w') as f:
        f.write("STUDENT GRADE REPORT\n")
        f.write("=" * 40 + "\n\n")
        
        for student in students:
            f.write(f"Name: {student['name']}\n")
            f.write(f"ID: {student['id']}\n")
            f.write(f"Overall Average: {student['overall_avg']:.2f}\n\n")
            
            for subject, grades in student['grades'].items():
                if not subject.endswith('_avg'):
                    avg = student['grades'][subject + '_avg']
                    f.write(f"  {subject}: {grades} (Avg: {avg:.2f})\n")
            
            f.write("-" * 40 + "\n\n")
    
    print(f"Report written to student_grades.txt")
    return students

students_data = [
    {
        "name": "Summer smith",
        "id": "S001",
        "grades": {
            "Math": [85, 90, 88],
            "Science": [92, 87]
        }
    }
]

result = process_student_grades(students_data)

print(f"John's overall average: {result[0]['overall_avg']:.2f}")