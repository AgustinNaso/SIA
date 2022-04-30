import numpy as np

import ex3_utils
from TP3.constants import FIRST, MIDDLE, LAST
from multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron


def ex2(learning_rate, epochs, layers):
    inputs = ex3_utils.import_data('data/ex3_23_training_set', 7)
    outputs = np.array(ex3_utils.import_data('data/ex3_2_expected_output', 1), dtype=float)

    training_set = np.array(inputs)
    expected_output = np.array(outputs)

    learning_rate = learning_rate
    epochs = epochs
    perceptron = MultilayerPerceptron(training_set, expected_output, learning_rate)
    perceptron.add(35, FIRST)
    for i in range(len(layers)):
        perceptron.add(layers[i], MIDDLE)
    perceptron.add(1, LAST)
    perceptron.train(epochs)

    results = np.array(perceptron.test_input(training_set), dtype=float)
    print('Expected      Result')

    for i in range(results.size):
        print(f'{expected_output[i]}    {results[i]}')
