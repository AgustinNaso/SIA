import numpy as np


def print_state(state):
    print("State: \n")
    print(state)


class Hopfield:

    def __init__(self, network_patterns):
        self.network_patterns = np.array(network_patterns)
        self.dimension = len(self.network_patterns[0])
        self.weights = np.dot(np.transpose(self.network_patterns), self.network_patterns) / self.dimension
        np.fill_diagonal(self.weights, 0)
        print(self.weights)

    def train(self, noisy_pattern, iterations):
        state = np.array(noisy_pattern)
        prev_state = np.zeros((self.dimension,))
        energies = [self.energy(state)]
        print_state(state)
        print(f"Energy: {energies[-1]}")
        i = 0

        while i < iterations and not np.array_equal(prev_state, state):
            prev_state = state
            state = self.activate(prev_state)
            energies.append(self.energy(state))
            print_state(state)
            print(f"Energy: {energies[-1]}")
            i += 1
        print(f"Iterations: {i}")
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


# arr = [[1, 1, -1, -1], [-1, -1, 1, 1]]
# hopfield = Hopfield(arr)
# found, pattern = hopfield.train([1, -1, -1, -1], 10)
# print(f"Result: {found}")
# print(f"Final state: {pattern}")
