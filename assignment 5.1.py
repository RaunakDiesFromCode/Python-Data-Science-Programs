import numpy as np

# Define two 1D arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])

# Add the two arrays
result_array1 = np.add(array1, array2)

# Multiply the two arrays element-wise
result_array2 = np.multiply(array1, array2)

# Display the result
print("Array 1:", array1)
print("Array 2:", array2)
print("Result Array (Array 1 + Array 2):", result_array1)
print("Result Array (Array 1 * Array 2):", result_array2)
