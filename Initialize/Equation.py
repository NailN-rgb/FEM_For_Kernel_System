import math
import numpy as np

def equation_initialize():
    a = -1
    b = 0
    f = 0
    x_a = 0
    x_b = 1
    ua = 0
    ub = 1
    bc = np.array([1, 0, ua], [2, 0, ub])



class Equation:
    def __init__(self, a, b, f, x_a, x_b, N, bc_matr):
        self.a = a
        self.b = b
        self.f = f
        self.N = N
        self.x_mesh = self.calculate_mesh(x_a, x_b)
        # boundary conditions matrix
        self.bc_matr = bc_matr

    # Determined to function for adding new mesh types in future
    def calculate_mesh(self, xa, xb):
        x_mesh = np.linspace(xa, xb, self.N)
        return x_mesh

    # WIP
    def print_equation_characteristic(self):
        print(self.a)
        print(self.b)
        print(self.f)