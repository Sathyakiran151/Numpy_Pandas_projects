''' 🔄 Array Reverser (Basic NumPy Project)
🎯 Problem

Take numbers from user and reverse the array'''

import numpy as np
arr=np.array(list(map(int,input("Enter the numbers:").spli())))
result=arr[::-1]
print("The Given array are :",arr)
print("The Reversed array are :",result)
