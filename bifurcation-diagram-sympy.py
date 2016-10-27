# drawing bifurcation diagrams using sympy
#
# dx/dt = a x (1 - x/k) (x – (k - x))/k + r (p – x/k)
# or, after rescaling variables:
# dx/dt = x (1 - x) (2x – 1) + r (p – x)

from sympy import *

# setting a parameter value
p = .5

# defining symbols, dynamical equation and its Jacobian
x, r = symbols('x r')
dx_dt = x * (1 - x) * (2 * x - 1) + r * (p - x)

# finding equilibrium points
eqs = solve(dx_dt, x)

# plotting equilibrium points using sympy's plot
plot(eqs[0], eqs[1], eqs[2], (r, 0, 1),
     xlabel = 'r', ylabel = 'x')
