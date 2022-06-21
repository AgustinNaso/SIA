import matplotlib.pyplot as plt
import numpy as np
from TP5.multilayer_perceptron.multilayer_perceptron import MultilayerPerceptron


def plot_points(array, labels, savePath=""):
    x, y = zip(*array)
    plt.scatter(x, y)
    for i, text in enumerate(labels):
        plt.annotate(text, (x[i], y[i]))
    # plt.show()
    # if savePath != "":
    plt.savefig(savePath)


def plot_comparison(noisy_set: np.ndarray, expected_output: np.ndarray, mlp: MultilayerPerceptron,
                    epochs: int, learning_rate: float):
    images = []

    for i in range(expected_output.shape[0]):
        images.append(expected_output[i].reshape((7, 5)))

    for j in range(noisy_set.shape[0]):
        images.append(noisy_set[j].reshape((7, 5)))

    predicted = np.array(mlp.test_input(noisy_set))

    error = (np.average((predicted - expected_output) ** 2)) / len(predicted)
    print("Mean square error: " + str(error))

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

def plot_comparison_no_noise(outputs: np.ndarray, expected_output: np.ndarray, epochs: int, learning_rate: float, reshape= (7, 5), savePath=""):
    images = []

    for i in range(expected_output.shape[0]):
        images.append(expected_output[i].reshape(reshape))

    for j in range(outputs.shape[0]):
        images.append(outputs[j].reshape(reshape))

    fig, axes = plt.subplots(2, outputs.shape[0], figsize=reshape)
    for p, ax in enumerate(axes.flat):
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.imshow(images[p])

    axes[0, 15].set_title("Expected Output", fontsize=20)
    axes[1, 15].set_title("Output", fontsize=20)

    plt.suptitle(f"Epochs: {epochs} - Learning Rate: {learning_rate}", fontsize=25)

    # plt.show()
    # if savePath != "":
    plt.savefig(savePath)