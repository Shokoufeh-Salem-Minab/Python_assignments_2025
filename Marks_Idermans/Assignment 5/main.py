#Marks Idermans
#mi24027

import numpy as np


#Task 1 – Create Arrays

print(" Task 1 ")
#1D array of numbers (1 to 10)
numbers_1d = np.arange(1, 11)
print("1D Array:", numbers_1d)

#2D array (3x3)
matrix_3x3 = np.array([[1,2,3],
                       [4,5,6],
                       [7,8,9]])
print("2D Array:\n", matrix_3x3)
print("Shape:", matrix_3x3.shape)  #number of rows, columns

#Task 2 – Reshape

print("\n Task 2 ")
#1D array of 12 elements
array_12 = np.arange(12)

#Reshape (3 rows, 4 columns)
array_3x4 = array_12.reshape(3,4)
print("Reshaped to 3x4:\n", array_3x4)

# Reshape (2 rows, 6 columns)
array_2x6 = array_12.reshape(2,6)
print("Reshaped to 2x6:\n", array_2x6)

#Task 3 – Axis Operations

print("\n Task 3 ")
matrix_for_axis = np.array([[1,2,3],
                            [4,5,6],
                            [7,8,9]])

#mean along columns (axis=0)
mean_per_column = matrix_for_axis.mean(axis=0)
print("Mean per column:", mean_per_column)

#sum along rows (axis=1)
sum_per_row = matrix_for_axis.sum(axis=1)
print("Sum per row:", sum_per_row)

#Task 4 – Comparison

print("\n Task 4 ")
#Create array of 10 random integers (0 and 99)
random_integers = np.random.randint(0, 100, 10)
mean_random = random_integers.mean()

#values greater than the mean
values_above_mean = random_integers[random_integers > mean_random]

print("Random integers:", random_integers)
print("Mean value:", mean_random)
print("Values above mean:", values_above_mean)


#Task 5 – Masking

print("\n Task 5")
#Create array from 0 to 20
numbers_0_to_20 = np.arange(21)

#even numbers using mask
even_numbers = numbers_0_to_20[numbers_0_to_20 % 2 == 0]

#numbers divisible by 3
divisible_by_3 = numbers_0_to_20[numbers_0_to_20 % 3 == 0]

print("Even numbers:", even_numbers)
print("Numbers divisible by 3:", divisible_by_3)


#Task 6 – OOP + NumPy

print("\n Task 6 ")
class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix  # store the NumPy array

    #Compute mean for each
    def row_mean(self):
        return self.matrix.mean(axis=1)

    #Return values above threshold
    def values_above_threshold(self, threshold):
        return self.matrix[self.matrix > threshold]

sample_matrix = np.array([[1,2,3],[4,5,6]])
matrix_tool = MatrixOperations(sample_matrix)

print("Row-wise means:", matrix_tool.row_mean())
print("Values above 3:", matrix_tool.values_above_threshold(3))


#7 – Thresholding

print("\n Task 7")
random_matrix_5x5 = np.random.rand(5,5)
print("Original 5x5 random matrix:\n", random_matrix_5x5)

#Replace < 0.5 = 0, >= 0.5 = 1
binary_matrix = np.where(random_matrix_5x5 < 0.5, 0, 1)
print("Binary thresholded matrix:\n", binary_matrix)


