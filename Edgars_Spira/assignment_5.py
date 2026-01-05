import numpy as np
# Task 1 – Create NumPy Arrays
print("TASK 1:")
# Create a 1D array of numbers from 1 to 10.
array1 = np.arange(1, 11)

# Create a 2D array with shape (3,3).
array2 = np.arange(1, 10).reshape(3, 3)

# Print the array and its shape.
print(f"Array 1 contents: {array1}", f"Array 1 shape: {array1.shape}")
print(f"Array 2 contents: {array2}", f"Array 2 shape: {array2.shape}")



# Task 2 – Reshape Practice
print("TASK 2:")
# Given an array of 12 elements, reshape it to (3,4).
array1 = np.arange(1, 13).reshape(3, 4)
print(f"Array 1 contents: {array1}", f"Array 1 shape: {array1.shape}")

# Then reshape it to (2,6).
array2 = array1.reshape(2, 6)
print(f"Array 2 contents: {array2}", f"Array 2 shape: {array2.shape}")
# Explain why reshape does not change array data.
# Reshape changes only shape of the array, not its contents.

#Task 3 – Axis Practice (mean, sum)**
print("TASK 3")

# Create a 3x3 matrix.
matrix = np.arange(1, 10).reshape(3, 3)
print(f"Matrix contents: {matrix}", f"Matrix shape: {matrix.shape}")

# Compute mean along axis=0.
np.mean(matrix, axis=0)
print(f"Mean for axis=0 (columns): {np.mean(matrix, axis=0)}")

# Compute sum along axis=1.
print(f"sum for axis=1 (rows): {np.sum(matrix, axis=1)}")

# Explain what each axis means.
# axis=0 -> columns -> top to bottom
# axis=1 -> rows -> left to right



# **Task 4 – Comparison Operations**
# Create an array of 10 random integers.
array = np.random.randint(0, 100, size=10) # 10 integers from range 0-99

# Find values greater than the mean.
# Return them as a new array.
mean_value = array.mean()
new_array = array[array > mean_value]


# **Task 5 – Masking and Filtering**
# Create an array 0–20.
array = np.arange(0, 21)

# Extract even numbers using a Boolean mask.
even_numbers = array[array % 2 == 0]

# Extract numbers divisible by 3.
div_by_3_numbers = array[array % 3 == 0]

# **Task 6 – Small OOP + NumPy**


# Write class MatrixTool:

# - method row_mean() → row-wise means
# - method above_threshold(t) → values > t
# Use NumPy arrays as input.

class MatrixTool:
    def __init__(self, arr):
        self.arr = np.array(arr)

    def row_mean(self):
        return self.arr.mean(axis=1)

    def above_threshold(self, t):
        return self.arr[self.arr > t]


# **Task 7 – Mini Challenge**

# Generate a 5x5 random matrix.
matrix = np.random.rand(5, 5)

# Replace values < 0.5 with 0.
matrix[matrix < 0.5] = 0

# Replace values ≥ 0.5 with 1.
matrix[matrix >= 0.5] = 1