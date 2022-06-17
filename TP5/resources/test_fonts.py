from seaborn import heatmap
import matplotlib.pyplot as plt
from fonts import font_1
from TP5.utils import to_bin_array


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
