import numpy as np


def print_section(title):
    """Helper function to print section headers"""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


# ==============================================================================
# TASK 1 - Create NumPy Arrays
# ==============================================================================
def task1_create_arrays():
    print_section("TASK 1 - Create NumPy Arrays")
    
    # Create a 1D array of numbers from 1 to 10
    array_1d = np.arange(1, 11)
    print("\n1D Array (1 to 10):")
    print(array_1d)
    print(f"Shape: {array_1d.shape}")
    print(f"Dimensions: {array_1d.ndim}D")
    
    # Create a 2D array with shape (3,3)
    array_2d = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])
    print("\n2D Array (3x3):")
    print(array_2d)
    print(f"Shape: {array_2d.shape}")
    print(f"Dimensions: {array_2d.ndim}D")
    print(f"Total elements: {array_2d.size}")


# ==============================================================================
# TASK 2 - Reshape Practice
# ==============================================================================
def task2_reshape_practice():
    print_section("TASK 2 - Reshape Practice")
    
    # Create an array of 12 elements
    original_array = np.arange(1, 13)
    print("\nOriginal array (12 elements):")
    print(original_array)
    print(f"Shape: {original_array.shape}")
    print(f"Memory ID: {id(original_array)}")
    
    # Reshape to (3,4)
    reshaped_3x4 = original_array.reshape(3, 4)
    print("\nReshaped to (3, 4):")
    print(reshaped_3x4)
    print(f"Shape: {reshaped_3x4.shape}")
    print(f"Memory ID: {id(reshaped_3x4)}")
    
    # Reshape to (2,6)
    reshaped_2x6 = original_array.reshape(2, 6)
    print("\nReshaped to (2, 6):")
    print(reshaped_2x6)
    print(f"Shape: {reshaped_2x6.shape}")
    print(f"Memory ID: {id(reshaped_2x6)}")
    
    # Explanation
    print("\n" + "-" * 70)
    print("EXPLANATION: Why reshape does NOT change array data")
    print("-" * 70)
    print("• Reshape only changes the VIEW of the data, not the data itself")
    print("• The underlying data remains in the same memory location")
    print("• Only the shape metadata changes (how we interpret the data)")
    print("• All reshaped arrays share the same underlying data")
    print("• Modifying one affects others (they're views, not copies)")
    
    # Demonstrate shared data
    print("\nDemonstration - Shared Data:")
    reshaped_3x4[0, 0] = 999
    print(f"Changed reshaped_3x4[0,0] to 999")
    print(f"Original array first element: {original_array[0]} (also changed!)")


# ==============================================================================
# TASK 3 - Axis Practice (mean, sum)
# ==============================================================================
def task3_axis_practice():
    print_section("TASK 3 - Axis Practice (mean, sum)")
    
    # Create a 3x3 matrix
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    
    print("\n3x3 Matrix:")
    print(matrix)
    
    # Compute mean along axis=0 (column-wise)
    mean_axis0 = np.mean(matrix, axis=0)
    print("\nMean along axis=0 (column-wise):")
    print(mean_axis0)
    print("Calculation: [mean(1,4,7), mean(2,5,8), mean(3,6,9)]")
    print(f"Result: [{mean_axis0[0]:.1f}, {mean_axis0[1]:.1f}, {mean_axis0[2]:.1f}]")
    
    # Compute sum along axis=1 (row-wise)
    sum_axis1 = np.sum(matrix, axis=1)
    print("\nSum along axis=1 (row-wise):")
    print(sum_axis1)
    print("Calculation: [sum(1,2,3), sum(4,5,6), sum(7,8,9)]")
    print(f"Result: [{sum_axis1[0]}, {sum_axis1[1]}, {sum_axis1[2]}]")
    
    # Explanation
    print("\n" + "-" * 70)
    print("EXPLANATION: What each axis means")
    print("-" * 70)
    print("• axis=0: Operations along ROWS (↓ vertically, collapses rows)")
    print("  - Result has shape (columns,)")
    print("  - Computes across different rows for each column")
    print("  - Think: 'Down the rows'")
    print("\n• axis=1: Operations along COLUMNS (→ horizontally, collapses columns)")
    print("  - Result has shape (rows,)")
    print("  - Computes across different columns for each row")
    print("  - Think: 'Across the columns'")
    print("\n• General rule: axis=n means 'collapse dimension n'")


# ==============================================================================
# TASK 4 - Comparison Operations
# ==============================================================================
def task4_comparison_operations():
    print_section("TASK 4 - Comparison Operations")
    
    # Create an array of 10 random integers
    np.random.seed(42)  # For reproducibility
    random_array = np.random.randint(0, 100, size=10)
    
    print("\nRandom array (10 integers):")
    print(random_array)
    
    # Calculate mean
    mean_value = np.mean(random_array)
    print(f"\nMean value: {mean_value:.2f}")
    
    # Find values greater than the mean
    comparison_mask = random_array > mean_value
    print(f"\nBoolean mask (values > mean):")
    print(comparison_mask)
    
    values_above_mean = random_array[comparison_mask]
    print(f"\nValues greater than mean:")
    print(values_above_mean)
    print(f"Count: {len(values_above_mean)} values")
    
    # Additional comparisons
    print("\nAdditional comparisons:")
    print(f"Values >= 50: {random_array[random_array >= 50]}")
    print(f"Values < 30: {random_array[random_array < 30]}")
    print(f"Values between 30 and 70: {random_array[(random_array >= 30) & (random_array <= 70)]}")


# ==============================================================================
# TASK 5 - Masking and Filtering
# ==============================================================================
def task5_masking_filtering():
    print_section("TASK 5 - Masking and Filtering")
    
    # Create an array 0-20
    array = np.arange(0, 21)
    print("\nOriginal array (0 to 20):")
    print(array)
    
    # Extract even numbers using a Boolean mask
    even_mask = array % 2 == 0
    even_numbers = array[even_mask]
    print("\nEven numbers (using mask):")
    print(f"Mask: {even_mask}")
    print(f"Even numbers: {even_numbers}")
    
    # Extract numbers divisible by 3
    div_by_3_mask = array % 3 == 0
    div_by_3 = array[div_by_3_mask]
    print("\nNumbers divisible by 3:")
    print(f"Mask: {div_by_3_mask}")
    print(f"Numbers: {div_by_3}")
    
    # Combine conditions
    even_and_div_by_3 = array[(array % 2 == 0) & (array % 3 == 0)]
    print("\nNumbers divisible by both 2 AND 3 (i.e., divisible by 6):")
    print(even_and_div_by_3)
    
    # Complex filtering example
    complex_filter = array[(array > 5) & (array < 15) & (array % 2 == 1)]
    print("\nOdd numbers between 5 and 15:")
    print(complex_filter)


# ==============================================================================
# TASK 6 - Small OOP + NumPy
# ==============================================================================
class MatrixTool:
    """A tool class for matrix operations using NumPy"""
    
    def __init__(self, matrix):
        """
        Initialize with a NumPy array
        
        Parameters:
            matrix: numpy.ndarray - Input matrix
        """
        if not isinstance(matrix, np.ndarray):
            matrix = np.array(matrix)
        self.matrix = matrix
    
    def row_mean(self):
        """
        Calculate row-wise means
        
        Returns:
            numpy.ndarray - Array of means for each row
        """
        return np.mean(self.matrix, axis=1)
    
    def above_threshold(self, threshold):
        """
        Return values greater than threshold
        
        Parameters:
            threshold: float - Threshold value
            
        Returns:
            numpy.ndarray - Values above threshold
        """
        return self.matrix[self.matrix > threshold]
    
    def col_mean(self):
        """Calculate column-wise means"""
        return np.mean(self.matrix, axis=0)
    
    def get_shape(self):
        """Get the shape of the matrix"""
        return self.matrix.shape
    
    def display(self):
        """Display the matrix"""
        print(self.matrix)
    
    def __str__(self):
        return f"MatrixTool with shape {self.matrix.shape}\n{self.matrix}"


def task6_oop_numpy():
    print_section("TASK 6 - Small OOP + NumPy")
    
    # Create a sample matrix
    sample_matrix = np.array([[10, 20, 30],
                              [40, 50, 60],
                              [70, 80, 90]])
    
    print("\nSample Matrix:")
    print(sample_matrix)
    
    # Create MatrixTool instance
    tool = MatrixTool(sample_matrix)
    
    print(f"\nMatrixTool Info:")
    print(f"Shape: {tool.get_shape()}")
    
    # Calculate row-wise means
    row_means = tool.row_mean()
    print(f"\nRow-wise means:")
    print(row_means)
    print("Explanation: [mean(10,20,30), mean(40,50,60), mean(70,80,90)]")
    print(f"Result: [{row_means[0]:.1f}, {row_means[1]:.1f}, {row_means[2]:.1f}]")
    
    # Calculate column-wise means
    col_means = tool.col_mean()
    print(f"\nColumn-wise means:")
    print(col_means)
    
    # Get values above threshold
    threshold = 45
    above_thresh = tool.above_threshold(threshold)
    print(f"\nValues above threshold ({threshold}):")
    print(above_thresh)
    
    # Test with different matrix
    print("\n" + "-" * 70)
    print("Testing with random matrix:")
    random_matrix = np.random.randint(1, 100, size=(4, 5))
    tool2 = MatrixTool(random_matrix)
    print(tool2)
    print(f"\nRow means: {tool2.row_mean()}")
    print(f"Values > 50: {tool2.above_threshold(50)}")


# ==============================================================================
# TASK 7 - Mini Challenge (Thresholding + Masking)
# ==============================================================================
def task7_mini_challenge():
    print_section("TASK 7 - Mini Challenge (Thresholding + Masking)")
    
    # Generate a 5x5 random matrix
    np.random.seed(123)  # For reproducibility
    matrix = np.random.rand(5, 5)
    
    print("\nOriginal 5x5 Random Matrix (values between 0 and 1):")
    print(matrix)
    print(f"\nMin value: {matrix.min():.4f}")
    print(f"Max value: {matrix.max():.4f}")
    print(f"Mean value: {matrix.mean():.4f}")
    
    # Create a copy for thresholding
    thresholded_matrix = matrix.copy()
    
    # Method 1: Using boolean indexing
    print("\n" + "-" * 70)
    print("Method 1: Using Boolean Indexing")
    print("-" * 70)
    thresholded_matrix[thresholded_matrix < 0.5] = 0
    thresholded_matrix[thresholded_matrix >= 0.5] = 1
    
    print("\nThresholded Matrix (< 0.5 → 0, >= 0.5 → 1):")
    print(thresholded_matrix.astype(int))
    
    # Method 2: Using np.where (more elegant)
    print("\n" + "-" * 70)
    print("Method 2: Using np.where (more elegant)")
    print("-" * 70)
    thresholded_matrix_v2 = np.where(matrix >= 0.5, 1, 0)
    
    print("\nThresholded Matrix (using np.where):")
    print(thresholded_matrix_v2)
    
    # Statistics
    print("\n" + "-" * 70)
    print("Statistics:")
    print("-" * 70)
    count_zeros = np.sum(thresholded_matrix == 0)
    count_ones = np.sum(thresholded_matrix == 1)
    print(f"Number of 0s: {count_zeros} ({count_zeros/25*100:.1f}%)")
    print(f"Number of 1s: {count_ones} ({count_ones/25*100:.1f}%)")
    
    # Additional masking examples
    print("\n" + "-" * 70)
    print("Additional Masking Examples:")
    print("-" * 70)
    
    # Create a more complex matrix
    complex_matrix = np.random.randint(-10, 10, size=(4, 4))
    print("\nComplex matrix (integers from -10 to 10):")
    print(complex_matrix)
    
    # Multiple thresholds
    result = np.zeros_like(complex_matrix)
    result[complex_matrix < -5] = -1
    result[(complex_matrix >= -5) & (complex_matrix < 5)] = 0
    result[complex_matrix >= 5] = 1
    
    print("\nMulti-level thresholding:")
    print("  -1 if value < -5")
    print("   0 if -5 <= value < 5")
    print("   1 if value >= 5")
    print(result)


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================
def main():
    """Main function to run all tasks"""
    
    print("\n" + "=" * 70)
    print(" " * 15 + "NumPy PRACTICE HOMEWORK")
    print("=" * 70)
    print("Goal: Understanding NumPy basics through practical tasks")
    print("Topics: arrays, reshaping, axis, comparisons, masking, OOP integration")
    print("=" * 70)
    
    # Run all tasks
    task1_create_arrays()
    task2_reshape_practice()
    task3_axis_practice()
    task4_comparison_operations()
    task5_masking_filtering()
    task6_oop_numpy()
    task7_mini_challenge()
    
    # Final summary
    print("\n" + "=" * 70)
    print(" " * 20 + "HOMEWORK COMPLETED!")
    print("=" * 70)
    print("\nKey Concepts Covered:")
    print("  ✓ Creating and manipulating NumPy arrays")
    print("  ✓ Reshaping and understanding memory views")
    print("  ✓ Understanding axis operations (axis=0, axis=1)")
    print("  ✓ Comparison operations and boolean indexing")
    print("  ✓ Masking and filtering techniques")
    print("  ✓ OOP integration with NumPy")
    print("  ✓ Thresholding and advanced masking")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()