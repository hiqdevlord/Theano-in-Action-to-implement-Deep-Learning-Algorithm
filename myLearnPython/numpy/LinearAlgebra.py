# __author__ = 'cjweffort'
# -*- coding: utf-8 -*-

from numpy import *
from numpy.linalg import *

"""
5 Linear Algebra
"""
"""
5.1 Simple Array Operations
"""
a = array([[1.0, 2.0], [3.0, 4.0]])
a.transpose()
u = eye(2)
print u
j = array([[0.0, -1.0], [1.0, 0.0]])
dot(j, j)
print trace(u) #矩阵的迹

y = array([[5.], [7.]])
print solve(a, y) #求解方程组
print eig(j) #求解矩阵j的特征值和特征向量

"""
5.2 The Matrix Class
"""
A = matrix('1.0 2.0; 3.0 4.0')
print type(A)
print A.T
X = matrix('5.0 7.0')
Y = X.T
print A * Y #矩阵乘法
print A.I #求解矩阵的逆
print solve(A, Y) #求解方程组的解

"""
5.3 Indexing: Comparing Matrices and 2D Arrays
"""
#(1)
A = arange(12)
A.shape = (3, 4)
M = mat(A.copy())
print type(A), " ", type(M)
print A[:, 1]
print A[:, 1].shape
print M[:, 1]
print M[:, 1].shape
A[1:,].take([1, 3], axis = 1)#等价于print A[1:, [1,3]]

#(2)
print A[0,:] > 1
print A[:, A[0,:] > 1]
print M[0, :] > 1
print M[:, M[0,:] > 1]#选取出来的结果和用2D Arrays选取结果不一样
print M[:, M.A[0,:] > 1]


