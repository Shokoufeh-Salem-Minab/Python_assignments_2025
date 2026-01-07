from datetime import datetime


def process_student_grades(students_data, output_file="student_results.txt"):
    """
    Process student information, calculate averages, and write to file.
    
    Args:
        students_data: List of dictionaries with student info and grades
        output_file: Output filename for results
    
    Returns:
        dict: Dictionary with student names as keys and averages as values
    """
    results = {}
    
    for student in students_data:
        name = student['name']
        grades = student['grades']
        
        if grades:
            average = sum(grades) / len(grades)
        else:
            average = 0
        
        results[name] = average
    
    write_results_to_file(students_data, results, output_file)
    
    return results


def write_results_to_file(students_data, results, filename):
    """
    Write student results to a text file.
    
    Args:
        students_data: List of student dictionaries
        results: Dictionary of averages
        filename: Output filename
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("="*70 + "\n")
        file.write("STUDENT GRADES REPORT\n")
        file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("="*70 + "\n\n")
        
        for student in students_data:
            name = student['name']
            grades = student['grades']
            average = results[name]
            
            file.write(f"Student: {name}\n")
            file.write(f"Grades: {grades}\n")
            file.write(f"Average: {average:.2f}\n")
            file.write("-"*70 + "\n\n")
        
        file.write("="*70 + "\n")
        file.write("SUMMARY\n")
        file.write("="*70 + "\n")
        file.write(f"Total Students: {len(students_data)}\n")
        
        if results:
            highest_avg = max(results.values())
            lowest_avg = min(results.values())
            class_avg = sum(results.values()) / len(results)
            
            best_students = [name for name, avg in results.items() if avg == highest_avg]
            
            file.write(f"Class Average: {class_avg:.2f}\n")
            file.write(f"Highest Average: {highest_avg:.2f} ({', '.join(best_students)})\n")
            file.write(f"Lowest Average: {lowest_avg:.2f}\n")
        
        file.write("="*70 + "\n")
    
    print(f"Results written to '{filename}'")


def main():
    print("="*70)
    print("STUDENT GRADES PROCESSING SYSTEM")
    print("="*70)
    
    # Student information with grades
    students = [
        {
            'name': 'Jānis Bērziņš',
            'grades': [85, 90, 78, 92, 88]
        },
        {
            'name': 'Ilze Gaļitskaja',
            'grades': [88, 91, 85, 89, 93]
        },
        {
            'name': 'Andris Kalniņš',
            'grades': [92, 88, 95, 90, 87]
        },
        {
            'name': 'Dace Celmiņa',
            'grades': [75, 80, 82, 79, 84]
        },
        {
            'name': 'Kristofers Sīmans',
            'grades': [95, 93, 97, 91, 94]
        }
    ]
    
    print("\nProcessing student data...")
    print(f"Total students: {len(students)}\n")
    
    # Display student information
    for student in students:
        print(f"{student['name']}: {student['grades']}")
    
    # Process grades and calculate averages
    results = process_student_grades(students, "student_results.txt")
    
    # Display results
    print("\n" + "="*70)
    print("RESULTS")
    print("="*70)
    
    for name, average in results.items():
        print(f"{name}: Average = {average:.2f}")
    
    # Display summary statistics
    class_average = sum(results.values()) / len(results)
    highest = max(results.values())
    lowest = min(results.values())
    
    print("\n" + "-"*70)
    print("SUMMARY")
    print("-"*70)
    print(f"Class Average: {class_average:.2f}")
    print(f"Highest Average: {highest:.2f}")
    print(f"Lowest Average: {lowest:.2f}")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    main()
