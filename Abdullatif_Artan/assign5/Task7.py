import numpy as np

matrix = np.random.rand(5, 5)

binary_matrix = np.where(matrix < 0.5, 0, 1)

print("Original matrix:\n", matrix)
print("Thresholded matrix:\n", binary_matrix)
