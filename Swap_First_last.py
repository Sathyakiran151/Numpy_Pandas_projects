import numpy as np

# Input
arr = np.array(list(map(int, input("Enter numbers: ").split())))

# Swap
if len(arr) > 1:
    arr[0], arr[-1] = arr[-1], arr[0]

# Output
print("Array after swapping:", arr)