import numpy as np
from GaussSeidel import GaussSeidel

n = 100

A = np.random.rand(n, n)
b = np.random.rand(n)

for i in range(n):
    c = 0
    for j in range(n):
        c += A[i, j]
    A[i, i] = c

x = GaussSeidel(A, np.zeros(n), b, 1e-12, 1000)

error = np.linalg.norm(x - np.linalg.solve(A, b), ord=2)

print(f"total error: {error}")
