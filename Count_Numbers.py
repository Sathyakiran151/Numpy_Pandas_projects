import numpy as np

# Input
arr = np.array(list(map(int, input("Enter numbers: ").split())))

# Counting
positive = np.sum(arr > 0)
negative = np.sum(arr < 0)
zeros = np.sum(arr == 0)

# Output
print("Array:", arr)
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zeros)