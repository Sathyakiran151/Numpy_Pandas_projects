''' 1. 🔢 Missing Number Finder

Problem:
Given numbers from 1 to N, one number is missing.

Example:
[1, 2, 3, 5] → Missing = 4

🧠 Approach:

Create expected sequence using np.arange(1, n+1)
Compare with given array
Use difference (set logic or NumPy filtering)

👉 Key idea: Compare ideal vs actual data'''
import numpy as np 
arr=np.array([1,4,3,7,8,9,10])
#Find the maximum number in the array
n=arr.max()
expected=np.arange(1,n+1)
missing=np.setdiff1d(expected,arr)
print("Missing number in the array is :",missing)