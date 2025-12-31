import numpy as np


# 1D array from 1 to 10
arr1 = np.arange(1, 11)

# 2D array with shape (3,3)
arr2 = np.arange(1, 10).reshape(3, 3)

print(arr1)
print("Shape:", arr1.shape)

print(arr2)
print("Shape:", arr2.shape)
