function  [V,t,neval] = adaptiveRK(F, a,b, U0, h0, tol)
% Runge-Kutta with adaptive step length control
% Input
% F     handle to function that defines the rhs in  U' = F(U,t)
% a, b  range of integration is [a, b]
% U0    column vector of initial values (initial condition)
% h0    initial step length
% tol   tolerance for step length control
% Output
% t     vector of t-values, where the solution is computed
% V     matrix with approximations of the solution, column-based
% neval number of function evaluations F(U,t)

% Runge-Kutta-Fehlberg45 constants.
alpha = [0 1/4 3/8 12/13 1 1/2];
beta = [0 1/4 3/32      1932/2197  439/216   -8/27
        0 0   9/32      -7200/2197 -8        2
        0 0   0         7296/2197  3680/513   -3544/2565
        0 0   0         0          -845/4104 1859/4104
        0 0   0         0          0          -11/40
        0 0 0 0 0 0];
% Weights (for linear combination of slopes)
wA = [25/216 0 1408/2565 2197/4104 -1/5 0]'; 
wB = [16/135 0 6656/12825 28561/56430 -9/50 2/55]'; 

% this is where your code should go...