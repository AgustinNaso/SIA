from abc import ABC, abstractmethod


class Perceptron(ABC):

    def __init__(self, training_set, expected_output):
        self.training_set = training_set
        self.expected_output = expected_output
        self.error_min = None
        self.w_min = None

    # Training algorithm
    @abstractmethod
    def train(self):
        pass

