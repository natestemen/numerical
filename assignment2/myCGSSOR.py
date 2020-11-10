import numpy as np


def myCG_SSOR(A, guess, b, tolerance, maxIterations):
    """Performs a sequence of preconditioned CG iterations on A x = b with the
    initial estimate x0, using the SSOR preconditioner, until the 2-norm of the
    residual is smaller than tol (relative to the initial residual), or until
    the number of iterations reaches maxit. ‘steps’ is the number of steps that
    were performed, and ‘res’ is a vector with the residual size after every
    interation (the 2-norm of the residual vector)."""

