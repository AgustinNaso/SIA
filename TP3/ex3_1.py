import numpy as np

import ex3_utils
from constants import FIRST, MIDDLE, LAST
from multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron


def ex1(learning_rate, epochs, layers):
    inputs = ex3_utils.import_data('data/ex3_1_training_set',1)
    outputs = ex3_utils.normalize(np.array(ex3_utils.import_data('data/ex3_1_expected_output',1), dtype=float))

    training_set = np.array(inputs)
    expected_output = np.array(outputs)

    perceptron = ex3_utils.create_multilayer_perceptron_and_train(training_set, expected_output, learning_rate, epochs,
                                                                  layers)
    # test_set = np.array([[1, 1], [-1, 1]], dtype=float)
    # test_outputs = np.array([[1], [-1]], dtype=float)

    results = np.array(perceptron.test_input(training_set), dtype=float)
    print('Expected      Result')

    for i in range(results.size):
        print(f'{expected_output[i]}    {results[i]}')

