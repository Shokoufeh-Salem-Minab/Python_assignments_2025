import os
import sys

# Add modules directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))

from file_handler import read_grades_file, write_grades_file, generate_report
from grade_manager import add_student, add_grade, remove_student, display_students, calculate_statistics

# ===== CONFIGURATION =====
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'output')
GRADES_FILE = os.path.join(DATA_DIR, 'students.json')
REPORT_FILE = os.path.join(OUTPUT_DIR, 'grades_report.txt')

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===== MAIN PROGRAM =====
def main():
    print("="*70)
    print("STUDENT GRADE MANAGEMENT SYSTEM")
    print("="*70)
    print(f"\nData directory: {DATA_DIR}")
    print(f"Output directory: {OUTPUT_DIR}")
    
    # Read existing grades from file
    print(f"\nLoading grades from: {GRADES_FILE}")
    grades = read_grades_file(GRADES_FILE)
    
    # Display initial students
    print("\n" + "-"*70)
    print("INITIAL DATA")
    print("-"*70)
    display_students(grades)
    
    # Add new students
    print("\n" + "-"*70)
    print("ADDING NEW STUDENTS")
    print("-"*70)
    add_student(grades, "Kristofers Sīmans", [88, 92, 85])
    add_student(grades, "Ieva Ošeniece", [95, 93, 97])
    
    # Add grades to existing student
    print("\n" + "-"*70)
    print("ADDING GRADES")
    print("-"*70)
    add_grade(grades, "Jānis Bērziņš", 88)
    add_grade(grades, "Ilze Gaļitskaja", 92)
    
    # Display updated students
    print("\n" + "-"*70)
    print("UPDATED GRADES")
    print("-"*70)
    display_students(grades)
    
    # Calculate and display statistics for one student
    print("\n" + "-"*70)
    print("STUDENT STATISTICS")
    print("-"*70)
    if "Andris Kalniņš" in grades:
        stats = calculate_statistics(grades["Andris Kalniņš"])
        print(f"\nAndris Kalniņš Statistics:")
        print(f"  Average: {stats['average']:.2f}")
        print(f"  Median: {stats['median']:.2f}")
        print(f"  Min: {stats['min']}, Max: {stats['max']}")
    
    # Save updated grades to file
    print("\n" + "-"*70)
    print("SAVING DATA")
    print("-"*70)
    write_grades_file(GRADES_FILE, grades)
    
    # Generate report
    print("\n" + "-"*70)
    print("GENERATING REPORT")
    print("-"*70)
    generate_report(grades, REPORT_FILE)
    
    # Display directory structure
    print("\n" + "-"*70)
    print("PROJECT DIRECTORY STRUCTURE")
    print("-"*70)
    print_directory_structure(os.path.dirname(__file__))
    
    # Display files created
    print("\n" + "-"*70)
    print("FILES CREATED/MODIFIED")
    print("-"*70)
    list_files_in_directory(DATA_DIR, "Data Directory")
    list_files_in_directory(OUTPUT_DIR, "Output Directory")
    
    print("\n" + "="*70)
    print("PROGRAM COMPLETED SUCCESSFULLY!")
    print("="*70)


def print_directory_structure(path, prefix="", is_last=True):
    """
    Print directory structure recursively.
    
    Args:
        path (str): Directory path
        prefix (str): Prefix for tree structure
        is_last (bool): Whether this is the last item
    """
    items = []
    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        return
    
    # Filter out common ignored items
    items = [item for item in items if not item.startswith('.') and item != '__pycache__']
    
    for i, item in enumerate(items):
        item_path = os.path.join(path, item)
        is_last_item = (i == len(items) - 1)
        current_prefix = "└── " if is_last_item else "├── "
        print(prefix + current_prefix + item)
        
        if os.path.isdir(item_path) and item != '__pycache__':
            next_prefix = prefix + ("    " if is_last_item else "│   ")
            print_directory_structure(item_path, next_prefix, is_last_item)


def list_files_in_directory(directory, label):
    """
    List all files in a directory.
    
    Args:
        directory (str): Directory path
        label (str): Label for output
    """
    if not os.path.exists(directory):
        print(f"{label}: (empty)")
        return
    
    files = os.listdir(directory)
    if not files:
        print(f"{label}: (empty)")
        return
    
    print(f"\n{label}:")
    for file in sorted(files):
        filepath = os.path.join(directory, file)
        size = os.path.getsize(filepath)
        print(f"  • {file} ({size} bytes)")


if __name__ == "__main__":
    main()
