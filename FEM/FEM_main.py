import matplotlib.pyplot as plt
from Equation import Equation
from AssembleKernel import AssembleK_Matrix
from AssembleForce import Force_Vector_Calculation
from BoundaryConditions import Boundary_Conditions


class Finite_Elements_Method(Equation):
    def __init__(self, a, b, f, x_a, x_b, N, bc_matr, TrueSol):
        self.a = a
        self.b = b
        self.f = f
        self.N = N
        self.x_mesh = self.calculate_mesh(x_a, x_b)
        # boundary conditions matrix
        self.bc_matr = bc_matr
        self.TrueSolution = TrueSol
        self.solution = None

    def Solve_Equation(self):
        K_glob = AssembleK_Matrix(self.a, self.b, self.x_mesh)

        F_glob = Force_Vector_Calculation(self.f, self.x_mesh)

        self.solution = Boundary_Conditions(K_glob, F_glob, self.bc_matr)
        self.error_calculate()


    def error_calculate(self):
        t_solution = []
        for x in self.x_mesh:
            t_solution.append(self.TrueSolution(x))

        error = abs(t_solution - self.solution)
        print(max(error))
        return 0


    def Vizualizate_Solution(self):
        plt.plot(self.x_mesh, self.solution)
        plt.show()