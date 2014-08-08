# coding: utf-8
#__author__ = cmathx

import theano
import theano.tensor as T

x = T.dmatrix('x')
y = T.dmatrix('y')
z = x + y

y = x * 2
print type(y.owner)
print y.owner.op.name
print len(y.owner.inputs)
print y.owner.inputs[0]
print y.owner.inputs[1]




