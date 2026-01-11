def grade_value(grade):
    mapping = { 
        "F": 1,
        "D": 2,
        "C": 3,
        "B": 4,
        "A": 5
    }
    return mapping.get(grade.upper(), 0)