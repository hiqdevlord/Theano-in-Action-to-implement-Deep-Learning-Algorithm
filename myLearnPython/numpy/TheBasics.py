# __author__ = 'cjweffort'
# -*- coding: utf-8 -*-

from numpy import *

"""
1 The Basics
"""
a = arange(15).reshape(3, 5)
#the attribute of matrix
print a
print a.shape
print a.ndim
print a.dtype.name
a.itemsize
type(a)

b = array([6, 7, 8])
print b
print type(b)

"""
1.1 Array Creation
"""
a = array([2, 3, 4])
print a.dtype
b = array([1.1, 2.2, 3.3])
print b.dtype

c = array([[1.5, 2.3], [4,5,6]])
d = array([[1, 2], [3, 4], ], dtype = complex)

#basic initalization of array
zz = zeros((3,4))
oo = ones((2, 3, 4), dtype = int16)
ee = empty((2, 3))
rr = random.random((2, 3))

xx2 = arange(15).reshape(3,5)#初始化序列为0，1，...，14，reshape函数分配矩阵的维度
xx1 = arange(10, 30, 5)#初始值为10，间隔为5
xx = linspace(0, 2*pi, 100)#初始值为0，终止值为2*pi，初始化个数为100
f = sin(xx)

"""
1.2 Basic Operation
"""
A = array( [[1,1], [0,1]] )
B = array( [[2,0], [3,4]] )
print A + B
print A * B
print dot(A, B)
A += B
print A

"""
1.3 Uniersal Functions
"""
B = arange(3)
print exp(B)
print sqrt(B)
C = array([2., -1., 4.])
add(B, C)

"""
1.4 Indexing, Slicing and Iterating
"""
a = arange(10) ** 3
a[:6:2] = -1000  #等价于a[0:6:2] = -1000,第0至第5个元素，每隔1个元素就把值赋值为-1000
print a[::-1]#将a数组倒置

b = arange(20).reshape(5, 4)
print b[2, 3]
print b[0:5, 1]
print b[:, 1]
print b[1:3, :]
print b[-1]

c = arange(24).reshape(2, 3, 4)
print c[1, ...]
print c[..., 2]

print 'row'
for row in c:
    print row
print 'element'
for element in c.flat:
    print element

