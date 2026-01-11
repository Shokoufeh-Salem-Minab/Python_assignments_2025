import numpy as np

print("-- task 1: create numpy arrays --\n")

# create 1d array from 1 to 10
array_1d = np.arange(1, 11)
print(f"1d array: {array_1d}")
print(f"shape: {array_1d.shape}\n")

# create 2d array with shape (3,3)
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"2d array:\n{array_2d}")
print(f"shape: {array_2d.shape}\n")

print("-- task 2: reshape practice --\n")

# array of 12 elements
arr_12 = np.arange(1, 13)
print(f"original array: {arr_12}")

# reshape to (3,4)
reshaped_3x4 = arr_12.reshape(3, 4)
print(f"reshaped (3,4):\n{reshaped_3x4}")

# reshape to (2,6)
reshaped_2x6 = arr_12.reshape(2, 6)
print(f"reshaped (2,6):\n{reshaped_2x6}")

print("\nexplanation: reshape doesn't change the actual data, just how its organized")
print("the same values stay in memory, we just view them differently\n")

print("-- task 3: axis practice --\n")

# create 3x3 matrix
matrix_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"matrix:\n{matrix_3x3}\n")

# mean along axis 0 (down the columns)
mean_axis0 = np.mean(matrix_3x3, axis=0)
print(f"mean along axis=0 (columns): {mean_axis0}")

# sum along axis 1 (across the rows)
sum_axis1 = np.sum(matrix_3x3, axis=1)
print(f"sum along axis=1 (rows): {sum_axis1}")

print("\nexplanation:")
print("axis=0 means going down, so we get mean of each column")
print("axis=1 means going across, so we get sum of each row\n")

print("-- task 4: comparison operations --\n")

# create array of 10 random integers between 1 and 20
random_arr = np.random.randint(1, 21, size=10)
print(f"random array: {random_arr}")

# find mean
mean_val = np.mean(random_arr)
print(f"mean: {mean_val}")

# find values greater than mean
greater_than_mean = random_arr[random_arr > mean_val]
print(f"values greater than mean: {greater_than_mean}\n")

print("-- task 5: masking and filtering --\n")

# create array 0 to 20
arr_0_20 = np.arange(0, 21)
print(f"array 0-20: {arr_0_20}")

# extract even numbers using boolean mask
even_mask = arr_0_20 % 2 == 0
even_numbers = arr_0_20[even_mask]
print(f"even numbers: {even_numbers}")

# extract numbers divisible by 3
div_by_3_mask = arr_0_20 % 3 == 0
div_by_3 = arr_0_20[div_by_3_mask]
print(f"divisible by 3: {div_by_3}\n")

print("-- task 6: small oop + numpy --\n")

# matrix tool class
class MatrixTool:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
    
    # calculate mean of each row
    def row_mean(self):
        return np.mean(self.matrix, axis=1)
    
    # get values above threshold
    def above_threshold(self, t):
        return self.matrix[self.matrix > t]

# test the class
test_matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
tool = MatrixTool(test_matrix)

print(f"test matrix:\n{test_matrix}")
print(f"row means: {tool.row_mean()}")
print(f"values above 25: {tool.above_threshold(25)}\n")

print("-- task 7: mini challenge --\n")

# generate 5x5 random matrix
random_matrix = np.random.rand(5, 5)
print(f"original random matrix:\n{random_matrix}\n")

# replace values < 0.5 with 0 and >= 0.5 with 1
thresholded = random_matrix.copy()
thresholded[thresholded < 0.5] = 0
thresholded[thresholded >= 0.5] = 1

print(f"after thresholding (0 or 1):\n{thresholded}")

print("\nexplanation: this is called thresholding which is like when you are converting continuous values")