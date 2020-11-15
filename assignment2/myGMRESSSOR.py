import numpy as np
from scipy import sparse, linalg


def myGMRES_SSOR(A, guess, b, tolerance=1e-12, maxIterations=1000):
    n = A.shape[0]
    maxIterations = min(n, maxIterations)
    omega = 1.9
    AL = -1 * sparse.tril(A, k=-1)
    AU = -1 * sparse.triu(A, k=1)
    AD = sparse.spdiags(A.diagonal(), [0], n, n)
    ADinv = sparse.spdiags([1 / x for x in A.diagonal()], [0], n, n)
    Pinv = (AD - omega * AL) @ ADinv @ (AD - omega * AU) / (omega * (2 - omega))

    r0 = b - A @ guess
    rho = np.linalg.norm(r0)
    r0 /= rho

    Q = np.zeros((n, maxIterations))
    Q[:, 0] = r0
    H = sparse.lil_matrix((maxIterations + 1, maxIterations))
    residuals = []
    for iteration in range(maxIterations):
        z = sparse.linalg.spsolve(Pinv, Q[:, iteration])
        v = A @ z
        for j in range(iteration + 1):
            H[j, iteration] = np.dot(Q[:, j], v)
            v -= H[j, iteration] * Q[:, j]

        norm_v = np.linalg.norm(v)
        H[iteration + 1, iteration] = norm_v
        Q[:, iteration + 1] = v / norm_v

        e = np.zeros(maxIterations + 1)
        e[0] = rho
        y, *_ = linalg.lstsq(H.toarray(), e)
        residual = np.linalg.norm(e - H @ y) / rho
        residuals.append(residual)

        if residual < tolerance or iteration == n - 1:
            w = sparse.linalg.spsolve(Pinv, Q @ y)
            x = guess + w
            break

    return x, residuals, iteration + 1

