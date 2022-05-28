import matplotlib

from TP4.kohonen.kohonen import Kohonen
from TP4.utils import *
import matplotlib.pyplot as plt

KOHONEN_DIM = 15
KOHONEN_RADIUS = 10
KOHONEN_ETA = 2
KOHONEN_EPOCHS = 15**2


def main():
    countries, inputs = import_data("europe.csv")
    standard_inputs = standarize(inputs)
    kohonen = Kohonen(standard_inputs, KOHONEN_DIM, KOHONEN_RADIUS, KOHONEN_ETA)
    kohonen.initialize_weights()
    activations = kohonen.train(KOHONEN_EPOCHS)
    print(activations)
    fig, ax = plt.subplots(1, 1)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white", "orange", "red"])
    im = ax.imshow(activations, cmap=cmap)
    fig.colorbar(im)
    ax.yaxis.set_major_locator(plt.NullLocator())  # remove y axis ticks
    ax.xaxis.set_major_locator(plt.NullLocator())  # remove x axis ticks
    plt.show()




if __name__ == "__main__":
    main()
