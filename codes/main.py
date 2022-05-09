import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.pyplot import stem

X = np.array([6,5,4,3,2,1])
Y = np.array([1/6,1/6,1/6,1/6,1/6,1/6])
fig1 = stem(X, Y, linefmt='k-', markerfmt='ko', basefmt='k-')
plt.grid('minor')
plt.savefig("figs/pmf.png")
