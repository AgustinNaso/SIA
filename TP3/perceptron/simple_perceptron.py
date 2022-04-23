from perceptron import Perceptron
import numpy as np


class SimplePerceptron(Perceptron):

    def __init__(self, training_set, expected_output):
        super().__init__(training_set, expected_output)

    # Simple Perceptron training algorithm
    def train(self):
        i = 0
        error = 1
        p = len(self.training_set)
        self.error_min = p * 2
        w = np.zeros(len(self.training_set[0]))
