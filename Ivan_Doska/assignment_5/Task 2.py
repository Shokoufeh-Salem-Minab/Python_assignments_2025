import numpy as np

a = np.arange(12)
print("Initial array:", a)
b = a.reshape(3, 4)
print("\nReshape to (3,4):\n", a)
c = a.reshape(2, 6)
print("\nReshape to (2,6):\n", c)
# original data is not modified, only its view changes