import math
import numpy as np

def Matrix_Crop(A, F, idx):
    if not idx[0]:
        A = np.delete(A, 0, axis=0)
        A = np.delete(A, 0, axis=1)
        F = np.delete(F, 0, axis=0)

    if not idx[-1]:
        A = np.delete(A, np.shape(A)[0] - 1, axis=0)
        A = np.delete(A, np.shape(A)[1] - 1, axis=1)
        F = np.delete(F, len(F) - 1, axis=0)

    return A,F

def Boundary_Conditions(A, F, bc_matrix):
    n_points = len(A)

    # 3-rd type BC
    if bc_matrix[0, 0] == 3:
        A[0, 0] += bc_matrix[0, 1]
        F[0] += bc_matrix[0, 2]
    if bc_matrix[1, 0] == 3:
        A[n_points - 1, n_points - 1] += bc_matrix[1, 1]
        F[n_points] += bc_matrix[1, 2]

    # 1-st type BC
    y = np.zeros([n_points])  # solution vector
    idx = [True] * n_points

    if bc_matrix[0, 0] == 1:
        idx[0] = False
        y[0] = bc_matrix[0, 2]
        F -= A[:, 0] * y[0]
    if bc_matrix[1, 0] == 1:
        idx[-1] = False
        y[-1] = bc_matrix[1, 2]
        F -= A[:, -1] * y[-1]

    A, F = Matrix_Crop(A, F, idx)
    y[idx] = np.linalg.solve(A, F)

    return y
