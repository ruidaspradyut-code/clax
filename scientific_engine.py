import math
import numpy as np
import matplotlib.pyplot as plt
import numexpr as ne


    
class Trigonometry:

    @staticmethod
    def sin(angle):
        return math.sin(math.radians(angle))

    @staticmethod
    def cos(angle):
        return math.cos(math.radians(angle))

    @staticmethod
    def tan(angle):
        return math.tan(math.radians(angle))

    @staticmethod
    def asin(value):
        return math.degrees(math.asin(value))

    @staticmethod
    def acos(value):
        return math.degrees(math.acos(value))

    @staticmethod
    def atan(value):
        return math.degrees(math.atan(value))
    

class AdvancedMath:

    @staticmethod
    def log10(value):
        return math.log10(value)

    @staticmethod
    def ln(value):
        return math.log(value)

    @staticmethod
    def log(value, base):
        return math.log(value, base)

    @staticmethod
    def exp(power):
        return math.exp(power)

    @staticmethod
    def power(base, exponent):
        return math.pow(base, exponent)
    
class VectorOperations:

    @staticmethod
    def add(v1, v2):
        return np.add(v1, v2)

    @staticmethod
    def subtract(v1, v2):
        return np.subtract(v1, v2)

    @staticmethod
    def dot_product(v1, v2):
        return np.dot(v1, v2)

    @staticmethod
    def cross_product(v1, v2):
        return np.cross(v1, v2)
    


class MatrixOperations:

    @staticmethod
    def add(m1, m2):
        return np.add(m1, m2)

    @staticmethod
    def subtract(m1, m2):
        return np.subtract(m1, m2)

    @staticmethod
    def multiply(m1, m2):
        return np.matmul(m1, m2)

    @staticmethod
    def determinant(matrix):
        return np.linalg.det(matrix)

    @staticmethod
    def inverse(matrix):

        matrix = np.array(matrix)

        det = np.linalg.det(matrix)

        if det == 0:
            raise ValueError("Matrix is singular and has no inverse")

        return np.linalg.inv(matrix)

    @staticmethod
    def transpose(matrix):
        return np.transpose(matrix)

    @staticmethod
    def rank(matrix):
        return np.linalg.matrix_rank(matrix)
    

class EquationSolver:

    @staticmethod
    def solve_2_variables(A, B):
        """
        A = coefficient matrix
        B = constants
        """

        return np.linalg.solve(A, B)

    @staticmethod
    def solve_3_variables(A, B):
        return np.linalg.solve(A, B)

    @staticmethod
    def solve_quadratic(a, b, c):

        if a == 0:
            raise ValueError("Not a quadratic equation")

        discriminant = b**2 - 4*a*c

        if discriminant > 0:

            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)

            return {
                "type": "real_distinct",
                "roots": (x1, x2)
            }

        elif discriminant == 0:

            x = -b / (2*a)

            return {
                "type": "real_equal",
                "roots": (x,)
            }

        else:

            real = -b / (2*a)
            imag = math.sqrt(-discriminant) / (2*a)

            return {
                "type": "complex",
                "roots": (
                    complex(real, imag),
                    complex(real, -imag)
                )
            }



class GraphEngine:

    @staticmethod
    def plot_function(func, start=-10, end=10, points=1000):

        x = np.linspace(start, end, points)

        y = func(x)

        plt.figure(figsize=(8, 6))
        plt.plot(x, y)

        plt.axhline(0)
        plt.axvline(0)

        plt.grid(True)

        plt.xlabel("x")
        plt.ylabel("y")

        plt.title("Function Graph")

        plt.show()