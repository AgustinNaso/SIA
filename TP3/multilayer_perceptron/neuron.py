import numpy as np


class Neuron:

    exitationValue = 0
    activationValue = 0

    def __init__(self, lastLayerNeurons, g):
        self.wi = np.zeros(lastLayerNeurons)
        self.g = g


    def exitate(self, prevLayer):
        sum = 0
        for j in range(len(self.wi)):
            sum = self.wi[j] * prevLayer[j]
        self.exitationValue = sum
        return sum

    def activate(self):
        self.activationValue = self.g(self.exitationValue)
        return self.activationValue


    # def error(self):


