import random

import numpy as np

# aa = np.random.dirichlet((0.7, 0.8, 1, 0.6, 0.2), 10)
aa = np.random.normal(loc=5, scale=3, size=100)

aa.sort()
gh = random.choices([1, 2, 3, 4], weights=[0.1, 0.2, 0.3, 0.4], k=2)
bb = np.random.random_integers(5, 20, size=10)
# hh = np.random.choice(aa, p)

adsf = 5