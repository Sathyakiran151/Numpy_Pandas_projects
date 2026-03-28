# Sum of Even Numbers Only 
import numpy as np
arr=np.array(list(map(int,input("Enter the Numbers:").split())))
result=np.sum(arr[arr%2==0])
print("Array:", arr)
print("the sum of even of numbers is :",result)