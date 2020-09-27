function VerifyTriDiagonalLU(n)

% (1) generate random A and f for the system Ax=f

% first set the random seed (because we want our results to be reproducible;
% the seed sets a starting point in the sequence of random numbers the program
% uses; different seed gives a different random matrix and right-hand-side)
rng(n)
 
% Generate random columns
a = rand(n,1);
b = rand(n,1);
c = rand(n,1);
f = rand(n,1);

% Convert to a matrix
A = zeros(n);
for i=1:n
  if i~=n
    A(i+1,i) = a(i+1);
    A(i,i+1) = c(i);
  end
  A(i,i) = b(i);
end

% (2) compute x in Ax=f using different algorithms

% compute x using built-in MATLAB solver
x_matlab=A\f;

figure(1)
plot(x_matlab)

% Solve using TriDiagonal LU
x = TriDiagonalSolve(a, b, c, f);

% Compare with the built-in MATLAB solver
err = norm(x - x_matlab)
