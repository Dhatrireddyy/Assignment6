# CBSE Probability Grade 12
# Exercise 13.2.5

# Name: Velma Dhatri Reddy
# Roll number: AI21BTECH11030

""" Problem Statement
A die marked 1,2,3 in red and 4,5,6 in green is tossed. Let A be the event,
‘the number is even’, and B be the event, ‘the number is red’. Are A and B independent?
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.pyplot import stem

X = np.array([6,5,4,3,2,1])
Y = np.array([1/6,1/6,1/6,1/6,1/6,1/6])
fig1 = stem(X, Y, linefmt='k-', markerfmt='ko', basefmt='k-')
plt.grid('minor')
plt.savefig("figs/pmf.png")
