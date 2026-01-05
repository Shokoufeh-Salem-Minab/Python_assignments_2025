import random

def avg_grade(student, size):
    grade = list()
    for x in range(size):
        grade.append(random.randint(1,5))   
    
    avg_grade = sum(grade) / len(grade)
    with open("grade.txt", "a") as f:
        f.write(f"{student}, Avg:{avg_grade}, Grade: {','.join(map(str, grade))}\n")
    
if __name__ == "__main__":
    avg_grade("Serhii", 6)