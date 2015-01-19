# __author__ = 'cjweffort'
# -*- coding: utf-8 -*-

from numpy import *
from math import floor

"""
2 Shape Manipulation
"""

"""
2.1 Changing the shape of an array
"""
a = floor(10 * random.random((3, 4)))
print a.ravel()
a.shape = (6, 2)
print a.transpose()
a.resize((4, 3))
print a
aa = a.reshape((2, 6))
print aa

"""
2.2 Stacking together different arrays
"""
a = floor(10*random.random((2,2)))
b = floor(10*random.random((2,2)))
vstack((a, b))#列叠加
hstack((a, b))#行叠加
column_stack((a, b))
row_stack((a, b))

a = array([4., 2.])
b = array([2., 8.])
print a[:, newaxis]
print column_stack((a[:,newaxis],b[:,newaxis]))
print vstack((a[:,newaxis],b[:,newaxis]))

"""
2.3 Splitting one array into several smaller ones
"""
a = floor(10*random.random((2,12)))
hsplit(a, 3)#等分为3部分
hsplit(a,(3,4))#在第3列和第4列进行切分
