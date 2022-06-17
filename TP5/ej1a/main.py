from seaborn import heatmap
import matplotlib.pyplot as plt
import numpy as np
from TP5.resources.fonts import font_1
from TP5.helpers.font_helper import to_bin_array, print_letter
from TP5.helpers.mlp_helper import create_multilayer_perceptron_and_train

nested_set = np.array(list(map(to_bin_array, font_1)))
set = np.array(list(map(np.concatenate, nested_set)))
layers = np.array([35, 15, 5, 2, 5, 15, 35])
learning_rate = 0.0005
epoch: int = 5000

perceptron = create_multilayer_perceptron_and_train(set, set, learning_rate, epoch, layers, 100)
outputs = perceptron.test_input(set)


for i in range(len(outputs)):
    print(set[i])
    print(outputs[i])
    print_letter(set[i])
    print_letter(outputs[i])

