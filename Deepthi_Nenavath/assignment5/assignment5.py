import numpy as np

def task1_create_arrays():
    """Task 1 – Create NumPy Arrays"""
    array_1d = np.arange(1, 11)
    array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    return array_1d, array_2d

def task2_reshape_practice():
    """Task 2 – Reshape Practice"""
    array_12 = np.arange(1, 13)
    reshaped_3x4 = array_12.reshape(3, 4)
    reshaped_2x6 = array_12.reshape(2, 6)
    return array_12, reshaped_3x4, reshaped_2x6

def task3_axis_practice():
    """Task 3 – Axis Practice"""
    matrix_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    mean_axis0 = np.mean(matrix_3x3, axis=0)
    sum_axis1 = np.sum(matrix_3x3, axis=1)
    return matrix_3x3, mean_axis0, sum_axis1

def task4_comparison_operations():
    """Task 4 – Comparison Operations"""
    random_array = np.random.randint(1, 100, 10)
    array_mean = np.mean(random_array)
    greater_than_mean = random_array[random_array > array_mean]
    return random_array, array_mean, greater_than_mean

def task5_masking_filtering():
    """Task 5 – Masking and Filtering"""
    array_0_20 = np.arange(0, 21)
    even_numbers = array_0_20[array_0_20 % 2 == 0]
    divisible_by_3 = array_0_20[array_0_20 % 3 == 0]
    return array_0_20, even_numbers, divisible_by_3

def task6_oop_numpy():
    """Task 6 – Small OOP + NumPy"""
    class MatrixTool:
        def __init__(self, matrix):
            self.matrix = np.array(matrix)
        
        def row_mean(self):
            return np.mean(self.matrix, axis=1)
        
        def above_threshold(self, t):
            return self.matrix[self.matrix > t]
    
    test_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    tool = MatrixTool(test_matrix)
    return test_matrix, tool.row_mean(), tool.above_threshold(5)

def task7_mini_challenge():
    """Task 7 – Mini Challenge"""
    random_matrix = np.random.rand(5, 5)
    thresholded = np.where(random_matrix < 0.5, 0, 1)
    return random_matrix, thresholded

def main():
    print("=== Task 1 – Create NumPy Arrays ===")
    arr1d, arr2d = task1_create_arrays()
    print("1D Array:", arr1d)
    print("2D Array:\n", arr2d)
    print("Shape:", arr2d.shape)

    print("\n=== Task 2 – Reshape Practice ===")
    arr12, reshaped_3x4, reshaped_2x6 = task2_reshape_practice()
    print("Original array:", arr12)
    print("Reshaped to (3,4):\n", reshaped_3x4)
    print("Reshaped to (2,6):\n", reshaped_2x6)

    print("\n=== Task 3 – Axis Practice ===")
    matrix, mean_axis0, sum_axis1 = task3_axis_practice()
    print("Matrix:\n", matrix)
    print("Mean along axis=0:", mean_axis0)
    print("Sum along axis=1:", sum_axis1)

    print("\n=== Task 4 – Comparison Operations ===")
    rand_arr, mean_val, greater_vals = task4_comparison_operations()
    print("Random array:", rand_arr)
    print("Mean:", mean_val)
    print("Values > mean:", greater_vals)

    print("\n=== Task 5 – Masking and Filtering ===")
    arr_0_20, evens, divisible3 = task5_masking_filtering()
    print("Array 0-20:", arr_0_20)
    print("Even numbers:", evens)
    print("Divisible by 3:", divisible3)

    print("\n=== Task 6 – Small OOP + NumPy ===")
    test_mat, row_means, above_threshold = task6_oop_numpy()
    print("Matrix:\n", test_mat)
    print("Row means:", row_means)
    print("Values > 5:", above_threshold)

    print("\n=== Task 7 – Mini Challenge ===")
    rand_mat, thresholded_mat = task7_mini_challenge()
    print("Original 5x5 random matrix:\n", rand_mat)
    print("Thresholded matrix (<0.5 → 0, ≥0.5 → 1):\n", thresholded_mat)

if __name__ == "__main__":
    main()