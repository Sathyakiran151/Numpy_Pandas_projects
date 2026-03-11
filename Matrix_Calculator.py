import numpy as np

# Input matrices
print("Enter elements of Matrix A (2x2):")
A = np.array([[int(input()), int(input())],
              [int(input()), int(input())]])

print("Enter elements of Matrix B (2x2):")
B = np.array([[int(input()), int(input())],
              [int(input()), int(input())]])

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

# Addition
print("\nMatrix Addition:")
print(A + B)

# Subtraction
print("\nMatrix Subtraction:")
print(A - B)

# Multiplication
print("\nMatrix Multiplication:")
print(np.dot(A, B))

# Transpose
print("\nTranspose of Matrix A:")
print(np.transpose(A))

# Determinant
print("\nDeterminant of Matrix A:")
print(np.linalg.det(A))

# Inverse
print("\nInverse of Matrix A:")
print(np.linalg.inv(A))