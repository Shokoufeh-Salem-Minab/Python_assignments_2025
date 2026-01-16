import numpy as np

#Task 1

# Create a 1-dimensional NumPy array containing numbers from 1 to 10
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Print the 1D array
print("1D Array:", array_1d)

# Create a 2-dimensional NumPy array (a matrix with 3 rows and 3 columns)
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Print the 2D array
print("2D Array:")
print(array_2d)

# Print the shape of the 2D array
# Shape tells us (rows, columns)
print("Shape:", array_2d.shape)
#Task 2

# Create a 1D array with numbers from 1 to 12
array_12 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape the array into 3 rows and 4 columns
# Total elements must stay the same (12)
reshaped_3x4 = array_12.reshape(3, 4)

# Print the reshaped (3x4) array
print("Reshaped to (3,4):")
print(reshaped_3x4)

# Reshape the same array into 2 rows and 6 columns
reshaped_2x6 = array_12.reshape(2, 6)

# Print the reshaped (2x6) array
print("Reshaped to (2,6):")
print(reshaped_2x6)

#Task 3

# Create a 3x3 matrix
matrix_3x3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Print the matrix
print("3x3 Matrix:")
print(matrix_3x3)

# Calculate the mean of each column (axis = 0 means column-wise)
mean_axis0 = np.mean(matrix_3x3, axis=0)

# Print column means
print("Mean along axis = 0 (columns):", mean_axis0)

# Calculate the sum of each row (axis = 1 means row-wise)
sum_axis1 = np.sum(matrix_3x3, axis=1)

# Print row sums
print("Sum along axis = 1 (rows):", sum_axis1)


# Task 4

# Create a random array of 10 integers between 1 and 99
random_array = np.random.randint(1, 100, 10)

# Print the random array
print("Random array:", random_array)

# Calculate the mean (average) of the random array
mean_val = np.mean(random_array)

# Select only the values that are greater than the mean
# This uses boolean indexing
values_above_mean = random_array[random_array > mean_val]

# Print values above the mean
print("Values above mean:", values_above_mean)

# Task 5

# Create an array with values from 0 to 19
array_0_20 = np.arange(20)

# Print the array
print("Array 0-20:", array_0_20)

# Create a boolean mask that is True for even numbers
even_mask = array_0_20 % 2 == 0

# Use the mask to extract even numbers
even_numbers = array_0_20[even_mask]

# Print even numbers
print("Even numbers:", even_numbers)

# Extract numbers that are divisible by 3
divisible_by_3 = array_0_20[array_0_20 % 3 == 0]

# Print numbers divisible by 3
print("Numbers divisible by 3:", divisible_by_3)

# Task 6

# Define a class to perform operations on a matrix
class MatrixTool:
    
    # Constructor: runs when an object of this class is created
    def __init__(self, matrix):
        # Convert input into a NumPy array and store it
        self.matrix = np.array(matrix)
        
    # Method to calculate the mean of each row
    def row_mean(self):
        # axis=1 calculates mean row-wise
        return np.mean(self.matrix, axis=1)
        
    # Method to return elements greater than a threshold value
    def above_threshold(self, t):
        # Boolean filtering to get values greater than t
        return self.matrix[self.matrix > t]
        
# Task 7

# Create a 5x5 matrix with random float values between 0 and 1
random_matrix = np.random.rand(5, 5)
print("Original random matrix:")
print(random_matrix)

# Convert the matrix into a binary matrix
# Values < 0.5 become 0, values >= 0.5 become 1
binary_matrix = np.where(random_matrix < 0.5, 0, 1)
print("Binary matrix (threshold 0.5):")
print(binary_matrix)
