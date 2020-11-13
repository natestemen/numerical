import numpy as np

import sys

sys.path.insert(0, "../assignment1/problemThree")

# from ..assignment1.problemThree.build_laplace_2d import build_laplace_2D
from build_laplace_2d import build_laplace_2D
from myGMRES import myGMRES
from myCGSSOR import myCG_SSOR
from myGMRESSSOR import myGMRES_SSOR


print("**********")

maxIterations = 500
tolerance = 1e-12

N = 8
n = N ** 2
A = build_laplace_2D(N)

x_exact = np.random.rand(n)
b = A @ x_exact

x0 = np.zeros(n)

x_gmres, resgmres, stepsgmres = myGMRES(A, x0, b, tolerance, maxIterations)
x_cgSSOR, rescgSSOR, stepscgSSOR = myCG_SSOR(A, x0, b, tolerance, maxIterations)
x_gmresSSOR, resgmresSSOR, stepsgmresSSOR = myGMRES_SSOR(
    A, x0, b, tolerance, maxIterations
)

print("error for GMRES, # of steps")
error = np.linalg.norm(x_exact - x_gmres)
print(f"error: {error}")
print(f"steps: {stepsgmres}")

print("----")

print("error for CG_SSOR, # of steps")
error = np.linalg.norm(x_exact - x_cgSSOR)
print(f"error: {error}")
print(f"steps: {stepscgSSOR}")

print("----")

print("error for GMRES_SSOR, # of steps")
error = np.linalg.norm(x_exact - x_gmresSSOR)
print(f"error: {error}")
print(f"steps: {stepsgmresSSOR}")

