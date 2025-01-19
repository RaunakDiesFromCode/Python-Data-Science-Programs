import numpy as np

arr = np.array([10, 2, 8, 4])

# Sort in ascending order
sorted_arr_asc = np.sort(arr)
print("Ascending order:", sorted_arr_asc)

# Sort in descending order
sorted_arr_dsc = np.sort(arr)[::-1]
print("Descending order:", sorted_arr_dsc)
