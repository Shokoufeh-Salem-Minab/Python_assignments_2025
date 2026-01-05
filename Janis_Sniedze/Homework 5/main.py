try:
	import numpy as np  # import numpy for array and numerical operations used in tasks
except ImportError:
	print("NumPy is required. Install with: pip install numpy")  # inform user about missing dependency
	raise  # re-raise to stop execution when numpy is missing


# numpy exercises


def task1():
	print("\nTask 1 — Create NumPy Arrays")  # prints a section header to separate output for readability
	arr1 = np.arange(1, 11)  # create a simple 1..10 1D array for basic demonstrations
	arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # create a small 3x3 matrix for 2D examples
	print("1D array:", arr1)  # show the 1D array values
	print("shape:", arr1.shape)  # show its shape metadata
	print("2D array:\n", arr2)  # display the 2D matrix so its layout is visible
	print("shape:", arr2.shape)  # display the shape of the 2D matrix


def task2():
	print("\nTask 2 — Reshape Practice")  # header for reshape examples
	a = np.arange(12)  # create a 1D array of length 12 to reshape into different views
	r1 = a.reshape((3, 4))  # reshape into 3 rows and 4 columns
	r2 = a.reshape((2, 6))  # reshape into 2 rows and 6 columns
	print("original (1D):", a)  # show the flat array
	print("reshaped (3,4):\n", r1)  # show the 3x4 view to illustrate shape change
	print("reshaped (2,6):\n", r2)  # show the 2x6 view to illustrate alternative reshape
	print("note: reshape changes the array's shape metadata and may return a view sharing the same buffer.")  # explain reshape behavior concisely


def task3():
	print("\nTask 3 — Axis Practice (mean, sum)")  # header for axis aggregation examples
	m = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])  # create a float matrix to compute means and sums
	meanAxis0 = m.mean(axis=0)  # compute column-wise mean to illustrate axis=0 aggregation
	sumAxis1 = m.sum(axis=1)  # compute row-wise sums to illustrate axis=1 aggregation
	print("matrix:\n", m)  # display the matrix used for calculations
	print("mean along axis=0 (columns):", meanAxis0)  # print computed column means
	print("sum along axis=1 (rows):", sumAxis1)  # print computed row sums


def task4():
	print("\nTask 4 — Comparison Operations")  # header for comparison and boolean masking examples
	rng = np.random.default_rng()  # create a random number generator instance for reproducible patterns when seeded
	arr = rng.integers(0, 100, size=10)  # generate ten random integers in [0,100)
	meanVal = arr.mean()  # compute the mean to use as threshold
	mask = arr > meanVal  # boolean mask identifying values above the mean
	greater = arr[mask]  # apply mask to extract elements greater than mean
	print("random ints:", arr)  # show the random values
	print("mean:", meanVal)  # show the threshold value
	print("values > mean:", greater)  # show values filtered by the condition


def task5():
	print("\nTask 5 — Masking and Filtering")  # header for basic masking examples
	a = np.arange(21)  # create a 0..20 array to demonstrate modular filtering
	ev = a[a % 2 == 0]  # select even numbers using boolean indexing
	div3 = a[a % 3 == 0]  # select numbers divisible by 3
	print("0..20:", a)  # display the original array
	print("even numbers:", ev)  # display even numbers extracted via mask
	print("divisible by 3:", div3)  # display numbers divisible by three


def task6():
	print("\nTask 6 — Small OOP + NumPy")  # header for small object-oriented helpers using numpy
	mat = np.array([[0.2, 0.8, 0.5], [0.9, 0.1, 0.3]])  # small example matrix to operate on
	tool = matrixTool(mat)  # wrap the matrix in a lightweight helper object
	print("matrix:\n", mat)  # show the matrix to contextualize subsequent results
	print("row means:", tool.rowMean())  # print mean per row using the helper
	print("values above 0.4:", tool.aboveThreshold(0.4))  # extract values above a threshold using the helper


def task7():
	print("\nTask 7 — Mini Challenge")  # header for the small binarization challenge
	rng = np.random.default_rng()  # generator for random floats
	m = rng.random((5, 5))  # create a 5x5 matrix of random floats in [0,1)
	print("original 5x5 random matrix:\n", m)  # show matrix before thresholding
	# thresholding: set entries >=0.5 to 1 and others to 0
	binarized = (m >= 0.5).astype(int)  # perform vectorized thresholding and convert to integer matrix
	print("binarized matrix (threshold 0.5):\n", binarized)  # display the binarized result


class matrixTool:  # lightweight helper class for matrix convenience functions
	def __init__(self, arr: np.ndarray):
		if not isinstance(arr, np.ndarray):
			arr = np.array(arr)  # coerce input to numpy array when needed
		self.mat = arr  # store internal matrix reference

	def rowMean(self):
		return self.mat.mean(axis=1)  # return mean value per row as a 1D array

	def aboveThreshold(self, t):
		return self.mat[self.mat > t]  # return flattened array of values strictly greater than t


def main():
	task1()  # run task 1 demonstration
	task2()  # run task 2 demonstration
	task3()  # run task 3 demonstration
	task4()  # run task 4 demonstration
	task5()  # run task 5 demonstration
	task6()  # run task 6 demonstration
	task7()  # run task 7 demonstration


if __name__ == "__main__":
	main()

