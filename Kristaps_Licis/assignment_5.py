import numpy as np

# TASK 1 - CREATE NUMPY ARRAYS
print("="*70)
print("TASK 1 - CREATE NUMPY ARRAYS")
print("="*70)

# Create a 1D array of numbers from 1 to 10
array_1d = np.arange(1, 11)
print("\n1D array (1 to 10):")
print(array_1d)

# Create a 2D array with shape (3,3)
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D array (3x3):")
print(array_2d)
print(f"Shape: {array_2d.shape}")

# TASK 2 - RESHAPE PRACTICE
print("\n" + "="*70)
print("TASK 2 - RESHAPE PRACTICE")
print("="*70)

# Given an array of 12 elements
array_12 = np.arange(1, 13)
print("\nOriginal array (12 elements):")
print(array_12)

# Reshape to (3,4)
reshaped_3x4 = array_12.reshape(3, 4)
print("\nReshaped to (3,4):")
print(reshaped_3x4)

# Reshape to (2,6)
reshaped_2x6 = array_12.reshape(2, 6)
print("\nReshaped to (2,6):")
print(reshaped_2x6)

print("\nExplanation: Reshape does not change array data because it only")
print("changes the view/structure of how elements are organized, not the")
print("actual values. The same elements are just arranged differently.")
print(f"Original data id: {id(array_12.data)}")
print(f"Reshaped data id: {id(reshaped_3x4.data)}")

# TASK 3 - AXIS PRACTICE
print("\n" + "="*70)
print("TASK 3 - AXIS PRACTICE (mean, sum)")
print("="*70)

# Create a 3x3 matrix
matrix_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n3x3 matrix:")
print(matrix_3x3)

# Compute mean along axis=0
mean_axis0 = np.mean(matrix_3x3, axis=0)
print("\nMean along axis=0 (column-wise):")
print(mean_axis0)
print("(Average of each column)")

# Compute sum along axis=1
sum_axis1 = np.sum(matrix_3x3, axis=1)
print("\nSum along axis=1 (row-wise):")
print(sum_axis1)
print("(Sum of each row)")

print("\nExplanation:")
print("  axis=0 → operates down the rows (column-wise calculation)")
print("  axis=1 → operates across the columns (row-wise calculation)")

# TASK 4 - COMPARISON OPERATIONS
print("\n" + "="*70)
print("TASK 4 - COMPARISON OPERATIONS")
print("="*70)

# Create an array of 10 random integers
np.random.seed(42)  # For reproducibility
random_array = np.random.randint(1, 100, size=10)
print("\nArray of 10 random integers:")
print(random_array)

# Calculate mean
array_mean = np.mean(random_array)
print(f"\nMean: {array_mean:.2f}")

# Find values greater than the mean
values_above_mean = random_array[random_array > array_mean]
print(f"\nValues greater than mean:")
print(values_above_mean)

# TASK 5 - MASKING AND FILTERING
print("\n" + "="*70)
print("TASK 5 - MASKING AND FILTERING")
print("="*70)

# Create an array 0-20
array_0_20 = np.arange(0, 21)
print("\nArray 0-20:")
print(array_0_20)

# Extract even numbers using Boolean mask
even_mask = array_0_20 % 2 == 0
even_numbers = array_0_20[even_mask]
print("\nEven numbers (using Boolean mask):")
print(even_numbers)

# Extract numbers divisible by 3
divisible_by_3_mask = array_0_20 % 3 == 0
divisible_by_3 = array_0_20[divisible_by_3_mask]
print("\nNumbers divisible by 3:")
print(divisible_by_3)

# TASK 6 - SMALL OOP + NUMPY
print("\n" + "="*70)
print("TASK 6 - SMALL OOP + NUMPY")
print("="*70)

class MatrixTool:
    """Class for matrix operations using NumPy."""
    
    def __init__(self, matrix):
        """
        Initialize with a NumPy array.
        
        Args:
            matrix: NumPy array (2D)
        """
        self.matrix = np.array(matrix)
    
    def row_mean(self):
        """
        Calculate row-wise means.
        
        Returns:
            NumPy array of mean values for each row
        """
        return np.mean(self.matrix, axis=1)
    
    def above_threshold(self, t):
        """
        Return values greater than threshold.
        
        Args:
            t: Threshold value
        
        Returns:
            NumPy array of values > t
        """
        return self.matrix[self.matrix > t]

# Test MatrixTool class
test_matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("\nTest matrix:")
print(test_matrix)

tool = MatrixTool(test_matrix)

print("\nRow-wise means:")
print(tool.row_mean())

threshold = 50
print(f"\nValues above threshold ({threshold}):")
print(tool.above_threshold(threshold))

# TASK 7 - MINI CHALLENGE
print("\n" + "="*70)
print("TASK 7 - MINI CHALLENGE (Thresholding + Masking)")
print("="*70)

# Generate a 5x5 random matrix
np.random.seed(42)
random_matrix = np.random.rand(5, 5)
print("\nOriginal 5x5 random matrix:")
print(random_matrix)

# Create a copy to apply thresholding
thresholded_matrix = random_matrix.copy()

# Replace values < 0.5 with 0
thresholded_matrix[thresholded_matrix < 0.5] = 0

# Replace values >= 0.5 with 1
thresholded_matrix[thresholded_matrix >= 0.5] = 1

print("\nThresholded matrix (0 if < 0.5, 1 if >= 0.5):")
print(thresholded_matrix)

print("\nExplanation: This is called binary thresholding.")
print("It converts continuous values to binary (0 or 1) based on a threshold.")
print("Common in image processing and machine learning!")

# SUMMARY
print("\n" + "="*70)
print("NUMPY PRACTICE COMPLETED!")
print("="*70)
print("\nKey Concepts Covered:")
print("  [DONE] Creating 1D and 2D arrays")
print("  [DONE] Reshaping arrays without changing data")
print("  [DONE] Understanding axis (axis=0 for columns, axis=1 for rows)")
print("  [DONE] Comparison operations and filtering")
print("  [DONE] Boolean masking for data extraction")
print("  [DONE] Integrating NumPy with OOP")
print("  [DONE] Thresholding and masking techniques")
print("="*70)
