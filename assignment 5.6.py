import numpy as np

arr = np.array([1, 7, 3, 4])

# Find indices of elements greater than 2 and less than 5
indices = np.where((arr > 2) & (arr < 5))

print("Indices are:", indices)
