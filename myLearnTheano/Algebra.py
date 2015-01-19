# coding: utf-8
#__author__ = cmathx

#theano.tensor.dscalar
#theano.tensor.dmatrix
#theano.tensor.vector

import theano
import theano.tensor as T
from theano import *
import theano.tensor as T

# Adding two Scalars
x = T.dscalar('x')
y = T.dscalar('y')
z = x + y
f = function([x, y], z)

print f(2, 3)
print f(16.3, 12.1)

print type(x)
print x.type
print T.dscalar
print x.type is T.dscalar

# Adding two Matrices
x = T.dmatrix('x')
y = T.dmatrix('y')
z = x + y
f = function([x, y], z)

print f([[1, 2], [3, 4]], [[10, 20], [30, 40]])

# usage of vector
a= theano.tensor.vector()
out = a + a ** 10
f = theano.function([a], out)
print f([0, 1, 2])

# data type
# byte: bscalar, bvector, bmatrix, brow, bcol, btensor3, btensor4
# 16-bit integers: wscalar, wvector, wmatrix, wrow, wcol, wtensor3, wtensor4
# 32-bit integers: iscalar, ivector, imatrix, irow, icol, itensor3, itensor4
# 64-bit integers: lscalar, lvector, lmatrix, lrow, lcol, ltensor3, ltensor4
# float: fscalar, fvector, fmatrix, frow, fcol, ftensor3, ftensor4
# double: dscalar, dvector, dmatrix, drow, dcol, dtensor3, dtensor4
# complex: cscalar, cvector, cmatrix, crow, ccol, ctensor3, ctensor4

