from build_laplace_2d import build_laplace_2D
import numpy as np
import matplotlib.pyplot as plt

right_hand_side = lambda x, y: 5000 * np.exp(-100 * ((x - 0.25) ** 2 + (y - 0.75) ** 2))

n = 64
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

boundary_term = 300
b_vec = np.array(b_vec).reshape((N, N))
b_vec[0, :] -= boundary_term
b_vec[-1, :] -= boundary_term
b_vec[:, 0] -= boundary_term
b_vec[:, -1] -= boundary_term
b_vec = np.array(b_vec).reshape((N ** 2,))


laplace_matrix = build_laplace_2D(N).toarray()
solution = np.linalg.solve(laplace_matrix, b_vec).reshape((N, N))

max_temp = np.amax(solution)
print(f"maximum temperature acheived: {max_temp}")

fig = plt.figure()
ax = fig.gca(projection="3d")

surf = ax.plot_surface(xv, yv, solution)
cp = plt.contour(xv, yv, solution)

plt.show()
