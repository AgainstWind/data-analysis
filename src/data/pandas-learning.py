import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

# DataFrame
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
print(df.head(3))
print(df.describe())


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()