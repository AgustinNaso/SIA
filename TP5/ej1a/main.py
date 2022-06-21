from seaborn import heatmap
import matplotlib.pyplot as plt
import numpy as np

from TP5.helpers.plot_helper import plot_points, plot_comparison_no_noise
from TP5.resources.fonts import font_1, font_1_header
from TP5.helpers.font_helper import to_bin_array, print_letter
from TP5.helpers.mlp_helper import create_multilayer_perceptron_and_train, round_array, concept_vector


nested_set = np.array(list(map(to_bin_array, font_1)))
sets = np.array(list(map(np.concatenate, nested_set)))
layers = np.array([20, 10, 2, 10, 20])
learning_rate = 0.0005
epoch: int = 5000

saveFolderPath = "/Users/gastondeschant/facultad/SIA-image-tp5/"
testPath = "ej1a-config-20-10-2/"

perceptron = create_multilayer_perceptron_and_train(sets, sets, learning_rate, epoch, layers, 100, momentum=True)
monochromatic_cmap = plt.get_cmap('binary')

# step = 5000
# for i in range(5):
midPoints = perceptron.enc_bulk(sets)
outputs = perceptron.test_input(sets)
#
plot_comparison_no_noise(np.array(outputs), sets, epoch, learning_rate,savePath= saveFolderPath+testPath+f"Compare-e{epoch}lr{learning_rate}.png")
plot_points(np.array(midPoints), np.array(font_1_header),savePath= saveFolderPath+testPath+f"LS-e{epoch}lr{learning_rate}.png")
#     epoch += 5000
#     perceptron.train(epochs=step)

midPoints = perceptron.enc_bulk(sets)
outputs = perceptron.test_input(sets)

plot_comparison_no_noise(np.array(outputs), sets, epoch, learning_rate,
                         savePath=saveFolderPath + testPath + f"Compare-e{epoch}lr{learning_rate}.png")
plot_points(np.array(midPoints), np.array(font_1_header),
            savePath=saveFolderPath + testPath + f"LS-e{epoch}lr{learning_rate}.png")

from_font = 3
to_font = 21

name_vector = [font_1_header[from_font], "", "", "", "", "", "", "", "",
                      font_1_header[to_font]]
plot_points(concept_vector(midPoints[from_font], midPoints[to_font], 10),
            np.array(name_vector))

heatmap(
    round_array(sets[from_font]),
    linewidths=0.2,
    cbar=False,
    square=True,
    cmap=monochromatic_cmap,
    linecolor='k')
plt.title(f"{name_vector[0]} real")
plt.show()
heatmap(
    round_array(sets[to_font]),
    linewidths=0.2,
    cbar=False,
    square=True,
    cmap=monochromatic_cmap,
    linecolor='k')
plt.title(f"{name_vector[len(name_vector)-1]} real")
plt.show()

c_vector = perceptron.dec_bulk(concept_vector(midPoints[from_font], midPoints[to_font], 10))

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

