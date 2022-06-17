from seaborn import heatmap
import numpy as np
import matplotlib.pyplot as plt
from TP5.resources.fonts import font_1


def to_bin_array(encoded_character):
    bin_array = np.zeros((7, 5), dtype=int)
    for row in range(0, 7):
        current_row = encoded_character[row]
        for col in range(0, 5):
            bin_array[row][4 - col] = current_row & 1
            current_row >>= 1
    return bin_array


monocromatic_cmap = plt.get_cmap('binary')

heatmap(
    to_bin_array(font_1[1]),
    linewidths=0.2,
    cbar=False,
    square=True,
    cmap=monocromatic_cmap,
    linecolor='k')
plt.show()

print(to_bin_array(font_1[1]))
