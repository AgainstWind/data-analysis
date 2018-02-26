import numpy as np
from scipy import stats

print("hello world!")
print(np.random.binomial(100,0.5,20))
print(stats.binom.pmf(20,100,0.4))
dd = stats.binom.pmf(np.arange(0,21,1),100,0.4)
print(dd.sum())