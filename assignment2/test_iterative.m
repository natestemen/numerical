%clear all
clc

disp('**********')

maxit=500;
tol=1e-12;

% consider a small problem with the 2D Laplacian matrix
N=8;
n=N^2;
A=build_laplace_2D_kron(N);

% generate a test problem with a random solution vector x_exact, and compute the
% corresponding right-hand side b
x_exact=rand(n,1);
b=A*x_exact;

% initial guess for the iterative methods
x0=zeros(n,1);

% call the solvers
%[x_cg rescg stepscg]=myCG(A,x0,b,tol,maxit);
[x_gmres resgmres stepsgmres]=myGMRES(A,x0,b,tol,maxit);
[x_cgSSOR rescgSSOR stepscgSSOR]=myCG_SSOR(A,x0,b,tol,maxit);
[x_gmresSSOR resgmresSSOR stepsgmresSSOR]=myGMRES_SSOR(A,x0,b,tol,maxit);

display('error for GMRES, # of steps')
err=norm(x_exact-x_gmres)
stepsgmres=stepsgmres

disp('----')

%display('error for CG, # of steps')
%err=norm(x_exact-x_cg)
%stepscg=stepscg

%disp('----')

display('error for GMRES_SSOR, # of steps')
err=norm(x_exact-x_gmresSSOR)
stepsgmresSSOR=stepsgmresSSOR

disp('----')

display('error for CG_SSOR, # of steps')
err=norm(x_exact-x_cgSSOR)
stepscgSSOR=stepscgSSOR
