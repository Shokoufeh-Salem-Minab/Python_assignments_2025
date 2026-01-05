import numpy as np

class MatrixTool:
    def __init__(self, matrix):
        self.matrix = matrix

    def row_mean(self):
        return self.matrix.mean(axis=1)
    
    def above_threshold(self, t):
        return self.matrix[self.matrix > t]

def main() -> None:
    print("Task 1")
    
    print("1D array")
    arr = np.arange(1,11)
    print("Array:", arr)
    print("Shape:", arr.shape)

    print("2D array")
    arr_2d = np.arange(1,10).reshape(3,3)
    print("Array:", arr_2d)
    print("Shape:", arr_2d.shape)

    print("Task 2")
    arr = np.arange(12)
    arr = arr.reshape(3,4)
    print("3x4:", arr)
    arr = arr.reshape(2,6)
    print("2x6:", arr)
    # 3x4 and 2x6 have same elements so data does not change

    print("Task 3")
    arr = np.arange(1,10).reshape(3,3)
    print("Mean axis=0:", arr.mean(axis=0))
    print("Sum axis=1:", arr.sum(axis=1))
    
    # 1 2 3 <- axis=1
    # 4 5 6 <- axis=1
    # 7 8 9 <- axis=1
    # ^ ^ ^
    # - axis=0

    print("Task 4")
    arr = np.random.randint(0,100, size = 10)
    print("10 num random arr:", arr)
    mean_val = arr.mean()
    greater = arr[arr > mean_val]
    print("Mean:", mean_val)
    print("Value > mean::", greater)

    print("Task 5")
    arr = np.arange(20)
    print("Even numbers:", arr[arr % 2 == 0])
    print("Num / 3:", arr[arr % 3 == 0])


    print("Task 6")
    arr = np.arange(1,10).reshape(3,3)
    tool = MatrixTool(arr)
    print("Row means:", tool.row_mean())
    print("Above threshold 5:", tool.above_threshold(3))

    print("Task 7")

    arr = np.random.rand(5, 5)
    print(arr)
    arr[arr < 0.5] = 0
    arr[arr >= 0.5] = 1
    print(arr)
if __name__ == "__main__":
    main()