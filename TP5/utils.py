import numpy as np
from TP5.multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron
from TP5.multilayer_perceptron.constants import *


def create_multilayer_perceptron_and_train(training_set: np.ndarray, expected_output: np.ndarray, learning_rate: float,
                                           epochs: int, layers: np.ndarray, batch_size: int,
                                           momentum=False, adaptive_params=None) -> MultilayerPerceptron:
    perceptron = MultilayerPerceptron(training_set, expected_output, learning_rate, adaptive_params, batch_size,
                                      momentum)
    perceptron.add(len(training_set[0]), FIRST)
    for i in range(len(layers)):
        perceptron.add(layers[i], MIDDLE)
    perceptron.add(len(expected_output[0]), LAST)
    perceptron.train(epochs)
    return perceptron


def to_bin_array(encoded_character: np.ndarray) -> np.ndarray:
    bin_array = np.zeros((7, 5), dtype=int)
    for row in range(0, 7):
        current_row = encoded_character[row]
        for col in range(0, 5):
            bin_array[row][4 - col] = current_row & 1
            current_row >>= 1
    return bin_array
