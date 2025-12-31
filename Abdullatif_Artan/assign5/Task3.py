import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

mean_axis0 = matrix.mean(axis=0)
sum_axis1 = matrix.sum(axis=1)

print("Mean axis=0:", mean_axis0)
print("Sum axis=1:", sum_axis1)
