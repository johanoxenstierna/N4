import random

import numpy as np

A = [[1, 2, 3], [4, 5, 6], [78]]


aa = np.random.normal(loc=[50, 3], scale=[1, 2], size=[5, 2])
flat_list = [y for x in A for y in x]  # NESTED FLATTING
adsf = 5