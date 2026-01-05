import numpy as np

# 1D array from 1 to 10
arr_1d = np.arange(1, 11)
print("1D Array:", arr_1d)
print("Shape:", arr_1d.shape)

# 2D array with shape (3, 3)
arr_2d = np.arange(1, 10).reshape(3, 3)
print("\n2D Array:\n", arr_2d)
print("Shape:", arr_2d.shape)

"""""""""""""
# Array of 12 elements
arr = np.arange(1, 13)

# Reshape to (3, 4)
reshaped_1 = arr.reshape(3, 4)
print("Reshape (3,4):\n", reshaped_1)

# Reshape to (2, 6)
reshaped_2 = arr.reshape(2, 6)
print("\nReshape (2,6):\n", reshaped_2)

#reshape() does not change the data, only how it is viewed.
#The total number of elements must stay the same (12 = 3×4 = 2×6).
"""""""""""""
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Mean along axis=0 (column-wise)
mean_axis_0 = matrix.mean(axis=0)
print("Mean (axis=0):", mean_axis_0)

# Sum along axis=1 (row-wise)
sum_axis_1 = matrix.sum(axis=1)
print("Sum (axis=1):", sum_axis_1)
"""""""""""""
# Random integers array
random_arr = np.random.randint(1, 100, 10)
print("Random Array:", random_arr)

# Mean of array
mean_value = random_arr.mean()
print("Mean:", mean_value)

# Values greater than mean
greater_than_mean = random_arr[random_arr > mean_value]
print("Values > Mean:", greater_than_mean)
"""""""""""""
arr = np.arange(0, 21)
print("Original Array:", arr)

# Even numbers
even_numbers = arr[arr % 2 == 0]
print("Even Numbers:", even_numbers)

# Numbers divisible by 3
div_by_3 = arr[arr % 3 == 0]
print("Divisible by 3:", div_by_3)
"""""""""""""
class MatrixTool:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def row_mean(self):
        return self.matrix.mean(axis=1)

    def above_threshold(self, t):
        return self.matrix[self.matrix > t]


# Example usage
mat = MatrixTool([
    [1, 2, 3],
    [4, 5, 6]
])

print("Row-wise Mean:", mat.row_mean())
print("Values above 3:", mat.above_threshold(3))
"""""""""""""
# 5x5 random matrix
matrix = np.random.rand(5, 5)
print("Original Matrix:\n", matrix)

# Apply threshold
matrix[matrix < 0.5] = 0
matrix[matrix >= 0.5] = 1

print("\nThresholded Matrix:\n", matrix)
