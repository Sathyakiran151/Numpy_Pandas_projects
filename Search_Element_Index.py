''' Search Element Index
🧠 Idea
Check condition → arr == value
Use np.where() to get index'''
import numpy as np
a=np.array(list(map(int,input("Enter the Numbers:").split(','))))
print("the values of array are:",a)
n=int(input("Enter the number to search:"))
index=np.where(a==n)
print("Index of value:", index)