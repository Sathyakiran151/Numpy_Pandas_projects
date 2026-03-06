import numpy as np

# Student marks (rows = students, columns = subjects)
marks = np.array([
    [85, 78, 92],
    [70, 88, 75],
    [90, 91, 89],
    [60, 65, 70]
])

# Average marks per student
student_avg = np.mean(marks, axis=1,dtype=int)
print("Average marks of each student:", student_avg)

# Average marks per subject
subject_avg = np.mean(marks, axis=0)
print("Average marks per subject:", subject_avg)

# Highest scorer
topper = np.argmax(student_avg)
print("Topper student index:", topper)

# Lowest scorer
lowest = np.argmin(student_avg)
print("Lowest scorer index:", lowest)