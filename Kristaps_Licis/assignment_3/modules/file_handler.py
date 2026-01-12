# file_handler.py - Module for file operations
# Handles reading and writing student grade data

import os
import json
from datetime import datetime


def read_grades_file(filepath):
    """
    Read grades from a JSON file.
    
    Args:
        filepath (str): Path to the grades file
    
    Returns:
        dict: Dictionary of students and their grades, or empty dict if file doesn't exist
    """
    if not os.path.exists(filepath):
        print(f"File '{filepath}' does not exist. Starting with empty data.")
        return {}
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"Successfully loaded data from '{filepath}'")
            return data
    except json.JSONDecodeError:
        print(f"Error: File '{filepath}' is not valid JSON. Starting with empty data.")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}


def write_grades_file(filepath, data):
    """
    Write grades to a JSON file.
    
    Args:
        filepath (str): Path to the grades file
        data (dict): Dictionary of students and their grades
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Ensure directory exists
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
            print(f"Successfully saved data to '{filepath}'")
            return True
    except Exception as e:
        print(f"Error writing file: {e}")
        return False


def generate_report(data, output_filepath):
    """
    Generate a text report of grades and save to file.
    
    Args:
        data (dict): Dictionary of students and their grades
        output_filepath (str): Path to save the report
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        directory = os.path.dirname(output_filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(output_filepath, 'w', encoding='utf-8') as file:
            file.write("="*70 + "\n")
            file.write("STUDENT GRADE REPORT\n")
            file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("="*70 + "\n\n")
            
            if not data:
                file.write("No student data available.\n")
                return True
            
            for student, grades in data.items():
                file.write(f"Student: {student}\n")
                file.write(f"  Grades: {grades}\n")
                
                if isinstance(grades, list) and grades:
                    average = sum(grades) / len(grades)
                    file.write(f"  Average: {average:.2f}\n")
                
                file.write("\n")
            
            file.write("="*70 + "\n")
            print(f"Report successfully generated: '{output_filepath}'")
            return True
    except Exception as e:
        print(f"Error generating report: {e}")
        return False
