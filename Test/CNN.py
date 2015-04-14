# __author__ = 'cjweffort'
# -*- coding: utf-8 -*-

import os
import sys
import time

import numpy
import theano
import theano.tensor as T
from theano.tensor.signal import downsample
from theano.tensor.nnet import conv

rng = numpy.random.RandomState(23455)
dataset = 'mnist.pkl.gz'
data_dir, data_file = os.path.split(dataset)
# if data_dir == "" and not os.path.isfile(dataset):
