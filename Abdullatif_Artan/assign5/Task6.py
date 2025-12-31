import numpy as np

class MatrixTool:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def row_mean(self):
        return self.matrix.mean(axis=1)

    def above_threshold(self, t):
        return self.matrix[self.matrix > t]


# Example usage
m = MatrixTool([[1, 2, 3], [4, 5, 6]])

print("Row means:", m.row_mean())
print("Above threshold 3:", m.above_threshold(3))
