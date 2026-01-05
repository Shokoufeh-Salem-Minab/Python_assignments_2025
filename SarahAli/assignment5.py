
# NumPy Practice Homework


import numpy as np


# Task 1 – Create NumPy Arrays


# 1D array from 1 to 10
arr_1d = np.arange(1, 11)
print("Task 1 - 1D Array:", arr_1d)

# 2D array with shape (3,3)
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("Task 1 - 2D Array:\n", arr_2d)
print("Shape of 2D array:", arr_2d.shape)


# Task 2 – Reshape Practice


# Array of 12 elements
arr12 = np.arange(1, 13)

# Reshape to (3,4)
arr_3x4 = arr12.reshape(3, 4)
print("\nTask 2 - Reshape to (3,4):\n", arr_3x4)

# Reshape to (2,6)
arr_2x6 = arr12.reshape(2, 6)
print("Task 2 - Reshape to (2,6):\n", arr_2x6)

# Explanation: reshape does not change the data in memory, only how we view it.


# Task 3 – Axis Practice (mean, sum)


# 3x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("\nTask 3 - 3x3 matrix:\n", matrix)

# Mean along axis=0 (columns)
mean_axis0 = matrix.mean(axis=0)
print("Mean along axis 0 (columns):", mean_axis0)

# Sum along axis=1 (rows)
sum_axis1 = matrix.sum(axis=1)
print("Sum along axis 1 (rows):", sum_axis1)


# Task 4 – Comparison Operations


# Array of 10 random integers from 0 to 20
rand_arr = np.random.randint(0, 21, size=10)
print("\nTask 4 - Random array:", rand_arr)

# Mean value
mean_val = rand_arr.mean()
print("Mean value:", mean_val)

# Values greater than mean
greater_than_mean = rand_arr[rand_arr > mean_val]
print("Values greater than mean:", greater_than_mean)


# Task 5 – Masking and Filtering


arr0_20 = np.arange(21)  # 0 to 20

# Extract even numbers
even_numbers = arr0_20[arr0_20 % 2 == 0]
print("\nTask 5 - Even numbers:", even_numbers)

# Extract numbers divisible by 3
div3_numbers = arr0_20[arr0_20 % 3 == 0]
print("Task 5 - Numbers divisible by 3:", div3_numbers)


# Task 6 – Small OOP + NumPy


class MatrixTool:
    def __init__(self, array):
        self.array = np.array(array)  # store as NumPy array

    def row_mean(self):
        return self.array.mean(axis=1)  # mean of each row

    def above_threshold(self, t):
        return self.array[self.array > t]  # return values above t

# Example usage
mt = MatrixTool([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print("\nTask 6 - Row-wise mean:", mt.row_mean())
print("Task 6 - Values above 5:", mt.above_threshold(5))


# Task 7 – Mini Challenge


# 5x5 random matrix between 0 and 1
rand_matrix = np.random.rand(5, 5)
print("\nTask 7 - Original 5x5 random matrix:\n", rand_matrix)

# Thresholding: <0.5 -> 0, >=0.5 -> 1
rand_matrix[rand_matrix < 0.5] = 0
rand_matrix[rand_matrix >= 0.5] = 1
print("Task 7 - After thresholding:\n", rand_matrix)
