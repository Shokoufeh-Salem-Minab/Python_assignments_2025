from datetime import date

def save_grade(grade, value, file_path):
    today = date.today()
    with open(file_path, "a") as file:
        file.write(f"{today},{grade},{value}\n")

def read_grades(file_path):
    values = []
    with open(file_path, "r") as file:
        for line in file:
            _, _, value = line.strip().split(",")
            values.append(int(value))
    return values