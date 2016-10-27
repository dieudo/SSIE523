from sympy import *
from sympy.matrices import *

x, y, a, b, c, d = symbols('x y a b c d')
dx_dt = a*x - b*x*y
dy_dt = -c*y + d*x*y

eqs = solve([dx_dt, dy_dt], [x,y])

model = Matrix([dx_dt, dy_dt])
vars = Matrix([x, y])
j = model.jacobian(vars)

jeq1 = j.subs(zip((x, y), eqs[0]))
print jeq1.eigenvals()

jeq2 = j.subs(zip((x, y), eqs[1]))
print jeq2.eigenvals()
