import numpy as np
import matplotlib.pyplot as plt


def print_state(state):
    print("State: ")
    for i in range(5):
        print(str(state[0 + i * 5]) + ' ' + str(state[1 + i * 5]) + ' ' + str(state[2 + i * 5]) + ' ' + str(
            state[3 + i * 5]) + ' ' + str(state[4 + i * 5]))


class Hopfield:

    def __init__(self, network_patterns):
        self.network_patterns = np.array(network_patterns)
        self.dimension = len(self.network_patterns[0])
        self.weights = np.dot(np.transpose(self.network_patterns), self.network_patterns) / self.dimension
        np.fill_diagonal(self.weights, 0)

    def train(self, noisy_pattern, iterations):
        state = np.array(noisy_pattern)
        prev_state = np.zeros((self.dimension,))
        energies = [self.energy(state)]
        print_state(state)
        print(f"Energy: {energies[-1]}\n")
        i = 0

        while i < iterations and not np.array_equal(prev_state, state):
            prev_state = state
            state = self.activate(prev_state)
            energies.append(self.energy(state))
            print_state(state)
            print(f"Energy: {energies[-1]}\n")
            i += 1

        new_list = range(0, i+1)
        plt.title("Energy levels per iteration")
        plt.plot([i for i in range(len(energies))], energies)
        plt.ylabel('Energy level')
        plt.xlabel('Iterations')
        plt.xticks(new_list)
        plt.show()

        print(f"Iterations: {i}\n")
        for pattern in self.network_patterns:
            if np.array_equal(pattern, state):
                return True, state
        return False, state

    def activate(self, state):
        result = []
        for i in range(len(self.weights)):
            new_state = np.inner(self.weights[i], state)
            if new_state > 0:
                result.append(1)
            elif new_state < 0:
                result.append(-1)
            else:
                result.append(state[i])
        return result

    def energy(self, state):
        result = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                result += self.weights[i][j] * state[i] * state[j]
        return -0.5 * result
