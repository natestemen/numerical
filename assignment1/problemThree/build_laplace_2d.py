import numpy as np
from scipy import sparse


def build_laplace_2D(N):
    dimension = N ** 2
    main_diag = np.full(dimension, -4.0)
    side_diag = np.ones(dimension - 1)
    side_diag[np.arange(1, dimension) % N == 0] = 0
    identity_diag = np.ones(dimension - N)
    diagonals = [main_diag, side_diag, side_diag, identity_diag, identity_diag]
    laplacian = sparse.diags(diagonals, [0, -1, 1, N, -N], shape=(dimension, dimension))
    return laplacian
