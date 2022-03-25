import numpy as np


class Individual:
    gen = np.array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    def fitness(self):
        return self.gen[0]
