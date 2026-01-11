import numpy as np
#--------------------
print("\nTask 1 – Create NumPy Arrays")
# we create numpy array with 1-10 numbers in 1 line
arr1 = np.arange(1, 11)  # 1..10
print("1D array 1..10:", arr1)
#shape shows how we display the content
print("Shape:", arr1.shape)

# we create 1-9 numbers array, using reshape, we reshape this array into smth like matrix with 3 lines containing 3 indexes in each
    # .reshape() is used for it
arr2 = np.arange(1, 10).reshape(3, 3)  # 3x3
print("\n2D array (3x3):\n", arr2)
# print how many lines we have
print("Shape:", arr2.shape)

#--------------------
print("\nTask 2 – Reshape Practice")
arr12 = np.arange(1, 13)  # 12 elements
print("Original array:", arr12)
print("Original shape:", arr12.shape)

reshaped_3x4 = arr12.reshape(3, 4)
print("\nReshaped to (3,4):\n", reshaped_3x4)
print("Shape:", reshaped_3x4.shape)

reshaped_2x6 = arr12.reshape(2, 6)
print("\nReshaped to (2,6):\n", reshaped_2x6)
print("Shape:", reshaped_2x6.shape)

# print("reshape changes only how we 'view' the same data in memory.")
# print("The numbers and their order stay the same. Only the rows/columns layout changes.")
# rint("It works because 12 elements can be arranged as 3*4 or 2*6.")

#--------------------
print("\nTask 3 – Axis Practice (mean, sum)")
mat3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Matrix:\n", mat3)

mean_axis0 = mat3.mean(axis=0)
print("\nMean along axis=0 (column-wise):", mean_axis0)

sum_axis1 = mat3.sum(axis=1)
print("Sum along axis=1 (row-wise):", sum_axis1)

# print("axis=0 means 'go down the rows' -> compute per column.")
# print("axis=1 means 'go across the columns' -> compute per row.")

#--------------------
print("\nTask 4 – Comparison Operations")
rand_ints = np.random.randint(0, 101, size=10)  # 10 random ints 0..100
print("Random integers:", rand_ints)

#.mean() calculates the mean value.
m = rand_ints.mean()
print("Mean:", m)

greater_than_mean = rand_ints[rand_ints > m]
print("Values greater than the mean:", greater_than_mean)

#--------------------
print("\n Task 5 – Masking and Filtering")
arr0_20 = np.arange(0, 21)
print("Array 0..20:", arr0_20)

# check ifthe number in array is even.
even_mask = (arr0_20 % 2 == 0)
evens = arr0_20[even_mask]
print("\nEven numbers:", evens)

# check if the number in array is divisible by 3
div3_mask = (arr0_20 % 3 == 0)
div_by_3 = arr0_20[div3_mask]
print("Divisible by 3:", div_by_3)

#--------------------
print("\n Task 6 – Small OOP + NumPy")

# here we create a class MatrixTool.
# this class is used as a "container" that stores a matrix and functions that work with this matrix.
# instead of passing the matrix into every function, we store it inside the object.
class MatrixTool:

    # __init__ is a special function that runs automatically when we create an object of this class.
    # matrix is the data that we pass when creating the object.
    # self refers to the specific object that is being created.
    def __init__(self, matrix):
        # here we store the given matrix inside the object.
        # np.array(matrix) ensures that the data is a NumPy array.
        self.matrix = np.array(matrix)

    # this method calculates the mean value for each row of the matrix.
    def row_mean(self):
        # axis=1 means "row-wise" operation.
        # the result is one mean value per row.
        return self.matrix.mean(axis=1)

    # this method returns all values from the matrix that are greater than the given threshold t.
    def above_threshold(self, t):
        # self.matrix > t creates a boolean mask (True / False).
        # using this mask, we extract only the values that are greater than t.
        # the result is returned as a 1D NumPy array.
        return self.matrix[self.matrix > t]


# here we create an object called tool from the MatrixTool class.
# mat3 is passed into the class and stored inside the object as self.matrix.
tool = MatrixTool(mat3)

# call the row_mean() method.
# this calculates the mean for each row of the stored matrix.
print("Row-wise means:", tool.row_mean())

# call the above_threshold() method with threshold value 5.
# this prints all values from the matrix that are greater than 5.
print("Values above threshold 5:", tool.above_threshold(5))


#--------------------
print("\n Task 7 – Mini Challenge (thresholding)")

# here we create a 5x5 matrix with random float numbers.
# np.random.rand(5, 5) generates numbers in the range [0, 1),
# which means: 0 can appear, but 1 will not (it is always a bit less than 1).
rand_5x5 = np.random.rand(5, 5)

# print the original random matrix, so we can compare it later with the thresholded result.
print("Original 5x5 random matrix:\n", rand_5x5)

# here we make a copy of the original matrix.
# we do this because we want to keep rand_5x5 unchanged,
# and do all replacements only in the copy.
binary = rand_5x5.copy()

# thresholding part:
# binary < 0.5 creates a boolean mask (True/False) for every element in the matrix.
# for every element that is < 0.5 (True in the mask), we replace it with 0.
binary[binary < 0.5] = 0

# binary >= 0.5 creates another boolean mask.
# for every element that is >= 0.5 (True in the mask), we replace it with 1.
binary[binary >= 0.5] = 1

# now binary contains only 0 and 1 values.
# print the result after thresholding.
print("\nAfter thresholding (<0.5 -> 0, >=0.5 -> 1):\n", binary)

