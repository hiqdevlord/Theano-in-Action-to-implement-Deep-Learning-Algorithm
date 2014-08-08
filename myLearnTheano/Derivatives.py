# coding: utf-8
#__author__ = cmathx

from theano import function, theano
from theano import pp
import theano.tensor as T


#computing Gradients
x = T.dscalar('x')
y= x ** 2
gy = T.grad(y, x)

print pp(gy)
f = function([x], gy)
print f(4)


x = T.matrix('x')
s = T.sum(1 / (1 + T.exp(-x)))
gs = T.grad(s, x)
dlogistic = function([[0, 1], [-1, -2]])
print dlogistic

#computing Jacobian
x = T.dvectors('x')
y = x ** 2
J, updates = theano.scan(lambda i, y,x : T.grad(y[i], x), sequences = T.arange(y.shape[0]), non_sequences = [y, x])
f = function([x], J, updates = updates)
print f([4, 4])


