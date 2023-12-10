import numpy as np

class PDEdata:
    def __init__(self):
        self.a = -1
        self.b = 0
        self.f = 0
        self.x_a = 0
        self.x_b = 1
        self.ua = 0
        self.ub = 1
        self.bc = np.array([[1, 0, self.ua], [1, 0, self.ub]])

    def set_a(self, _a):
        self.a = _a

    def set_b(self, _b):
        self.b = _b

    def set_f(self, _f):
        self.f = _f

    def set_x_a(self, _x_a):
        self.x_a = _x_a

    def set_x_b(self, _x_b):
        self.x_b = _x_b

    def set_ua(self, _ua):
        self.ua = _ua

    def set_ub(self, _ub):
        self.ub = _ub

    def set_first_bc(self, side_id):

        if side_id == 0:
            self.bc[0, 0] = 1
            self.bc[0, 2] = self.ua
        elif side_id == 1:
            self.bc[1, 0] = 1
            self.bc[1, 2] = self.ub
        else:
            print("Incorrect Input")

    def set_third_bc(self, side_id, g):

        if side_id == 0:
            self.bc[0, 0] = 3
            self.bc[0, 1] = g
            self.bc[0, 2] = self.ua
        elif side_id == 1:
            self.bc[1, 0] = 3
            self.bc[1, 1] = g
            self.bc[1, 2] = self.ub
        else:
            print("Incorrect Input")