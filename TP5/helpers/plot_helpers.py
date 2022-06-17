import matplotlib.pyplot as plt
import numpy as np


def plot_points(array, labels):
    x, y = zip(*array)
    plt.scatter(x, y)
    for i, text in enumerate(labels):
        plt.annotate(text, (x[i], y[i]))
    plt.show()
