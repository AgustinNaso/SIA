from seaborn import heatmap
import matplotlib.pyplot as plt
import numpy as np
from TP5.resources.fonts import font_1
from TP5.helpers.font_helper import to_bin_array, print_letter
from TP5.utils import create_multilayer_perceptron_and_train

nested_set = np.array(list(map(to_bin_array, font_1)))
set = np.array(list(map(np.concatenate, nested_set)))
layers = np.array([35, 25, 15, 5, 2, 5, 15, 25, 35])
learning_rate = 0.0005
epoch: int = 15000

perceptron = create_multilayer_perceptron_and_train(set, set, learning_rate, epoch, layers, 100)
outputs = perceptron.test_input(set)
# print(output[0])
# output_hm = np.split(np.array(output[0]), 7)
# monocromatic_cmap = plt.get_cmap('binary')

for i in range(len(outputs)):

    # heatmap(
    #     to_bin_array(font_1[1]),
    #     linewidths=0.2,
    #     cbar=False,
    #     square=True,
    #     cmap=monocromatic_cmap,
    #     linecolor='k')
    # plt.show()
    print_letter(set[i])
    print_letter(outputs[i])




# heatmap(
#     to_bin_array(output_hm),
#     linewidths=0.2,
#     cbar=False,
#     square=True,
#     cmap=monocromatic_cmap,
#     linecolor='k')
# plt.show()

