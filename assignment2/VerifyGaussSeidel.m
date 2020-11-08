function err = VerifyGaussSeidel(n)

% Generate a random matrix
A = rand(n);
b = rand(n,1);

% Make the matrix diagonally dominant
for i=1:n
  c = 0;
  for j=1:n
    c = c + A(i,j);
  end
  A(i,i) = c;
end

% Solve using Gauss-Seidel
x = GaussSeidel(A, zeros(n,1), b, 1e-12, 1000);

% Compare with the built-in MATLAB solver
err = norm(x - A\b);