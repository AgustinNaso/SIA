import csv
import numpy as np
from perceptron.linear_perceptron import LinearPerceptron
from perceptron.non_linear_perceptron import NonLinearPerceptron


def import_data(file):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter=" ")
    data = []
    for row in csv_reader:
        entry = [float(a) for a in row if a != '']
        data.append(entry)
    return data


training_set = import_data('data/ex2_training_set')
expected_output = import_data('data/ex2_expected_output')
learning_rate = 0.1
iterations = 1000
perceptron = LinearPerceptron(training_set, expected_output, learning_rate)
non_linear = NonLinearPerceptron(training_set, expected_output, learning_rate)
perceptron.train(iterations)
non_linear.train(iterations)
print(non_linear.get_results(np.array([[4.4793, -4.0765, 4.4558], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.883]],
                                dtype=float)))
