# __author__ = 'cjweffort'
# -*- coding: utf-8 -*-

from numpy import *

"""
6 Tricks and Tips
"""
"""
6.1 "Automatic" Reshaping
"""
a = arange(30)
a.shape = 2, -1, 3 #这边使用-1，第二个维度的值会自动计算
print a

"""
6.2 Vector Stacking
"""
x = arange(0, 10, 2)
y = arange(5)
m = vstack([x, y]) #将2个长度相同的一维向量叠加为二维向量
xy = hstack([x, y])

"""
6.3 Histograms
"""
import pylab
mu, sigma = 2, 0.5
v = random.normal(mu, sigma, 10000)
pylab.hist(v, bins = 50, normed = 1)
pylab.show()
(n, bins) = histogram(v, bins = 50, normed = True)
pylab.plot(.5 * (bins[1:] + bins[:-1]), n)
pylab.show()