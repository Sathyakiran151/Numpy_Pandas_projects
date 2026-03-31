import numpy as np

# Input
arr = np.array(list(map(int, input("Enter numbers: ").split())))

# Remove duplicates
unique_arr = np.unique(arr)

# Output
print("Original Array:", arr)
print("Array without duplicates:", unique_arr)