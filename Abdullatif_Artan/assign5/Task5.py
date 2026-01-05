import numpy as np

arr = np.arange(21)

even_numbers = arr[arr % 2 == 0]
div_by_3 = arr[arr % 3 == 0]

print("Even numbers:", even_numbers)
print("Divisible by 3:", div_by_3)
