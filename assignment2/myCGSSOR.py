import numpy as np
from scipy import sparse
from scipy.sparse import linalg


def myCG_SSOR(A, guess, b, tolerance=1e-12, maxIterations=1000):
    n = A.shape[0]
    maxIterations = min(n, maxIterations)
    omega = 1.9
    AL = -1 * sparse.tril(A, k=-1)
    AU = -1 * sparse.triu(A, k=1)
    AD = sparse.spdiags(A.diagonal(), [0], n, n)
    ADinv = sparse.spdiags([1 / x for x in A.diagonal()], [0], n, n)
    Pinv = (AD - omega * AL) @ ADinv @ (AD - omega * AU) / (omega * (2 - omega))

    Rvecs = np.zeros((n, maxIterations))
    Qvecs = np.zeros((n, maxIterations))
    Pvecs = np.zeros((n, maxIterations))
    Xvecs = np.zeros((n, maxIterations))
    Xvecs[:, 0] = guess

    r0 = b - A @ guess
    q0 = linalg.spsolve(Pinv, r0)
    p0 = np.copy(q0)
    Rvecs[:, 0], Qvecs[:, 0], Pvecs[:, 0] = r0, q0, p0

    residuals = [np.linalg.norm(r0)]
    for k in range(1, maxIterations):
        Aonp = A @ Pvecs[:, k - 1]
        alpha = np.dot(Rvecs[:, k - 1], Qvecs[:, k - 1]) / np.dot(Pvecs[:, k - 1], Aonp)

        xk = Xvecs[:, k - 1] + alpha * Pvecs[:, k - 1]
        rk = Rvecs[:, k - 1] - alpha * Aonp

        residual = np.linalg.norm(rk) / residuals[0]
        residuals.append(residual)
        if residual < tolerance or k == maxIterations - 1:
            return xk, residuals, k

        Xvecs[:, k] = xk
        Rvecs[:, k] = rk

        qk = sparse.linalg.spsolve(Pinv, rk)
        Qvecs[:, k] = qk

        beta = np.dot(rk, qk) / np.dot(Rvecs[:, k - 1], Qvecs[:, k - 1])
        Pvecs[:, k] = qk + beta * Pvecs[:, k - 1]
    return xk, residuals, maxIterations
