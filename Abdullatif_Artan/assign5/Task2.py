import numpy as np

arr = np.arange(1, 13)

arr_3x4 = arr.reshape(3, 4)
arr_2x6 = arr.reshape(2, 6)

print(arr_3x4)
print(arr_2x6)
