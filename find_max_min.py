import numpy as np

# Input
arr = np.array(list(map(int, input("Enter numbers: ").split())))

# Find max and min
maximum = np.max(arr)
minimum = np.min(arr)

# Output
print("Array:", arr)
print("Maximum value:", maximum)
print("Minimum value:", minimum)