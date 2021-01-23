
# solve the XOR problem with Numpy
# XOR: x1 != x2

import numpy as np

# create input data (x1, x2, bias)
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

ytrue = np.array([0, 1, 1, 0])


def neuron(X, w):
    d = np.dot(X, w)
    yhat = (d > 1).astype(int)
    return yhat


def feed_forward(X, wh, wo):
    hidden_out = neuron(X, wh.T)
    bias = np.ones((4,1))
    hidden_outb = np.hstack([hidden_out, bias])
    yhat = neuron(hidden_outb, wo)
    return yhat

# hidden layer:
# 1)
# 2) x2 is set but x1 is not
# out) either 1) or 2) was true
wh = np.array([[1.0, -1.0, 1.0],  # x1 is 1 but x2 is not
               [-1.0, 1.0, 1.0]]) # x2 is 1 but x1 is not
wo = np.array([0.5, 0.5, 1.0])    # OR: either of the hidden neurons results in 1

yhat = feed_forward(X, wh, wo)

print(yhat)
print(np.all(yhat == ytrue))  # all correct?
