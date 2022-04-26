def linear_activation(excitation):
    return excitation


def non_linear_activation(excitation, g):
    return g(excitation)
