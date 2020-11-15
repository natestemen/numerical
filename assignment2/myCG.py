import numpy as np
from scipy import sparse


def myCG(A, guess, b, tolerance=1e-12, maxIterations=1000):
    n = A.shape[0]
    maxIterations = min(n, maxIterations)

    Rvecs = np.zeros((n, maxIterations))
    Pvecs = np.zeros((n, maxIterations))
    Xvecs = np.zeros((n, maxIterations))
    Xvecs[:, 0] = guess

    r0 = b - A @ guess
    p0 = np.copy(r0)
    Rvecs[:, 0], Pvecs[:, 0] = r0, p0

    residuals = [np.linalg.norm(r0)]
    for k in range(1, maxIterations):
        Aonp = A @ Pvecs[:, k - 1]
        alpha = np.dot(Rvecs[:, k - 1], Rvecs[:, k - 1]) / np.dot(Pvecs[:, k - 1], Aonp)

        xk = Xvecs[:, k - 1] + alpha * Pvecs[:, k - 1]
        rk = Rvecs[:, k - 1] - alpha * Aonp

        residual = np.linalg.norm(rk) / residuals[0]
        residuals.append(residual)
        if residual < tolerance or k == maxIterations - 1:
            return xk, residuals, k

        Xvecs[:, k] = xk
        Rvecs[:, k] = rk

        beta = np.dot(rk, rk) / np.dot(Rvecs[:, k - 1], Rvecs[:, k - 1])
        Pvecs[:, k] = rk + beta * Pvecs[:, k - 1]
    return xk, residuals, maxIterations
