import numpy as np

import ex3_utils
from TP3.constants import FIRST, MIDDLE, LAST
from multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron


def ex2(learning_rate, epochs, layers):
    inputs = ex3_utils.import_data('data/ex3_23_training_set', 7)
    outputs = np.array(ex3_utils.import_data('data/ex3_2_expected_output', 1), dtype=float)

    training_set = np.array(inputs)
    expected_output = np.array(outputs)

    perceptron = ex3_utils.create_multilayer_perceptron_and_train(training_set, expected_output, learning_rate, epochs, layers)
    results = np.array(perceptron.test_input(training_set), dtype=float)
    print('Expected      Result')

    for i in range(results.size):
        print(f'{np.round(expected_output[i])[0]}\t    {np.abs(np.round(results[i])[0])}')
