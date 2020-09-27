
n=1000;
% Generate a random matrix
A = rand(n);
b = rand(n,1);

% Perform the LU decomposition
tic
T = LUFactorization(A);
toc
y = ForwardSubstitution(T, b);
x = BackwardSubstitution(T, y);

% Compare with the built-in MATLAB solver
error_norm = norm(x - A\b)
