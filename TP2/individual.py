import numpy as np


#                  0  1  2  3   4    5    6  7     8    9    10
class Individual:  # W0 W1 W2 w11 w12  w13  w21 w22  w23  w01  w02
    gen = np.array([0, 1,  2,  3, 4,   5,   6,   7,   8,  9,   10])

    xi = np.array([[4.4793, -4.0765, -4.0765],[-4.1793, -4.9218, 1.7664],[-3.9429, -0, 7689, 4.8830]])
    zeta = np.array([ 0, 1, 1])

    def __init__(self, gen):
        self.gen = gen
        self.fitness = self.get_fitness()
        self.roulette_probability = 0

    def get_fitness(self):
        fitness = 0
        for i in range(3):
            fitness += np.float_power((self.zeta[i] - self.f(self.xi[i])), 2)
        return fitness

    def f(self, xi):
        sum1 = 0
        sum2 = 0
        for i in range(2):
            for j in range(3):
                sum2 += self.gen[3 + i * 2 + j] * xi[j]
            sum2 -= - self.gen[9 + i]
            sum1 += self.gen[i + 1] * g(sum2)
            sum2 = 0
        return g(sum1 - self.gen[0])

    def set_roulette_probability(self, probability):
        self.roulette_probability = probability
        return


def g(x):
    return np.float_power(np.e, x) / (1 + np.float_power(np.e, x))
