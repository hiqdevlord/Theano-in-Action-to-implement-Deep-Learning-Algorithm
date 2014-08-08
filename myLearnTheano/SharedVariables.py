# coding: utf-8
#__author__ = cmathx

from theano import shared
from theano import function
import theano.tensor as T

#shared variable
state = shared(0)
inc = T.iscalar('inc')
#updates(key,value) key:original value  value:new value
accumulator = function([inc], state, updates = [(state, state + inc)])
print state.get_value()
print accumulator(1)
print state.get_value()
print accumulator(300)
print state.get_value()

#set the shared variable
state.set_value(-1)
accumulator(3)
print state.get_value()

decrementor = function([inc], state, updates = [(state, state - inc)])

#usage of given symol
fn_of_state = state * 2 + inc
foo = T.scalar(dtype = state.dtype)
skip_shared = function([inc, foo], fn_of_state, givens = [(state, foo)])
print skip_shared(1, 3)
print state.get_value()

