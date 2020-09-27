# Problem 1 (LU decomposition)
 - [ ] `LUFactorization` function
 - [ ] `ForwardSubstitution` function
 - [ ] `BackwardSubstitution` function
 - [ ] Run (somehow) `VerifyLU.m` and report output

# Problem 2 (Tridiagonal solver)
 - [ ] Derive recurrence relations for `l_i`, `d_i`, and `u_i`.
 - [ ] `TriDiagonalSolve.py`
 - [ ] `VerifyTriDiagonalLU.py`
 - [ ] Asymptotic computational cost for our algorithm
 - [ ] `CompareBVP.py`
 - [ ] Plot full LU, tridiagonal LU and exact solution for N=20.
 - [ ] Run the code and get times for larger N.
 - [ ] Ratio of compute times for N and N/2.

# Problem 3 (2D model problem)
 - [ ] `build_laplace` function
 - [ ] `laplace_zeroBC.py`
 - [ ] test with N = 32 and make mesh plots
 - [ ] `laplace_heat.py`
 - [ ] test with N = 64 and make mesh/contour plots

# Problem 4 (Conditioning of linear systems)
 - [ ] Show the conditioning equality
 - [ ] `Matrix_conditioning.py`
 - [ ] A bunch of small questions about conditioning
 - [ ] Compute inverse of B and a bunch of small questions

# Problem 5 (Determining the base of a floating point number system)
 - [ ] Download and run matlab file
 - [ ] find exact values for `a` and rounded `a`
 - [ ] write down final values of `fl(a + i)`, `\bar{a}`, and `b`

# Problem 6 (QR decomposition by Gram-Schmidt and Householder)
 - [ ] Download `myGramSchmidt.m` and modify it so it's stable to `myGramSchmidtMod.py`
 - [ ] write `myHouseholder.py` with a function `myHouseholder` that returns `Q` and `R`
 - [ ] compare `myGramSchmidt`, `myGramSchmidtMod`, `myHouseholder` with a random matrix
 - [ ] generate the Vandermonde matrix
