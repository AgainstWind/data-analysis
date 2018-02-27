import numpy as np
from scipy import stats
import matplotlib as mp
import pandas as pd

print("hello world!")
print(np.random.binomial(100,0.5,20))
print(stats.binom.pmf(20,100,0.4))
dd = stats.binom.pmf(np.arange(0,21,1),100,0.4)
print(dd.sum())

print("---------------")
norm = np.random.normal(size=5)
print(norm)
print(5*norm)

print("---------------")
print(1.01**20)
