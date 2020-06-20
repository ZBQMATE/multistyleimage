import numpy as np
import scipy.io
import tensorflow.compat.v1 as tf
from functools import reduce
import scipy.misc
import math


aa = np.load("layer1" + ".npy")
bb = np.load("layer2" + ".npy")

np.save("meanarr.npy", (aa+bb)/2)

