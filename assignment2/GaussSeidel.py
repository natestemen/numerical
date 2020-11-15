import numpy as np


def GaussSeidel(A, guess, b, tolerance, maxIterations):
    n = A.shape[0]
    x_old = guess
    for iteration in range(maxIterations):
        x_new = np.zeros_like(x_old)
        for i in range(n):
            new_sum = np.dot(A[i, :i], x_new[:i])
            old_sum = np.dot(A[i, i + 1 :], x_old[i + 1 :])
            x_new[i] = (b[i] - new_sum - old_sum) / A[i, i]
        if np.linalg.norm(x_new - x_old) < tolerance:
            break
        x_old = x_new
    if iteration == maxIterations - 1:
        print("HIT MAX ITERATION: ", maxIterations)
    return x_new
