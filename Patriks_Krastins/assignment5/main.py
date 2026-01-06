import numpy as np

# Task 1 – Create NumPy Arrays
arr1d = np.arange(1, 11)
arr2d = np.arange(1, 10).reshape(3, 3)

print(arr1d, "\n")
print(arr2d, "\n")
print("Shape:", arr2d.shape)
print("\n--------------------------\n")

# Task 2 – Reshape Practice
arr = np.arange(12)

reshaped1 = arr.reshape(3, 4)
reshaped2 = arr.reshape(2, 6)

print(reshaped1, "\n")
print(reshaped2, "\n")
#Does not cahnge array data bc it only returns a view of the same data
print("\n--------------------------\n")

# Task 3 – Axis Practice
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Mean axis=0:", matrix.mean(axis=0).astype(int))
#mean for each column
print("Sum axis=1:", matrix.sum(axis=1))
#sum for each row
print("\n--------------------------\n")

# Task 4 – Comparison Operations
randArr = np.random.randint(1, 20, 10)
mean = randArr.mean()

greaterMean = randArr[randArr > mean]

print(randArr, "\n")
print(greaterMean)
print("\n--------------------------\n")

# Task 5 – Masking and Filtering
nums = np.arange(21)

evenNums = nums[nums % 2 == 0]
devideBy3 = nums[nums % 3 == 0]

print(evenNums, "\n")
print(devideBy3)
print("\n--------------------------\n")

# Task 6 – Small OOP + NumPy
class MatrixTool:
    def __init__(self, matrix):
        self.m = np.array(matrix)

    def rowMean(self):
        rowMeans = self.m.mean(axis=1)
        return rowMeans.astype(int)

    def aboveThreshold(self, t):
        aboveThreshold = self.m > t
        return self.m[aboveThreshold]

tool = MatrixTool([[1, 2, 3], [4, 5, 6]])

print(tool.rowMean(), "\n")
print(tool.aboveThreshold(3))
print("\n--------------------------\n")

# Task 7 – Mini Challenge
randMatrix = np.random.rand(5, 5)

randMatrix[randMatrix < 0.5] = 0
randMatrix[randMatrix >= 0.5] = 1

randMatrix = randMatrix.astype(int)

print(randMatrix)
