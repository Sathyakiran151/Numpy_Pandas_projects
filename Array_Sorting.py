import numpy as np

arr = np.array([5, 2, 8, 1, 9])

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("Original:", arr)
print("Ascending:", ascending)
print("Descending:", descending)