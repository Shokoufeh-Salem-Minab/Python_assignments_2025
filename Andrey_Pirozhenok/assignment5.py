import numpy


class MatrixTool:
    def __init__(self, matrix: numpy.ndarray):
        self.matrix = matrix

    def row_mean(self) -> numpy.ndarray:
        return numpy.mean(self.matrix, 1)

    def above_threshold(self, t) -> numpy.ndarray:
        m = self.matrix.reshape(-1)
        return m[m > t]


def main() -> None:
    print("Task 1")
    np_array = numpy.arange(1, 11)
    print(np_array)

    print("Task 2")
    np_array = numpy.arange(12)
    print(np_array)
    print(np_array.reshape((3, 4)))
    print(np_array.reshape((2, 6)))
    # This does not change the data because np arrays are laid out as continuous memory blocks
    # (i.e. single dimension arrays) under the hood

    print("Task 3")
    mat = numpy.arange(1, 10).reshape((3, 3))
    print(mat)
    print(numpy.mean(mat[:, 0]))
    print(numpy.sum(mat[0, :]))

    # mat[   idx0,     idx1    ]
    #    axis 0 ^   axis 1^

    print("Task 4")
    data = numpy.random.randint(low=1, high=100, size=10)
    print(data)
    mean = numpy.mean(data)
    print(mean)
    print(data[data > mean])  # pretend that this is a return

    print("Task 5")
    data = numpy.arange(21)
    print(data[data % 2 == 0])
    print(data[data % 3 == 0])

    print("Task 6")
    data = numpy.arange(9).reshape(3, 3)
    c = MatrixTool(data)
    print(data)
    print(c.above_threshold(2))
    print(c.above_threshold(3))
    print(c.above_threshold(4))
    print(c.row_mean())

    print("Task 7")
    data = numpy.random.rand(5, 5)
    print(data)
    data[data < 0.5] = 0
    data[data >= 0.5] = 1
    print(data)


if __name__ == "__main__":
    main()
