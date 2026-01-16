import numpy as np

# 3×3 matrix
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)
m0 = m.mean(axis=0) # mean for each column
print("\nMean along axis = 0", m0)
s1 = m.sum(axis=1) # sum each row, 1+2+3 4+5+6 7+8+9
print("\nSum along axis = 1", s1)