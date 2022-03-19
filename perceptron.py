import numpy as np


class Perceptron:

    def __init__(self, eta=0.10, epochs=50):

        self.eta = eta
        self.epochs = epochs

    def predict(self, x):

        total_stimulation = np.dot(x, self.w)
        y_pred = 1 if total_stimulation > 0 else -1
        return y_pred

    def fit(self, X, y):

        ones = np.ones((X.shape[0], 1))
        X_1 = np.append(X.copy(), ones, 1)

        self.w = np.random.rand(X_1.shape[1])
        print(self.w)

        for e in range(self.epochs):

            for x, y_target in zip(X_1, y):
                y_pred = self.predict(x)
                delta_w = self.eta * (y_target - y_pred) * x
                self.w += delta_w