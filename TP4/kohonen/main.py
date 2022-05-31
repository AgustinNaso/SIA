import matplotlib

from TP4.kohonen.kohonen import Kohonen, get_mean_distance_of_neighbors
from TP4.utils import *
import matplotlib.pyplot as plt

KOHONEN_DIM = 4
KOHONEN_RADIUS = KOHONEN_DIM
KOHONEN_ETA = 0.5
KOHONEN_EPOCHS = 500 * 28


def main():
    countries, inputs = import_data("../TP4/europe.csv")
    standard_inputs = standarize(inputs)
    kohonen = Kohonen(standard_inputs, KOHONEN_DIM, KOHONEN_RADIUS, KOHONEN_ETA)
    kohonen.initialize_weights()
    activations, neurons = kohonen.train(KOHONEN_EPOCHS)
    distances = np.zeros(shape=(KOHONEN_DIM, KOHONEN_DIM))
    for i in range(len(neurons)):
        for j in range(len(neurons)):
            distances[i][j] = get_mean_distance_of_neighbors(i, j, neurons)

    fig, ax = plt.subplots(1, 1)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white", "orange", "red"])
    im = ax.imshow(activations, cmap=cmap)
    fig.colorbar(im)
    plt.title(f'Grilla de neuronas de {KOHONEN_DIM}x{KOHONEN_DIM} ')
    ax.yaxis.set_major_locator(plt.NullLocator())  # remove y axis ticks
    ax.xaxis.set_major_locator(plt.NullLocator())  # remove x axis ticks
    plt.show()

    fig, ax = plt.subplots(1, 1)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white", "grey"])
    im = ax.imshow(distances, cmap=cmap)
    fig.colorbar(im)
    plt.title(f'Media de distancia euclidea entre pesos de neuronas vecinas')
    ax.yaxis.set_major_locator(plt.NullLocator())  # remove y axis ticks
    ax.xaxis.set_major_locator(plt.NullLocator())  # remove x axis ticks
    plt.show()


if __name__ == "__main__":
    main()
