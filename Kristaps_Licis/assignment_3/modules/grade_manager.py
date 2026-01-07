# grade_manager.py - Module for grade operations
# Manages adding, removing, and calculating student grades

import statistics


def add_student(data, name, grades=None):
    """
    Add a new student to the grades dictionary.
    
    Args:
        data (dict): Dictionary of students and grades
        name (str): Student name
        grades (list): Initial grades (optional)
    
    Returns:
        bool: True if added, False if student already exists
    """
    if name in data:
        print(f"Student '{name}' already exists!")
        return False
    
    data[name] = grades if grades else []
    print(f"Student '{name}' added successfully!")
    return True


def add_grade(data, name, grade):
    """
    Add a grade to an existing student.
    
    Args:
        data (dict): Dictionary of students and grades
        name (str): Student name
        grade (float): Grade to add
    
    Returns:
        bool: True if successful, False if student doesn't exist
    """
    if name not in data:
        print(f"Student '{name}' not found!")
        return False
    
    data[name].append(grade)
    print(f"Grade {grade} added to {name}")
    return True


def remove_student(data, name):
    """
    Remove a student from the grades dictionary.
    
    Args:
        data (dict): Dictionary of students and grades
        name (str): Student name
    
    Returns:
        bool: True if removed, False if student doesn't exist
    """
    if name not in data:
        print(f"Student '{name}' not found!")
        return False
    
    del data[name]
    print(f"Student '{name}' removed!")
    return True


def calculate_average(grades):
    """
    Calculate average grade from a list of grades.
    
    Args:
        grades (list): List of grades
    
    Returns:
        float: Average grade, or 0 if list is empty
    """
    if not grades:
        return 0
    return sum(grades) / len(grades)


def calculate_statistics(grades):
    """
    Calculate statistics for a list of grades.
    
    Args:
        grades (list): List of grades
    
    Returns:
        dict: Dictionary with average, max, min, and median
    """
    if not grades:
        return {'average': 0, 'max': 0, 'min': 0, 'median': 0}
    
    return {
        'average': calculate_average(grades),
        'max': max(grades),
        'min': min(grades),
        'median': statistics.median(grades)
    }


def display_students(data):
    """
    Display all students and their grades.
    
    Args:
        data (dict): Dictionary of students and grades
    """
    if not data:
        print("No students in the system.")
        return
    
    print("\n" + "="*70)
    print("STUDENT GRADES")
    print("="*70)
    
    for name, grades in data.items():
        print(f"\n{name}:")
        print(f"  Grades: {grades}")
        
        if grades:
            stats = calculate_statistics(grades)
            print(f"  Average: {stats['average']:.2f}")
            print(f"  Min: {stats['min']}, Max: {stats['max']}")
            print(f"  Median: {stats['median']:.2f}")
        else:
            print("  No grades recorded")
    
    print("\n" + "="*70 + "\n")
