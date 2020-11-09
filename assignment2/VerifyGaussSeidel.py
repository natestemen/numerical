import numpy as np
from GaussSeidel import GaussSeidel

n = 100

A = np.random.rand(n, n)
b = np.random.rand(n)

for i in range(n):
    A[i, i] = sum(A[i, j] for j in range(n))

x = GaussSeidel(A, np.zeros(n), b, 1e-12, 1000)

error = np.linalg.norm(x - np.linalg.solve(A, b))

print(f"total error: {error}")
