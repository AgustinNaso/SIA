import numpy as np
from TP5.multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron
from TP5.multilayer_perceptron.constants import *


def create_multilayer_perceptron_and_train(training_set: np.ndarray, expected_output: np.ndarray, learning_rate: float,
                                           epochs: int, layers: np.ndarray, batch_size: int,
                                           momentum=False, adaptive_params=None, noise_factor=None) -> MultilayerPerceptron:
    perceptron = MultilayerPerceptron(training_set, expected_output, learning_rate, adaptive_params, batch_size,
                                      momentum)
    # For basic autoencoder, training set should be the same as expected output
    perceptron.add(len(training_set[0]), FIRST)
    for i in range(len(layers)):
        perceptron.add(layers[i], MIDDLE)
    perceptron.add(len(expected_output[0]), LAST)
    if noise_factor:
        perceptron.train(epochs, noise_factor)
    else:
        perceptron.train(epochs)
    return perceptron
