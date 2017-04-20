import numpy as np
import sympy as sp
from sympy import init_printing
from sympy.utilities.lambdify import lambdify

init_printing(use_latex=True)

x, nu, t = sp.symbols('x nu t')
phi = (sp.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) + 
       sp.exp(-(x - 4 * t - 2 * np.pi)**2 / (4 * nu * (t+1))))
print('\nphi:'); print(phi)

phiprime = phi.diff(x)
print('\nphiprime:'); print(phiprime)

u = -2 * nu * (phiprime / phi) + 4
print('\nu:'); print(u)

ufunc = lambdify((t, x, nu), u)
print('\nufunc:'); print(ufunc(1,4,3))


