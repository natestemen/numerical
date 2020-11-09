import numpy as np


def myGMRES(A, guess, b, tolerance=1e-12, maxIterations=1000):
    n = A.shape[0]
    r0 = b - A @ guess
    rho = np.linalg.norm(r0)
    r0 /= rho
    Q = [0] * maxIterations
    Q[0] = r0
    H = np.zeros((maxIterations + 1, maxIterations))
    residuals = []
    iterations = [guess]
    for iteration in range(maxIterations):
        v = A @ Q[iteration]
        for j in range(iteration):
            H[j, iteration] = np.dot(Q[j], v)
            v -= H[j, iteration] * Q[j]
        H[iteration + 1, iteration] = np.linalg.norm(v)
        Q[iteration + 1] = v / H[iteration + 1, iteration]

        e = np.zeros(maxIterations + 1)
        e[0] = rho

        y = np.linalg.lstsq(H, e, rcond=None)[0]

        x = guess + np.asarray(Q).T @ y

        residual = np.linalg.norm(e - H @ y)
        residuals.append(residual)
        if residual < tolerance:
            break

    return x, residuals, iteration
