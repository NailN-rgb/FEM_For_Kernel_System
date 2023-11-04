import math

import numpy as np
from FEM_main import Finite_Elements_Method


# Solver in FEM directory
# Initialization will be in Initialize directory

#Test
a = lambda x: -1
b = lambda x: -1
f = lambda x: 0
x_a = 0
x_b = 1
ua = 2
ub = 3.0862
bc = np.array([[1, 0, ua], [1, 0, ub]])
N = 100
TrueSolution = lambda x: math.exp(-x) + math.exp(x)

fem = Finite_Elements_Method(a, b, f, x_a, x_b, N, bc, TrueSolution)
fem.Solve_Equation()
fem.Vizualizate_Solution()

