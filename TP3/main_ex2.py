import csv
import numpy as np
from perceptron.linear_perceptron import LinearPerceptron
from perceptron.non_linear_perceptron import NonLinearPerceptron


def normalize(output):
    min_expected = min(output)
    max_expected = max(output)
    return list(map(lambda x: (x - min_expected) / (max_expected - min_expected), output))


def import_data(file):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter=" ")
    data = []
    for row in csv_reader:
        entry = [float(a) for a in row if a != '']
        data.append(entry)
    return data


inputs = import_data('data/ex2_training_set')
outputs = normalize(np.array(import_data('data/ex2_expected_output'), dtype=float))
learning_rate = 0.02
training_set = inputs[:180]
test_set = np.array(inputs[180:], dtype=float)
expected_output = outputs[:180]
test_outputs = np.array(outputs[180:], dtype=float)
iterations = 10000
perceptron = NonLinearPerceptron(training_set, expected_output, learning_rate)
perceptron.train(iterations)

results = np.array(perceptron.get_results(test_set), dtype=float)
print('Expected      Result')

for i in range(results.size):
    print(f'{test_outputs[i]}    {results[i]}')
