import matplotlib.pyplot as plt
import numpy as np

def plot_points(array):
    tags = np.arange(0, len(array))
    x, y = zip(*array)
    plt.scatter(x,y)
    for i, text in enumerate(tags):
        plt.annotate(text, (x[i], y[i]))
    plt.show()
