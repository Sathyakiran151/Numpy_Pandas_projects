import numpy as np

# Input
arr = np.array(list(map(int, input("Enter numbers: ").split())))

# Average
avg = np.mean(arr)

# Filter values > average
above_avg = arr[arr > avg]

# Output
print("Array:", arr)
print("Average:", avg)
print("Values above average:", above_avg)