import numpy as np
#Task 1
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("1D Array:", array_1d)
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(array_2d)
print("Shape:", array_2d.shape)
#Task 2
array_12 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshaped_3x4 = array_12.reshape(3, 4)
print("Reshaped to (3,4):")
print(reshaped_3x4)
reshaped_2x6 = array_12.reshape(2, 6)
print("Reshaped to (2,6):")
print(reshaped_2x6)
#Task 3
matrix_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("3x3 Matrix:")
print(matrix_3x3)
mean_axis0 = np.mean(matrix_3x3, axis = 0)
print("Mean along axis = 0 (columns):", mean_axis0)
sum_axis1 = np.sum(matrix_3x3, axis = 1)
print("Sum along axis = 1 (rows):", sum_axis1)
# Task 4
random_array = np.random.randint(1, 100, 10)
print("Random array:", random_array)
mean_val = np.mean(random_array)
values_above_mean = random_array[random_array > mean_val]
print("Values above mean:", values_above_mean)
# Task 5
array_0_20 = np.arange(20)
print("Array 0-20:", array_0_20)
even_mask = array_0_20 % 2 == 0
even_numbers = array_0_20[even_mask]
print("Even numbers:", even_numbers)
divisible_by_3 = array_0_20[array_0_20 % 3 == 0]
print("Numbers divisible by 3:", divisible_by_3)
# Task 6
class MatrixTool:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
    
    def row_mean(self):
        return np.mean(self.matrix, axis=1)
    
    def above_threshold(self, t):
        return self.matrix[self.matrix > t]
# Task 7
random_matrix = np.random.rand(5, 5)
print("Original random matrix:")
print(random_matrix)
binary_matrix = np.where(random_matrix < 0.5, 0, 1)
print("Binary matrix (threshold 0.5):")
print(binary_matrix)
