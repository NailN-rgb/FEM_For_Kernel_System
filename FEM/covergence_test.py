import math
import numpy as np
from FEM_main import Finite_Elements_Method
from eq1 import equation1_init


def covergence(point_num):
    bvp = equation1_init()
    N1 = point_num
    N2 = (point_num - 1) * 2 + 1

    fem1 = Finite_Elements_Method(bvp, N1, None)
    fem2 = Finite_Elements_Method(bvp, N2, None)

    sol1 = fem1.get_solution()
    sol2 = fem2.get_solution()

    sol2tmp = sol2[::2]

    err = sol1 - sol2tmp
    print(max(abs(err))/(1/point_num)**2)


