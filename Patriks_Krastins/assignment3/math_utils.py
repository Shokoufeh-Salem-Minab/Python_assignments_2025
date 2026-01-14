def add(a, b):
    return a + b

def saveResult(path, value):
    with open(path, "w") as f:
        f.write(str(value))