# coding: utf-8
#__author__ = cmathx

import theano
import theano.tensor as T
import numpy as np

X = T.matrix("X")
W = T.matrix("W")
b_sym = T.vector("b_sym")

results, updates = theano.scan(lambda v: T.tanh(T.dot(v, W) + b_sym), sequences = X)
complete_elementwise = theano.function(inputs = [X, W, b_sym], outputs = [results])

x = np.eye(2, dtype = theano.config.floatX)
w = np.ones((2, 2), dtype = theano.config.floatX)
b = np.ones((2), dtype = theano.config.floatX)
b[1] = 2

print complete_elementwise(x, w, b)[0]

print np.tanh(x.dot(w) + b)


