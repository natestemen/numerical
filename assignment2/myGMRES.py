import numpy as np
from scipy import sparse


def myGMRES(A, guess, b, tolerance=1e-12, maxIterations=1000):
    n = A.shape[0]
    r0 = b - A @ guess
    rho = np.linalg.norm(r0)
    r0 /= rho
    Q = np.zeros((n, maxIterations))
    Q[:, 0] = r0
    H = sparse.csr_matrix((maxIterations + 1, maxIterations))
    residuals = []
    for iteration in range(maxIterations):
        v = A @ Q[:, iteration]
        for j in range(iteration + 1):
            H[j, iteration] = np.dot(Q[:, j], v)
            v -= H[j, iteration] * Q[:, j]
        norm_v = np.linalg.norm(v)
        H[iteration + 1, iteration] = norm_v
        Q[:, iteration + 1] = v / norm_v

        e = np.zeros(maxIterations + 1)
        e[0] = rho

        y, _, _, residual, *_ = sparse.linalg.lsqr(H, e)
        residual /= rho

        residuals.append(residual)
        if residual < tolerance:
            x = guess + Q @ y
            break

    return x, residuals, iteration + 1
