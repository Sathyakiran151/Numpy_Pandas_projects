'''🧮 Matrix Diagonal Sum

Problem:
Find sum of diagonal elements'''
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
print(arr)
sum_diagonal=np.trace(arr)
print("Sum of the digonal elements:",sum_diagonal)

# optimal way
import numpy as np
n=int(input("Enter the sixe of the array:"))
arr=np.array(list(map(int,input("Enter numbers:").split()))).reshape(n,n)
print(arr)
sum_diagonal=np.trace(arr)
print("Sum of the digonal elements:",sum_diagonal)
