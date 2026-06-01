import numpy as np
import math


class Matrix:

    @staticmethod
    def madd(m1, m2):
        return np.add(m1, m2)

    @staticmethod
    def msub(m1, m2):
        return np.subtract(m1, m2)

    @staticmethod
    def matrix_multiplication(m1, m2):
        return np.matmul(m1, m2)

    @staticmethod
    def inverse(m1):
        return np.linalg.inv(m1)
    inverce = inverse   # backward-compat alias

    @staticmethod
    def trace(m1):
        return np.trace(m1)

    @staticmethod
    def ma_rank(m1):
        return np.linalg.matrix_rank(m1)

    @staticmethod
    def determinant(m1):
        """ADDED: compute determinant of a square matrix."""
        return np.linalg.det(m1)

    @staticmethod
    def system_of_linear_equation(A, B):
        rank_A   = np.linalg.matrix_rank(A)
        rank_aug = np.linalg.matrix_rank(np.column_stack((A, B)))
        n_vars   = A.shape[1]

        if rank_A == rank_aug == n_vars:
            return "Unique Solution", np.linalg.solve(A, B)
        elif rank_A < rank_aug:
            return "No Solution", None
        else:
            solution, *_ = np.linalg.lstsq(A, B, rcond=None)
            return "Infinite Solutions", solution


class vector:

    @staticmethod
    def vadd(v1, v2):
        return np.add(v1, v2)

    @staticmethod
    def vsub(v1, v2):
        return np.subtract(v1, v2)

    @staticmethod
    def dot_product(v1, v2):
        return np.dot(v1, v2)
    dot_prouct = dot_product  

    @staticmethod
    def cross_product(v1, v2):
        return np.cross(v1, v2)

    @staticmethod
    def magnitude(v1):
        """ADDED: Euclidean norm / magnitude of a vector."""
        return np.linalg.norm(v1)


class angulur_conversion:

    @staticmethod
    def radian_to_degree(radian):
        return math.degrees(radian)

    @staticmethod
    def degree_to_radian(degree):
        return math.radians(degree)


class Tignomatry:

    @staticmethod
    def sin_fun(x):
        return math.sin(x)

    @staticmethod
    def cos_fun(x):
        return math.cos(x)

    @staticmethod
    def tangent(x):
        cos_x = math.cos(x)
        if abs(cos_x) < 1e-12:
            raise ValueError("tan is undefined at this angle (cos = 0)")
        return math.tan(x)

    @staticmethod
    def arcsin(x):
        if not (-1 <= x <= 1):
            raise ValueError("arcsin domain is [-1, 1]")
        return math.asin(x)

    @staticmethod
    def arccos(x):
        if not (-1 <= x <= 1):
            raise ValueError("arccos domain is [-1, 1]")
        return math.acos(x)

    @staticmethod
    def arctan(x):
        return math.atan(x)


class logarthmic:

    @staticmethod
    def natural_log(x):
        if x <= 0:
            raise ValueError("ln requires x > 0")
        return math.log(x)

    @staticmethod
    def log_10(x):
        if x <= 0:
            raise ValueError("log10 requires x > 0")
        return math.log10(x)

    @staticmethod
    def log_base(x, base):
        if x <= 0:
            raise ValueError("log requires x > 0")
        if base <= 0 or base == 1:
            raise ValueError("base must be > 0 and ≠ 1")
        return math.log(x, base)


class expoant:

    @staticmethod
    def power(x, y):
        return math.pow(x, y)

    @staticmethod
    def square_root(x):
        if x < 0:
            raise ValueError("sqrt requires x ≥ 0")
        return math.sqrt(x)


    @staticmethod
    def square(x):
        return x * x

    @staticmethod
    def expnantial(x):
        return math.exp(x)
