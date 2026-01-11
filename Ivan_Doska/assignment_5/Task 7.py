import numpy as n

matrix = n.random.rand(5, 5) # [0, 1)
bm = matrix.copy() # bm - binary matrix
bm[bm < 0.5] = 0
bm[bm >= 0.5] = 1
print("Original matrix:\n", matrix)
print("\nThresholded (binary) matrix:\n", bm)