from seaborn import heatmap
import matplotlib.pyplot as plt
import numpy as np

from TP5.helpers.plot_helper import plot_points
from TP5.resources.fonts import font_1, font_1_header
from TP5.helpers.font_helper import to_bin_array, print_letter
from TP5.helpers.mlp_helper import create_multilayer_perceptron_and_train


def round_array(array):
    for idx in range(len(array)):
        array[idx] = 1 if array[idx] > 0.7 else 0
    return np.array(array).reshape(7, 5)


def concept_vector(point1, point2, point_amount):
    delta_0 = point2[0] - point1[0]
    delta_1 = point2[1] - point1[1]
    vector = []
    for i in range(point_amount):
        vector.append([ point1[0]+delta_0*(i/point_amount), point1[1]+delta_1*(i/point_amount)])
    return np.array(vector)


nested_set = np.array(list(map(to_bin_array, font_1)))
sets = np.array(list(map(np.concatenate, nested_set)))
layers = np.array([35, 20, 2, 20, 35])
learning_rate = 0.0005
epoch: int = 10000

perceptron = create_multilayer_perceptron_and_train(sets, sets, learning_rate, epoch, layers, 100, momentum=True)
midPoints = perceptron.enc_bulk(sets)
print(f'element     mid points')
for i in range(len(midPoints)):
    print(f'{i}    {midPoints[i]}')

decs = perceptron.dec_bulk(midPoints)
print(f'element     errors')
for i in range(len(decs)):
    print(f'{i}    {sets[i] - decs[i]}')

outputs = perceptron.test_input(sets)
monochromatic_cmap = plt.get_cmap('binary')

plot_points(np.array(midPoints), np.array(font_1_header))
plot_points(concept_vector(midPoints[17], midPoints[20], 10), np.array([font_1_header[17], "", "", "", "", "", "", "",  "",
                                                                        font_1_header[20]]))

heatmap(
        round_array(sets[17]),
        linewidths=0.2,
        cbar=False,
        square=True,
        cmap=monochromatic_cmap,
        linecolor='k')
plt.title(f"{6} real")
plt.show()
heatmap(
        round_array(sets[20]),
        linewidths=0.2,
        cbar=False,
        square=True,
        cmap=monochromatic_cmap,
        linecolor='k')
plt.title(f"{5} real")
plt.show()

c_vector = perceptron.dec_bulk(concept_vector(midPoints[17], midPoints[20], 10))

for i in range(len(c_vector)):
    heatmap(
        round_array(c_vector[i]),
        linewidths=0.2,
        cbar=False,
        square=True,
        cmap=monochromatic_cmap,
        linecolor='k')
    plt.title(f"{i} real")
    plt.show()

# for i in range(len(sets)):
#     heatmap(
#         round_array(sets[i]),
#         linewidths=0.2,
#         cbar=False,
#         square=True,
#         cmap=monochromatic_cmap,
#         linecolor='k')
#     plt.title(f"{i} real")
#     plt.show()
#     heatmap(
#         round_array(outputs[i]),
#         linewidths=0.2,
#         cbar=False,
#         square=True,
#         cmap=monochromatic_cmap,
#         linecolor='k')
#     plt.title(f"{i} test")
#     plt.show()
