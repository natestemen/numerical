function A=build_laplace_2D_kron(N)

% Assemble the system matrix A
e = ones(N,1);
D = spdiags([e -2*e e], -1:1, N, N);
I = speye(N);
A = kron(D,I)+kron(I,D);