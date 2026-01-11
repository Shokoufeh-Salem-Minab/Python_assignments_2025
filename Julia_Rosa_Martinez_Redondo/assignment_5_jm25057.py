# ~~~~~~~~A C T I V I T Y 5 PYTHON - NumPy Practice~~~~~~~~
# By Julia Rosa Martinez Redondo jm25057

import numpy as np   # numpy basics, we use it for arrays and math stuff

# ~~~~~~~~TASK 1~~~~~~~~
# here i create a simple array from 1 to 10
nums1 = np.arange(1, 11)
print("nums 1 to 10:")
print(nums1)

# this is a 2D array, i reshape it to be 3x3
arr2d = np.arange(1, 10).reshape(3, 3)
print("\n3x3 array:")
print(arr2d)
print("shape:", arr2d.shape)   # shape shows rows and columns

# ~~~~~~~~TASK 2~~~~~~~~
# now i work with an array of 12 numbers
nums12 = np.arange(1, 13)
print("\nnums before reshape:")
print(nums12)

# reshape just changes how numbers are placed
resh1 = nums12.reshape(3, 4)
print("\nreshape 3x4:")
print(resh1)

resh2 = nums12.reshape(2, 6)
print("\nreshape 2x6:")
print(resh2)
# same values, just moved, nothing is deleted

# ~~~~~~~~TASK 3~~~~~~~~
# matrix example to practice axis
mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("\nmatrix:")
print(mat)

# axis 0 means columns
mean_cols = mat.mean(axis=0)
print("\nmean axis 0:")
print(mean_cols)

# axis 1 means rows
sum_rows = mat.sum(axis=1)
print("sum axis 1:")
print(sum_rows)
# axis 0 goes down
# axis 1 goes side

# ~~~~~~~~TASK 4~~~~~~~~
# random numbers to compare with the mean
rand_nums = np.random.randint(0, 50, 10)
print("\nrandom nums:")
print(rand_nums)

avg = rand_nums.mean()
print("avg:")
print(avg)

# here i select only numbers bigger than the average
above_avg = rand_nums[rand_nums > avg]
print("bigger than avg:")
print(above_avg)

# ~~~~~~~~TASK 5~~~~~~~~
# masking example
nums20 = np.arange(0, 21)
print("\nnums 0 to 20:")
print(nums20)

# even numbers using modulo
even_nums = nums20[nums20 % 2 == 0]
print("even nums:")
print(even_nums)

# numbers divisible by 3
div3_nums = nums20[nums20 % 3 == 0]
print("div by 3:")
print(div3_nums)


# ~~~~~~~~TASK 6~~~~~~~~
# small class to practice numpy with oop
class MatrixTool:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)   # make sure it is numpy array

    def row_mean(self):
        # mean for each row
        return self.matrix.mean(axis=1)

    def above_threshold(self, t):
        # return values bigger than t
        return self.matrix[self.matrix > t]


tool = MatrixTool(mat)
print("\nrow mean:")
print(tool.row_mean())

print("above 5:")
print(tool.above_threshold(5))

# ~~~~~~~~TASK 7~~~~~~~~
# random matrix & thresholding
rand_mat = np.random.rand(5, 5)
print("\nrandom matrix:")
print(rand_mat)

# here i change values depending if they are < or >= 0.5
bin_mat = rand_mat.copy()
bin_mat[bin_mat < 0.5] = 0
bin_mat[bin_mat >= 0.5] = 1

print("\nafter change:")
print(bin_mat)
