import csv
import numpy as np
from TP3.perceptron.linear_perceptron import LinearPerceptron
from metrics import get_results, cross_validation, accuracy
from constants import *
import matplotlib.pyplot as plt


def normalize(output):
    min_expected = min(output)
    max_expected = max(output)
    return np.array(list(map(lambda x: 2 * ((x - min_expected) / (max_expected - min_expected)) - 1, output)))


def import_data(file):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter=" ")
    data = []
    for row in csv_reader:
        entry = [float(a) for a in row if a != '']
        data.append(entry)
    return data


inputs = import_data('data/ex2_training_set')
outputs = np.array(import_data('data/ex2_expected_output'), dtype=float)
norm_outputs = normalize(np.array(import_data('data/ex2_expected_output'), dtype=float))
learning_rates = [0.005, 0.01, 0.5]
epochs = [100, 500, 1000]
k_folds = [10, 20, 40]

for e in epochs:
    for lr in learning_rates:
        for k in k_folds:
            best_training_set, best_output, best_test_set, best_test_output = cross_validation(k, inputs, outputs,
                                                                                               LINEAR, e, lr)

            perceptron = LinearPerceptron(best_training_set, best_output, lr)
            perceptron.train(e, best_test_set)

            train_accuracies = []
            test_accuracies = []
            for r, s in zip(perceptron.results_train, perceptron.results):
                train_accuracies.append(accuracy(get_results(r, best_output, criteria=lambda x, y: np.abs(x - y) < 0.01)))
                test_accuracies.append(accuracy(get_results(s, best_test_output, criteria=lambda x, y: np.abs(x - y) < 0.01)))

            print(train_accuracies)
            print(test_accuracies)

            x = np.linspace(1, e, e)
            y1 = train_accuracies
            y2 = test_accuracies
            plt.title(f'Variation of accuracy with η = {lr}, epoch = {e} y k = {k}')
            plt.xlabel('Epochs')
            plt.ylabel('Accuracy')
            plt.plot(x, y1, 'o', color='#ffc0cb')
            plt.plot(x, y2, 'o', color='#c3e6fc')
            plt.legend(["Train set", "Test set"], loc="upper right")
            plt.show()
            plt.clf()

            x = np.linspace(1, e, e)
            y = perceptron.errors
            plt.title(f'Variation of error con η = {lr}, epoch = {e} y k = {k}')
            plt.xlabel('Epochs')
            plt.ylabel('Error')
            plt.plot(x, y, label='line', linewidth=2, color='#ffc0cb')
            plt.savefig(f'plots/errors/{lr}-{k}-{e}.png')
            plt.clf()

# perceptron.train(iterations)
