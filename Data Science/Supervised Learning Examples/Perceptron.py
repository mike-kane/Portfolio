import numpy as np

class Perceptron():

    def __init__(self, weights=np.array([1]), threshold=0):

        self.weights = weights
        self.threshold = threshold



    def activate(self, inputs):
        """Checks if dot product of inputs and weights are greater than the activation
            threshold.  If so, perceptron fires by returning 1. Otherwise, returns 0.
        """

        total = np.sum(np.dot(inputs, self.weights))
        if total >= self.threshold:
            return 1
        else:
            return 0

    def update(self, actual, expected, eta=.1):

        for index, value in enumerate(actual):
            p = self.activate(value)   # get perceptron's prediction for this instance
            error = expected[index] - p  # Compute error rate (error of 0 means it get it right, so weight should not be updated)
            self.weights[index] += eta * error * value # update weights
