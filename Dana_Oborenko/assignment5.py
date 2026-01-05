from __future__ import annotations

import numpy as np

# to run programm
# python3 Dana_Oborenko/assignment5.py

def task1_create_arrays() -> None:
    print("\n--- Task 1: Create NumPy Arrays ---")
    arr_1d = np.arange(1, 11)  # 1..10
    arr_2d = np.arange(1, 10).reshape(3, 3)  # 3x3

    print("1D array:", arr_1d)
    print("1D shape:", arr_1d.shape)

    print("\n2D array (3x3):\n", arr_2d)
    print("2D shape:", arr_2d.shape)


def task2_reshape_practice() -> None:
    print("\n--- Task 2: Reshape Practice ---")
    arr = np.arange(1, 13)  # 12 elements

    reshaped_3x4 = arr.reshape(3, 4)
    reshaped_2x6 = arr.reshape(2, 6)

    print("Original:", arr, "shape:", arr.shape)
    print("\nReshaped (3,4):\n", reshaped_3x4, "shape:", reshaped_3x4.shape)
    print("\nReshaped (2,6):\n", reshaped_2x6, "shape:", reshaped_2x6.shape)

    print("\nExplanation:")
    print("- reshape does NOT change the data values.")
    print("- It only changes how NumPy 'views' the same data in memory (new shape).")
    print("- Total number of elements stays the same (12).")


def task3_axis_practice() -> None:
    print("\n--- Task 3: Axis Practice (mean, sum) ---")
    matrix = np.arange(1, 10).reshape(3, 3)
    print("Matrix:\n", matrix)

    mean_axis0 = matrix.mean(axis=0)
    sum_axis1 = matrix.sum(axis=1)

    print("\nMean along axis=0 (column-wise):", mean_axis0)
    print("Sum along axis=1 (row-wise):", sum_axis1)

    print("\nExplanation:")
    print("- axis=0 means 'go down rows' → operations per column.")
    print("- axis=1 means 'go across columns' → operations per row.")


def task4_comparisons() -> None:
    print("\n--- Task 4: Comparison Operations ---")
    rng = np.random.default_rng()
    arr = rng.integers(low=0, high=100, size=10)

    mean_value = arr.mean()
    above_mean = arr[arr > mean_value]

    print("Array:", arr)
    print("Mean:", mean_value)
    print("Values > mean:", above_mean)


def task5_masking_filtering() -> None:
    print("\n--- Task 5: Masking and Filtering ---")
    arr = np.arange(0, 21)

    evens = arr[arr % 2 == 0]
    divisible_by_3 = arr[arr % 3 == 0]

    print("Array 0..20:", arr)
    print("Even numbers:", evens)
    print("Divisible by 3:", divisible_by_3)


class MatrixTool:
    def __init__(self, matrix: np.ndarray):
        self.matrix = np.array(matrix)

    def row_mean(self) -> np.ndarray:
        """Return row-wise means (axis=1)."""
        return self.matrix.mean(axis=1)

    def above_threshold(self, t: float) -> np.ndarray:
        """Return values that are > t (flattened)."""
        return self.matrix[self.matrix > t]


def task6_oop_numpy() -> None:
    print("\n--- Task 6: Small OOP + NumPy ---")
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

    tool = MatrixTool(matrix)

    print("Matrix:\n", matrix)
    print("Row-wise means:", tool.row_mean())
    print("Values above threshold 5:", tool.above_threshold(5))


def task7_mini_challenge() -> None:
    print("\n--- Task 7: Mini Challenge (Thresholding) ---")
    rng = np.random.default_rng()
    m = rng.random((5, 5))  # values in [0, 1)

    print("Original 5x5 matrix:\n", m)

    thresholded = m.copy()
    thresholded[thresholded < 0.5] = 0
    thresholded[thresholded >= 0.5] = 1

    print("\nThresholded matrix (<0.5 → 0, >=0.5 → 1):\n", thresholded)


def main() -> None:
    task1_create_arrays()
    task2_reshape_practice()
    task3_axis_practice()
    task4_comparisons()
    task5_masking_filtering()
    task6_oop_numpy()
    task7_mini_challenge()


if __name__ == "__main__":
    main()

