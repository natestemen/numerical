import numpy as np

print("--------------------------")
print("------- P A R T  B -------")
print("--------------------------")

A = np.matrix([[1, -1], [1, 1]])
b = np.matrix([[1], [1]])

x = np.linalg.solve(A, b)

print("solution for unperturbed problem:")
print(x)

print(f"matrix condition number: {np.linalg.cond(A, 2)}")

perturbed_b = np.matrix([[1.001], [1]])
x_perturbed = np.linalg.solve(A, perturbed_b)

print("solution for perturbed problem:")
print(x_perturbed)

delta_x = x - x_perturbed
norm_delta_x = np.linalg.norm(delta_x, 2)
norm_x = np.linalg.norm(x, 2)

delta_b = b - perturbed_b
norm_delta_b = np.linalg.norm(delta_b, 2)
norm_b = np.linalg.norm(b, 2)

relative_cond = (norm_delta_x * norm_b) / (norm_delta_b * norm_x)

print(f"relative condition number of perturbation: {relative_cond}")

print("--------------------------")
print("------- P A R T  C -------")
print("--------------------------")

delta = 10 ** (-10)
B = np.matrix([[1, -1 + delta], [1, -1]])
b = np.matrix([[1], [1]])

x = np.linalg.solve(B, b)

print("solution for unperturbed problem:")
print(x)

print("inverse of B:")
print(np.linalg.inv(B))
print(f"matrix condition number: {np.linalg.cond(B, 2)}")

perturbed_b = np.matrix([[1.001], [1]])
x_perturbed = np.linalg.solve(B, perturbed_b)

print("solution for perturbed problem:")
print(x_perturbed)

delta_x = x - x_perturbed
norm_delta_x = np.linalg.norm(delta_x, 2)
norm_x = np.linalg.norm(x, 2)

delta_b = b - perturbed_b
norm_delta_b = np.linalg.norm(delta_b, 2)
norm_b = np.linalg.norm(b, 2)

relative_cond = (norm_delta_x * norm_b) / (norm_delta_b * norm_x)

print(f"relative condition number of perturbation: {relative_cond}")
