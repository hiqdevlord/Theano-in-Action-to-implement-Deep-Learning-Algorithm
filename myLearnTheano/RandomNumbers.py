# coding: utf-8
#__author__ = cmathx

from theano.tensor.shared_randomstreams import RandomStreams
from theano import function

srng = RandomStreams(seed = 234)
rv_u = srng.uniform((2, 2))
rv_n = srng.normal((2, 2))
f = function([], rv_u)
g = function([], rv_n, no_default_updates = True)
nearly_zeros = function([], rv_u + rv_u- 2 * rv_u)
f_val0 = f()
f_val1 = f()
g_val0 = g()
g_val1 = g()

print "f_val0 = ", f_val0
print "f_val1 = ", f_val1
print "g_val0 = ", g_val0
print "g_val1 = ", g_val1

#seed just one random variable
rng_val = rv_u.rng.get_value(borrow = True)
print "rng_val.state = ", rng_val.get_state()
rng_val.seed(89234)  #seeds the generator
rv_u.rng.set_value(rng_val, borrow = True)
print "rng_val = ", rv_u.rng.get_value(borrow = True)
#seed all of the random variables
srng.seed(902340)

#Sharing Streams Between Functions
state_after_v0 = rv_u.rng.get_value().get_state()
nearly_zeros()
v1 = f()
v2 = f()
rng = rv_u.rng.get_value(borrow = True)
rng.set_state(state_after_v0)
# v2 = f()
v3 = f()
print 'v1 = ', v1
print 'v2 = ', v2
print 'v3 = ', v3
v3 = f()
print 'v3 = ', v3



