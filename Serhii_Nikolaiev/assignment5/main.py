import numpy

arr1 = numpy.arange(1, 10)
arr2 = numpy.zeros((3, 3))
print(arr1)
print(arr1.shape)
print(arr2)
print(arr2.shape)


def reshape(np_array: numpy.ndarray):
    # reshape does not change array data, because inside
    # it's just changing axis, not modifying data
    return np_array.reshape((3, 4)).reshape((2, 6))


arr3 = numpy.zeros((3, 3))
mean = numpy.mean(arr3, axis=0)
sum_ = numpy.sum(arr3, axis=1)
# axis 0 in 2d are rows
# axis 1 in 2d are columns

rng = numpy.random.default_rng()
rnd_ints = rng.integers(low=0, high=10, size=10)
avg = numpy.mean(rnd_ints)
vals_bigger_than_mean = rnd_ints[rnd_ints > avg]

arr4 = numpy.arange(0, 20)
arr_new = arr4[arr4 % 2 == 0]
arr_new_new = arr4[arr4 % 3 == 0]


class MatrixTool:
    def __init__(self, np_array):
        self.np_array = np_array

    def row_mean(self):
        return self.np_array.mean(axis=1)

    def above_threshold(self, t):
        return self.np_array > t


arri = numpy.arange(0, 6).reshape(2, 3)
print(arri)
print(MatrixTool(arri).row_mean())
print(MatrixTool(arri).above_threshold(2))

rnd_ints_new = rng.integers(low=0, high=10, size=25).reshape((5, 5))
rnd_ints_new = rnd_ints_new[rnd_ints_new > 0]
rnd_ints_new[rnd_ints_new < 0.5] = 0
rnd_ints_new[rnd_ints_new >= 0.5] = 1
