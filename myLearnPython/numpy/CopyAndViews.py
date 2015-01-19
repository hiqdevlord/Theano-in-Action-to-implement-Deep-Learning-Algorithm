# __author__ = 'cjweffort'
# -*- coding: utf-8 -*-

from numpy import *
"""
3 Copies and Views
"""
"""
3.1 No Copy At All
"""
a = arange(12)
b = a
print b is a
b.shape = 3, 4
print 'id(a) = ', id(a)
print 'id(b) = ', id(b)

"""
3.2 View Or Shallow Copy
"""
c = a.view()
print c is a
print 'id(a) = ', id(a)
print 'id(c) = ', id(c)
print c.base is a
print c.flags.owndata
c.shape = 2, 6
print a.shape
c[0, 4] = 1234
print a

s = a[:, 1:3]
s[:] = 10
print a

"""
Deep Copy
"""
d = a.copy()
print d is a
print d.base is a
d[0, 0] = 999
print a
