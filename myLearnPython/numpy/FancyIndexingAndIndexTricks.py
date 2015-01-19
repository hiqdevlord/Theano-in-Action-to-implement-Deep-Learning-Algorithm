# __author__ = 'cjweffort'
# -*- coding: utf-8 -*-

from numpy import *

"""
4 Fancy indexing and index tricks
"""
"""
4.1 Indexing with Arrays of Indices
"""

#对1维数组进行index选取
a = arange(12) ** 2
i = array([1, 1, 3, 8, 5])
print a[i]
j = array([[3, 4], [9, 7]])
print a[j]

#对2维数组进行index（一个维度）选取
palette = array([[0, 0, 0],
                 [255, 0, 0],
                 [0, 255, 0],
                 [0, 0, 255],
                 [255, 255, 255]])
image = array([[0, 1, 2, 0], [0, 3, 4, 0]])
print palette[image]

#对2维数组进行index（两个维度）选取
a = arange(12).reshape(3, 4)
i = array([[0, 1], [1, 2]])
j = array([[2, 1], [3, 3]])
print a[i, j]#等价于l = a[i,j]; print a[l]
print a[:, j]

#search of the maximum value of time-dependent series
time = linspace(20, 145, 5)
data = sin(arange(20).reshape(5, 4))
ind = data.argmax(axis = 0)
time_max = time[ind]
data_max = data[ind, xrange(data.shape[1])]
all(data_max == data.max(axis = 0))

a = arange(5)
a[[1, 3, 4]] = 0 #按照index对其进行重新赋值
a[[0, 0, 2]] = [1, 2, 3] #index出现重复的值，会对该索引到的值进行多次赋值
a[[0, 0, 2]] += 1 #此时index出现重复的值，不一定会对索引到的值进行多次操作

"""
4.2 Indexing with Boolean Arrays
"""

#First Way
a = arange(12).reshape(3,4)
b = a > 4
print b
print a[b] #1d array with the selected elems
a[b] = 0
print a

#Second Way
a = arange(12).reshape(3,4)
b1 = array([False,True,True])
b2 = array([True, False, True, False])
print a[b1, :]
print a[: b2]
print a[b1, b2]

"""
4.3 The ix_() Function
"""
a = array([2, 3, 4, 5])
b = array([8, 5, 4])
c = array([5, 4, 6, 8, 3])
ax, bx, cx = ix_(a, b, c)
print ax.shape, bx.shape, cx.shape
result = ax + bx * cx
print result
print result[3, 2, 4]
print a[3] + b[2] * c[4]

def ufunc_reduce(ufct, *vectors):
    vs = ix_(*vectors)
    r = ufct.identity
    for v in vs:
        r = ufct(r, v)
    return r
print ufunc_reduce(add, a, b, c)


