import numpy as np

class HopfieldNetwork:
    def __init__(self, num_neurons=784):
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))


    def train_pattern(self, patterns):
        for pattern in patterns:
            pattern = pattern.reshape(self.num_neurons, 1)
            self.weights += np.dot(pattern, pattern.T)

        np.fill_diagonal(self.weights, 0)


    def recall(self, pattern, steps=10, tolerance=1e-6):

        pattern = pattern.copy()
        previous_energy = self.energy(pattern)
        size = pattern.shape[0]

        for _ in range(steps):
            pattern = pattern.reshape(self.num_neurons, 1)
            pattern = np.sign(np.dot(self.weights, pattern))
            pattern = pattern.reshape((size, size))
            current_energy = self.energy(pattern)
            if abs(current_energy - previous_energy) < tolerance:
                break
            previous_energy = current_energy

        pattern = pattern.reshape(28, 28)
        return pattern

    def energy(self, pattern):
        #  - 0.5 time summation of all nodes of the pattern times the coresponding weights
        pattern = pattern.reshape(self.num_neurons, 1)
        return -0.5 * pattern.T @ self.weights @ pattern




