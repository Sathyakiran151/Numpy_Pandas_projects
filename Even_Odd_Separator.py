import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Original:", arr)
print("Even numbers:", even)
print("Odd numbers:", odd)