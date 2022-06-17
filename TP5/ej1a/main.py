from seaborn import heatmap
import matplotlib.pyplot as plt
import numpy as np
from TP5.resources.fonts import font_1
from TP5.helpers.font_helper import to_bin_array, print_letter
from TP5.utils import create_multilayer_perceptron_and_train


def round_array(array):
    for idx in range(len(array)):
        array[idx] = 1 if array[idx] > 0.7 else 0
    return np.array(array).reshape(7, 5)


nested_set = np.array(list(map(to_bin_array, font_1)))
set = np.array(list(map(np.concatenate, nested_set)))
layers = np.array([35, 15, 2, 15, 35])
learning_rate = 0.0005
epoch: int = 1

perceptron = create_multilayer_perceptron_and_train(set, set, learning_rate, epoch, layers, 100)
outputs = perceptron.test_input(set)
# print(output[0])
# output_hm = np.split(np.array(output[0]), 7)
monochromatic_cmap = plt.get_cmap('binary')

print(np.array(outputs[0]).reshape(len(outputs[0]), 1).shape)
print(round_array(outputs[0]))

# for i in range(len(outputs)):
#     # heatmap(
#     #     to_bin_array(font_1[1]),
#     #     linewidths=0.2,
#     #     cbar=False,
#     #     square=True,
#     #     cmap=monocromatic_cmap,
#     #     linecolor='k')
#     # plt.show()
#     print_letter(set[i])
#     print_letter(outputs[i])

heatmap(
    round_array(outputs[0]),
    linewidths=0.2,
    cbar=False,
    square=True,
    cmap=monochromatic_cmap,
    linecolor='k')
plt.show()

