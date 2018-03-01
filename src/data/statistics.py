import numpy as np
import matplotlib
# matplotlib.use('agg') windows下backend_interagg
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

print(matplotlib.get_backend())
x = np.array(range(1000))
y = np.random.normal(0, 0.1, 1000)
x1 = np.arange(-0.5,0.5,0.01)
density = stats.gaussian_kde(y)
# plt.hist(y,bins=20,label="hist",normed=True)
plt.plot(x1,density(x1))
plt.show()
plt.savefig('hist.png')
sns.distplot(y,rug=True,hist=True)



