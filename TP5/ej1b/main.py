import json
import numpy as np
from TP5.resources.fonts import font_1, font_2, font_3
from TP5.helpers.mlp_helper import create_multilayer_perceptron_and_train
from TP5.helpers.font_helper import to_bits, add_noise
from TP5.helpers.plot_helpers import plot_comparison


with open("config.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

learning_rate = jsonObject["learning_rate"]
epochs = jsonObject["epochs"]
hidden_layers = np.array(jsonObject["hidden_layers"])
batch_size = jsonObject["batch_size"]
momentum = jsonObject["momentum"]
adaptive_eta = jsonObject["adaptive_eta"]
set_momentum = False
adaptive_params = None
fonts = jsonObject["fonts"]
noise_factor = jsonObject["noise_factor"]
noise_coverage = jsonObject["noise_coverage"]

if adaptive_eta == 1:
    adaptive_k = int(jsonObject["adaptive_k"])
    adaptive_inc = int(jsonObject["adaptive_inc"])
    adaptive_dec = int(jsonObject["adaptive_dec"])
    adaptive_params = [adaptive_inc, adaptive_dec, adaptive_k]

if momentum == 1:
    set_momentum = True

if fonts == 1:
    expected_output = to_bits(font_1)
elif fonts == 2:
    expected_output = to_bits(font_2)
else:
    expected_output = to_bits(font_3)

noisy_set = add_noise(expected_output, noise_coverage, noise_factor)

perceptron = create_multilayer_perceptron_and_train(noisy_set, expected_output, learning_rate,
                                                    epochs, hidden_layers, batch_size, noise_coverage=noise_coverage,
                                                    noise_factor=noise_factor)

plot_comparison(noisy_set, expected_output, perceptron, epochs, learning_rate)

# plt.imshow(noisy[20], cmap=plt.get_cmap('gray'))
# plt.show()
