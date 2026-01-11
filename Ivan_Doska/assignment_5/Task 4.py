import numpy as np

a = np.random.randint(0, 100, size=10) # random values [0; 99)
print(a)
m = a.mean()
print(m)
b = a[a > m]
print("Values greater than mean:", b) 