import csv
import constants
import numpy as np
from multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron


def import_data(file, data_type):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter=" ")
    data = []
    for row in csv_reader:
        if data_type == constants.MULTIPLE:
            entry = [float(a) for a in row if a != '']
            data.append(entry)
        else:
            data.append(row[-1])
    return data


inputs = import_data('data/ex3_training_set', constants.MULTIPLE)
outputs = np.array(import_data('data/ex3_expected_output', constants.SINGLE), dtype=float)
print(outputs)
learning_rate = 0.02
training_set = inputs[:60]
test_set = np.array(inputs[60:], dtype=float)
expected_output = outputs[:60]
test_outputs = np.array(outputs[60:], dtype=float)
perceptron = MultilayerPerceptron(training_set, expected_output, learning_rate, 1)
perceptron.train(100)
