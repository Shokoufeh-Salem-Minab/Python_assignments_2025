import numpy as np

print("=== NUMPY PRACTICE HOMEWORK ===\n")

# TASK 1 
print("--- TASK 1: Create NumPy Arrays ---")

# 1D array from 1 to 10
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("1D Array:", arr_1d)
print("Shape:", arr_1d.shape)

# 2D array with shape (3,3)
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(arr_2d)
print("Shape:", arr_2d.shape)

# TASK 2 
print("\n--- TASK 2: Reshape Practice ---")

# Array of 12 elements
arr_12 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original array:", arr_12)

# Reshape to (3,4)
reshaped_3_4 = arr_12.reshape(3, 4)
print("\nReshaped to (3,4):")
print(reshaped_3_4)

# Reshape to (2,6)
reshaped_2_6 = arr_12.reshape(2, 6)
print("\nReshaped to (2,6):")
print(reshaped_2_6)

print("\nExplanation: Reshape does not change the data, it only changes how the data is organized. The same numbers are just arranged differently.")

# TASK 3
print("\n--- TASK 3: Axis Practice ---")

# Create 3x3 matrix
matrix_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("3x3 Matrix:")
print(matrix_3x3)

# Mean along axis=0 (column-wise)
mean_axis0 = matrix_3x3.mean(axis=0)
print("\nMean along axis=0 (columns):", mean_axis0)

# Sum along axis=1 (row-wise)
sum_axis1 = matrix_3x3.sum(axis=1)
print("Sum along axis=1 (rows):", sum_axis1)

print("\nExplanation:")
print("axis=0 means going DOWN (columns) - computes mean of each column")
print("axis=1 means going ACROSS (rows) - computes sum of each row")

# TASK 4 
print("\n--- TASK 4: Comparison Operations ---")

# Create array of 10 random integers
random_arr = np.random.randint(1, 20, size=10)
print("Random array:", random_arr)

# Calculate mean
arr_mean = random_arr.mean()
print("Mean:", arr_mean)

# Find values greater than mean
greater_than_mean = random_arr[random_arr > arr_mean]
print("Values greater than mean:", greater_than_mean)

# TASK 5
print("\n--- TASK 5: Masking and Filtering ---")

# Create array 0-20
arr_0_20 = np.arange(0, 21)
print("Array 0-20:", arr_0_20)

# Extract even numbers
even_numbers = arr_0_20[arr_0_20 % 2 == 0]
print("Even numbers:", even_numbers)

# Extract numbers divisible by 3
divisible_by_3 = arr_0_20[arr_0_20 % 3 == 0]
print("Divisible by 3:", divisible_by_3)

# TASK 6 
print("\n--- TASK 6: Small OOP + NumPy ---")

class MatrixTool:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
    
    def row_mean(self):
        """Calculate mean of each row"""
        return self.matrix.mean(axis=1)
    
    def above_threshold(self, t):
        """Return values greater than threshold"""
        return self.matrix[self.matrix > t]

# Test the class
test_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tool = MatrixTool(test_matrix)

print("Test Matrix:")
print(test_matrix)

print("\nRow-wise means:", tool.row_mean())
print("Values above threshold 5:", tool.above_threshold(5))

# TASK 7 - Mini Challenge 
print("\n--- TASK 7: Mini Challenge ---")

# Generate 5x5 random matrix
random_matrix = np.random.rand(5, 5)
print("Original 5x5 random matrix:")
print(random_matrix)

# Replace values < 0.5 with 0
random_matrix[random_matrix < 0.5] = 0

# Replace values >= 0.5 with 1
random_matrix[random_matrix >= 0.5] = 1

print("\nAfter thresholding (0 or 1):")
print(random_matrix.astype(int))

print("\nExplanation: This is called thresholding - converting continuous")
print("values to binary (0 or 1) based on a threshold value (0.5).")

print("\n=== END OF HOMEWORK ===")