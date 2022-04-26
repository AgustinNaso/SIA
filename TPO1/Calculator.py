import numpy as np
from types import MethodType


xi1 = np.array([4.4793, -4.0765, -4.0765], dtype=float)
xi2 = np.array([-4.1793, -4.9218, 1.7664], dtype=float)
xi3 = np.array([-3.9429, -0.7689, 4.8830], dtype=float)
xi = np.array([xi1, xi2, xi3], dtype=object)
zeta = np.array([0.0, 1.0, 1.0])

def get_error(input):
    fitness = 0
    for i in range(3):
        fitness += np.float_power((zeta[i] - f(input, xi[i])), 2)
    return fitness


def f(input, xi):
    return g(input[1] * g(input[3] * xi[0] + input[4] * xi[1] + input[5] * xi[2] - input[9])
             + input[2] * g(input[6] * xi[0] + input[7] * xi[1] + input[8] * xi[2] - input[10])
             - input[0])


def g(x):
    if -700 < x < 700:
        return np.exp(x) / (1 + np.exp(x))
    return 0 if x < 0 else 1

