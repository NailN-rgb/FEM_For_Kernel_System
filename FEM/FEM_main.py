import matplotlib.pyplot as plt
import numpy as np
from Equation import Equation
from AssembleKernel import assemble_k_matrix
from AssembleForce import force_vector_calculation
from BoundaryConditions import boundary_conditions


class Finite_Elements_Method(Equation):
    def __init__(self, bvp, N, TrueSol):
        self.a = bvp.a
        self.b = bvp.b
        self.f = bvp.f
        self.N = N
        self.x_mesh = self.calculate_mesh(bvp.x_a, bvp.x_b)
        # boundary conditions matrix
        self.bc_matr = bvp.bc
        self.TrueSolution = TrueSol
        self.solution = None

    def solve_equation(self):
        K_glob = assemble_k_matrix(self.a, self.b, self.x_mesh)

        F_glob = force_vector_calculation(self.f, self.x_mesh)

        self.solution = boundary_conditions(K_glob, F_glob, self.bc_matr)

    def get_solution(self):
        self.solve_equation()
        return np.array(self.solution)

    def error_calculate(self):
        t_solution = []
        for x in self.x_mesh:
            t_solution.append(self.TrueSolution(x))

        error = abs(t_solution - self.solution)
        print(max(error))
        return 0

    def visualization_solution(self):
        plt.plot(self.x_mesh, self.solution)
        plt.show()
