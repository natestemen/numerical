from build_laplace_2d import build_laplace_2D
import numpy as np
import matplotlib.pyplot as plt

right_hand_side = (
    lambda x, y: 20 * (np.pi ** 2) * np.sin(2 * np.pi * x) * np.sin(4 * np.pi * y)
)

n = 32
N = n + 2
h = 1 / (n + 1)

b_vec = []

x = np.linspace(0, 1, N)
y = np.linspace(0, 1, N)

xv, yv = np.meshgrid(x, y, indexing="ij")

for i in range(N):
    for j in range(N):
        x_point, y_point = xv[i, j], yv[i, j]
        b_vec.append((-(h ** 2)) * right_hand_side(x_point, y_point))

laplace_matrix = build_laplace_2D(N).toarray()
solution = np.linalg.solve(laplace_matrix, b_vec).reshape((N, N))

solution[0, :] = np.zeros(N)
solution[-1, :] = np.zeros(N)
solution[:, 0] = np.zeros(N)
solution[:, -1] = np.zeros(N)


fig = plt.figure()
ax = fig.gca(projection="3d")

exact = np.sin(2 * np.pi * xv) * np.sin(4 * np.pi * yv)
surf = ax.plot_surface(xv, yv, solution)
surf = ax.plot_surface(xv, yv, exact)
surf = ax.plot_surface(xv, yv, exact - solution)

plt.show()
