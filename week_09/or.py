
# solve the OR problem with Numpy

import numpy as np

# create input data (x1, x2, bias)
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

# weights
w = np.array([0.5, 0.5, 1.0])

ytrue = np.array([0, 1, 1, 1])

# dot = w1 * x1 + w2 * x2 + w0 * 1
# first datapoint: dot = 0.5 * 0 + 0.5 * 0 + 1.0 * 1 = 1.0

def neuron(X, w):
    d = np.dot(X, w)
    yhat = (d > 1).astype(int)
    return yhat

yhat = neuron(X, w)

print(yhat)
print(np.all(yhat == ytrue))  # all correct?
