from sympy.physics.hydrogen import Psi_nlm, R_nl
from sympy.physics import hydrogen
from sympy import Symbol, symbols, Matrix
from sympy import integrate, conjugate, pi, sin
r_axis = Matrix(r_axis)
phi, theta = symbols('phi theta', real=True)
r = Symbol('r', real=True, positive=True)
Z, n, l, m = symbols('Z n l m', positive=True, integer=True, real=True)
n = 3
l = 1
m = 0
wf = R_nl(n, l, r, Z) #Psi_nlm(n, l, m, r, phi, theta)
abs_sqrd = wf*conjugate(wf)
