
# solve the AND problem with Numpy

import numpy as np

# create input data (x1, x2, bias)
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

# weights
w = np.array([0.5, 0.5, 0.1])

ytrue = np.array([0, 0, 0, 1])

def neuron(X, w):
    d = np.dot(X, w)
    yhat = (d > 1).astype(int)
    return yhat

yhat = neuron(X, w)

print(yhat)
print(np.all(yhat == ytrue))  # all correct?
