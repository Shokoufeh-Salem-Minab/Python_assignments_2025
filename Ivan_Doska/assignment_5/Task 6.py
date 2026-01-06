import numpy as n

class MatrixTool:
    def __init__(self, matrix: n.ndarray):
        self.matrix = n.asarray(matrix)

    def row_mean(self) -> n.ndarray:
        return self.matrix.mean(axis=1)

    def above_threshold(self, t: float) -> n.ndarray:
        return self.matrix[self.matrix > t]

m = n.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tool = MatrixTool(m)
print(tool.row_mean())
print(tool.above_threshold(5))