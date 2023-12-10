import math

import numpy as np
from FEM_main import Finite_Elements_Method
from eq1 import equation1_init
from  covergence_test import covergence

# Solver in FEM directory
# Initialization will be in Initialize directory
N = 100
TrueSolution = lambda x: math.exp(-x) + math.exp(x)

bvp = equation1_init()

fem = Finite_Elements_Method(bvp, N, TrueSolution)
fem.solve_equation()
fem.visualization_solution()

covergence(100)

