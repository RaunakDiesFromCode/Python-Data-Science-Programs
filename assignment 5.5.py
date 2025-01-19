import numpy as np

arr = np.array([10, 2, 8, 4])

# Find index of a specific element
index = np.where(arr == 8)

# Find index of max and min elements
max_index = np.argmax(arr)
min_index = np.argmin(arr)

print("Index of 8:", index)
print("Index of max element:", max_index)
print("Index of min element:", min_index)
