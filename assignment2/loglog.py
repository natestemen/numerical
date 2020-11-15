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

Ns = range(80, 150, 10)
ns = [N ** 2 for N in Ns]
tol = 1e-10

steps = {"gmres": [], "gmresssor": [], "cg": [], "cgssor": []}
for N in Ns:
    print(N)
    n = N ** 2
    A = build_laplace_2D(N)
    b = np.ones(n)
    x0 = np.zeros(n)

    *_, stepsgmres = myGMRES(A, x0, b, tol)
    print("\tdone with GMRES")
    *_, stepsgmresSSOR = myGMRES_SSOR(A, x0, b, tol)
    print("\tdone with GMRES SSOR")
    *_, stepscg = myCG(A, x0, b, tol)
    print("\tdone with CG")
    *_, stepscgSSOR = myCG_SSOR(A, x0, b, tol)
    print("\tdone with CG SSOR")

    steps["gmres"].append(stepsgmres)
    steps["gmresssor"].append(stepsgmresSSOR)
    steps["cg"].append(stepscg)
    steps["cgssor"].append(stepscgSSOR)

fig = plt.figure()
ax = plt.subplot(111)
x = np.log(ns)
ax.plot(x, np.log(steps["gmres"]), label="GMRES")
ax.plot(x, np.log(steps["gmresssor"]), label="GMRES with SSOR")
ax.plot(x, np.log(steps["cg"]), label="CG")
ax.plot(x, np.log(steps["cgssor"]), label="CG with SSOR")

ax.legend()
ax.set_xlabel(r"Log of Problem Size")
ax.set_ylabel(r"Log of # of Iterations")
plt.show()

slope_gmres, _ = np.polyfit(x, np.log(steps["gmres"]), 1)
print(f"GMRES loglog slope: {slope_gmres}")
slope_cg, _ = np.polyfit(x, np.log(steps["cg"]), 1)
print(f"CG loglog slope: {slope_cg}")
slope_gmresssor, _ = np.polyfit(x, np.log(steps["gmresssor"]), 1)
print(f"GMRES with SSOR loglog slope: {slope_gmresssor}")
slope_cgssor, _ = np.polyfit(x, np.log(steps["cgssor"]), 1)
print(f"CG with SSOR loglog slope: {slope_cgssor}")
