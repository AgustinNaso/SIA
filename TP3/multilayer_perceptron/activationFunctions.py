import numpy as np


class Activation:

    @staticmethod
    def sigmoid(x):
        if -700 < x < 700:
            return np.exp(x) / (1 + np.exp(x))
        return 0 if x < 0 else 1

    @staticmethod
    def sigmoid_dx(x):
        if -700 < x < 700:
            return np.exp(x) / np.power(np.exp(x) + 1, 2)
        return 0
