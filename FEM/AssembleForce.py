import math
import numpy as np


def force_vector_calculation(f, x_mesh, quad_points=1):
    n_points = len(x_mesh)
    F = np.zeros([n_points])

    for i in range(n_points - 1):
        h = x_mesh[i+1] - x_mesh[i]

        if quad_points == 1:
            f_local = f(x_mesh[i] + h/2) * h/2
            F[i] += f_local
            F[i + 1] += f_local

    return F