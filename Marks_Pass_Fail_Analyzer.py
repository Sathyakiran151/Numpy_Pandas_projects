''' 📊 Marks Pass/Fail Analyzer
🧠 Core Idea

Instead of using loops ❌
We use NumPy condition → returns True/False → filter data '''

import numpy as np
# sample data : marks of students

marks=np.array([65,75,86,34,2,43,65,67,87,98])
#condition of pass marks 
result=marks>=35
# the marks of students 
print("Marks of students :",marks)
# the result of pass/fail
print("The result of students :",result)
# filter the students who passed
passed=marks[marks>=35]
print("The students of marks who passed is:",passed)
# filter the students who fail
failed=marks[marks<35]
print("The students of marks who failed is:",failed)
