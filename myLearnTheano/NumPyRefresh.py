# coding: utf-8
# __author__ = cmathx

import numpy


#numpy array 使用
print numpy.asarray([[1., 2], [3, 4], [5, 6]])
print numpy.asarray([[1., 2], [3, 4], [5, 6]]).shape
print numpy.asarray([[1., 2], [3, 4], [5, 6]])[2, 0]

#矩阵相乘
a = numpy.asarray([1.0, 2.0, 3.0])
b = 2.0
print a * b

m1 = numpy.asarray([[1.0], [2.0], [3.0]])
m2 = numpy.asarray([[1., 2], [3, 4], [5, 6]])
print m1 * m2