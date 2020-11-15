import numpy as np
import sys

sys.path.insert(0, "../assignment1/problemThree")

from build_laplace_2d import build_laplace_2D
from myGMRES import myGMRES
from myGMRESSSOR import myGMRES_SSOR
from myCG import myCG
from myCGSSOR import myCG_SSOR

import matplotlib.pyplot as plt

plt.style.use("ggplot")

maxIterations = 400
tolerance = 1e-10

N = 32
n = N ** 2
A = build_laplace_2D(N)

b = np.ones(n)

x0 = np.zeros(n)

x_gmres, resgmres, stepsgmres = myGMRES(A, x0, b, tolerance, maxIterations)
x_gmresSSOR, resgmresSSOR, stepsgmresSSOR = myGMRES_SSOR(
    A, x0, b, tolerance, maxIterations
)
x_cg, rescg, stepscg = myCG(A, x0, b, tolerance, maxIterations)
x_cgSSOR, rescgSSOR, stepscgSSOR = myCG_SSOR(A, x0, b, tolerance, maxIterations)

print(f"Steps for GMRES:           {stepsgmres}")
print("----")
print(f"Steps for GMRES with SSOR: {stepsgmresSSOR}")
print("----")
print(f"Steps for CG:              {stepscg}")
print("----")
print(f"Steps for CG with SSOR:    {stepscgSSOR}")

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(resgmres, label="GMRES")
ax.plot(resgmresSSOR, label="GMRES with SSOR")
ax.plot(rescg, label="CG")
ax.plot(rescgSSOR, label="CG with SSOR")

plt.title("Residual Size")
ax.legend()
ax.set_xlabel(r"Iterations $n$")
ax.set_ylabel(r"Residual $\|\|r_n\|\|$")
plt.yscale("log")
plt.show()
