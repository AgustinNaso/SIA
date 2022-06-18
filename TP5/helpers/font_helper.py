import numpy as np
import random
from TP5.multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron
import matplotlib.pyplot as plt


def plot_comparison(noisy_set: np.ndarray, expected_output: np.ndarray, mlp: MultilayerPerceptron,
                    epochs: int, learning_rate: float):
    images = []

    for i in range(expected_output.shape[0]):
        images.append(expected_output[i].reshape((7, 5)))

    for j in range(noisy_set.shape[0]):
        images.append(noisy_set[j].reshape((7, 5)))

    predicted = np.array(mlp.test_input(noisy_set))

    error = (np.average((predicted - expected_output) ** 2)) / len(predicted)
    print(error)

    for k in range(predicted.shape[0]):
        images.append(predicted[k].reshape((7, 5)))

    fig, axes = plt.subplots(3, noisy_set.shape[0], figsize=(7, 5))
    for p, ax in enumerate(axes.flat):
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.imshow(images[p])

    axes[0, 15].set_title("Expected Output", fontsize=20)
    axes[1, 15].set_title("Input With Noise", fontsize=20)
    axes[2, 15].set_title("Output", fontsize=20)

    plt.suptitle(f"Epochs: {epochs} - Learning Rate: {learning_rate}", fontsize=25)

    plt.show()



def add_noise(images: np.ndarray, noise_coverage: float, noise_factor: float) -> np.ndarray:
    noisy_set = np.empty((np.size(images, 0), np.size(images, 1)))
    for i in range(images.shape[0]):
        noisy_set[i] = np.array([images[i][j] + random.uniform(0, noise_factor) * (1 if images[i][j] <= 0 else -1)
                                 if random.uniform(0, 1) < noise_coverage else images[i][j]
                                 for j in range(0, images.shape[1])])
    return noisy_set


def to_bits(fonts: np.ndarray) -> np.ndarray:
    results = np.empty((np.size(fonts, 0), np.size(fonts, 1) * 5), dtype=int)
    for i in range(np.size(fonts, 0)):
        results[i] = to_bin_array(fonts[i]).flatten()
    return results


def to_bin_array(encoded_character: np.ndarray) -> np.ndarray:
    bin_array = np.zeros((7, 5), dtype=int)
    for row in range(0, 7):
        current_row = encoded_character[row]
        for col in range(0, 5):
            bin_array[row][4 - col] = current_row & 1
            current_row >>= 1
    return bin_array


def print_letter(array):
    for i in range(7):
        for j in range(5):
            if array[j + i * 5] > 0.5:
                print("*", end="")
            else:
                print(" ", end="")
        print("")
    print("")
