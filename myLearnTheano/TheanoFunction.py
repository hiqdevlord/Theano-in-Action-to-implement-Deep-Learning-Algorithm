# coding: utf-8
#__author__ = cmathx

import numpy
from theano import *
import theano.tensor as T

############function(parameters:dmatrix)################
#function1
x = T.dmatrix('x')
s = 1 / (1 + T.exp(-x))
logistic = function([x], s)

print logistic([[0, 1], [-1, -2]])


#function2
s2 = (1 + T.tanh(x / 2)) / 2
logistic2 = function([x], s2)
print logistic2([[0, 1], [-1, -2]])

#function(more parameters)
a, b = T.dmatrices('a', 'b')
diff = a- b
abs_diff = abs(diff)
diff_squared = diff ** 2
f = function([a, b], [diff, abs_diff, diff_squared])

print f([[1, 1], [1, 1]], [[0, 1], [2, 3]])

############function(parameters:dscalars)################
#function1(default parameters)
x, y = T.dscalars('x', 'y')
z = x + y
f = function([x, Param(y, default = 1)], z)
print f(33)
print f(33, 2)

#function2(default parameters)
x, y, w = T.dscalars('x', 'y', 'w')
z = (x + y) * w
f = function([x, Param(y, default = 1), Param(w, default = 2, name = 'w_by_name')], z)
print f(33)
print f(33, 2)
print f(33, 0, 1)
print f(33, w_by_name = 1)

