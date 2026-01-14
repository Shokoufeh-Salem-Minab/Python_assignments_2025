import random
from math_utils import add, saveResult

x = random.randint(1, 10)
y = random.randint(1, 10)

result = add(x, y)
print("Result:", result)

saveResult("assignment3/data.txt", result)
