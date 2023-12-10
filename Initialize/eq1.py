from data import PDEdata


def equation1_init():
    bvp = PDEdata()
    bvp.set_a(lambda x: -1)
    bvp.set_b(lambda x: -1)
    bvp.set_f(lambda x: 0)
    bvp.set_x_a(0)
    bvp.set_x_b(1)
    bvp.set_ua(2)
    bvp.set_ub(3.0862)
    bvp.set_first_bc(0)
    bvp.set_first_bc(1)

    return bvp
