import numpy as np


class Individual:  # W0 W1 W2 w11 w12  w13  w21 w22  w23  w01  w02
    gen = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    xi1 = np.array([4.4793, -4.0765, -4.0765], dtype=float)
    xi2 = np.array([-4.1793, -4.9218, 1.7664], dtype=float)
    xi3 = np.array([-3.9429, -0, 7689, 4.8830], dtype=float)
    xi = np.array([xi1, xi2, xi3], dtype=object)
    zeta = np.array([0.0, 1.0, 1.0])

    def __init__(self, gen):
        self.gen = gen
        # converting minimization problem into maximization problem to handle selection
        self.fitness = 1/(1 + self.get_fitness())
        self.real_fitness = self.get_fitness()

    def __str__(self):
        string = ""
        for i in range(11):
            string += str(self.gen[i]) + " "
        return string

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__().__eq__(other.to_string())

    def __hash__(self):
        return self.__str__().__hash__()

    def get_max_fitness(self, other):
        return self if self.fitness > other.fitness else other

    def get_min_fitness(self, other):
        return self if self.fitness < other.fitness else other

    def get_fitness(self):
        fitness = 0
        for i in range(3):
            fitness += np.float_power((self.zeta[i] - self.f(self.xi[i])), 2)
        return fitness

    def f(self, xi):
        sum1 = 0.0
        sum2 = 0.0
        for i in range(2):
            for j in range(3):
                sum2 += self.gen[3 + i * 2 + j] * xi[j]
            sum2 -= self.gen[9 + i]
            sum1 += self.gen[i + 1] * g(sum2)
            sum2 = 0
        return g(sum1 - self.gen[0])


def g(x):
    if -700 < x < 700:
        return 1 - (1 / (np.exp(x) + 1))
    return 0 if x < 0 else 1

