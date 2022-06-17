from seaborn import heatmap
import matplotlib.pyplot as plt
import numpy as np
from TP5.resources.fonts import font_2
from TP5.helpers.font_helper import to_bin_array
from TP5.utils import create_multilayer_perceptron_and_train

nested_set = np.array(list(map(to_bin_array, font_2)))
set = np.array(list(map(np.concatenate, nested_set)))
layers = np.array([35, 25, 15, 5, 2, 5, 15, 25, 35])
learning_rate = 0.0005
epoch = 5000

perceptron = create_multilayer_perceptron_and_train(set, set, learning_rate, epoch, layers, 100)
output = perceptron.test_input([set[1]])
# print(output[0])
# output_hm = np.split(np.array(output[0]), 7)
monocromatic_cmap = plt.get_cmap('binary')

heatmap(
    to_bin_array(font_2[1]),
    linewidths=0.2,
    cbar=False,
    square=True,
    cmap=monocromatic_cmap,
    linecolor='k')
plt.show()

def print_letter(array):
    for i in range(7):
        for j in range(5):
            if array[j+i*5] > 0.5:
                print("*",end="")
            else:
                print(" ",end="")
        print("")

print_letter(output[0])

# heatmap(
#     to_bin_array(output_hm),
#     linewidths=0.2,
#     cbar=False,
#     square=True,
#     cmap=monocromatic_cmap,
#     linecolor='k')
# plt.show()

