import math
import numpy as np


def Local_Stiffnes_Matrix(a, b, x_left, x_right):
    # x_left and x_right values - left and right parts or element

    h = x_right - x_left
    quad_point = x_left + h / 2

    a_x = a(quad_point) / h
    b_x = b(quad_point) * h / 4
    Kernel = np.array([[a_x + b_x, -a_x + b_x], [-a_x + b_x, a_x + b_x]])
    return Kernel


def AssembleK_Matrix(a, b, x_mesh, quad_points=1):
    global Kernel_Local
    n_points = len(x_mesh)
    n_elements = n_points - 1

    # Degrees of freedom may be larger for FEM with approximation by another polinomes
    deg_of_freedom = 2

    K = np.zeros([n_points, n_points])
    for i in range(n_elements):
        if quad_points == 1:
            Kernel_Local = Local_Stiffnes_Matrix(a, b, x_mesh[i], x_mesh[i + 1])

        for j in range(deg_of_freedom):
            for k in range(deg_of_freedom):
                K[i + j, i + k] += Kernel_Local[j, k]

    return K
