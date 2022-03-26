import numpy as np


class Individual:
    def __init__(self):
        self.gen = np.zeros((11,), dtype=int)

    def fitness(self):
        return self.gen[0]
