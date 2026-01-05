import numpy as np

arr = np.random.randint(1, 100, 10)

mean_value = arr.mean()
greater_than_mean = arr[arr > mean_value]

print("Array:", arr)
print("Mean:", mean_value)
print("Values > mean:", greater_than_mean)
