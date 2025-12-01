"""
NumPy Practice & Mini OOP

Demonstrates basic NumPy operations.

Features:
* Array creation and reshaping
* Axis-based computations (mean, sum)
* Comparison operations and masking/filtering
* Simple OOP integration with NumPy arrays
* Thresholding a random matrix

"""

import numpy as np

arr1 = np.arange(1, 11)
print("1D array: ", arr1)
print("Shape: ", arr1.shape)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print("2D array:\n", arr2)
print("Shape: ", arr2.shape)
print("\n")

print("=" * 40)
print("Reshaping arrays:")

arr3 = np.arange(12)
print("Original array: ", arr3)

arr3 = arr3.reshape(3, 4)
print("Reshaped to 3x4:\n", arr3)

arr3 = arr3.reshape(2, 6)
print("Reshaped to 2x6:\n", arr3)

print("Reshape does not change data, it just reorganizes the view of elements.")
print("\n")

print("=" * 40)
print("Axis practice:")
arr4 = np.array([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
print("Matrix:\n", arr4)

mean0 = arr4.mean(axis=0)  # column-wise mean
sum1 = arr4.sum(axis=1)    # row-wise sum
print("Mean along axis 0 (columns): ", mean0)
print("Sum along axis 1 (rows): ", sum1)
print("Axis 0 = down columns, Axis 1 = across rows.")
print("\n")

print("=" * 40)
print("Comparison Operations:")
randints = np.random.randint(0, 20, 10)
print("Random integers:", randints)

meanval = randints.mean()
abovemean = randints[randints > meanval]
print("Mean value:", meanval)
print("Values greater than mean:", abovemean)
print("\n")

print("=" * 40)
print("Masking and filtering:")
arr5 = np.arange(21)
evenmask = arr5 % 2 == 0

evennums = arr5[evenmask]
div3nums = arr5[arr5 % 3 == 0]

print("Even numbers:", evennums)
print("Numbers divisible by 3:", div3nums)
print("\n")

print("=" * 40)
print("Small OOP + NumPy:")
class MatrixTool:
    def __init__(self, array):
        self.array = array

    def row_mean(self):
        return self.array.mean(axis=1)

    def above_threshold(self, t):
        return self.array[self.array > t]


mt = MatrixTool(np.random.rand(3,3))
print("Matrix:\n", mt.array)
print("Row-wise mean:", mt.row_mean())
print("Values above 0.5:", mt.above_threshold(0.5))
print("\n")

print("=" * 40)
print("Mini challenge:")
rand5x5 = np.random.rand(5,5)
print("5x5 random matrix:\n", rand5x5)

thresholded = np.where(rand5x5 < 0.5, 0, 1)
print("After thresholding (<0.5=0, >=0.5=1):\n", thresholded)