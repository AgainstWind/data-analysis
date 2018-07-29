import sklearn
import numpy as np
import matplotlib.pyplot as plt

# plt.figure(1)
# plt.subplot(211)
# centers = [(-2,-2),(-2,1.5),(1.5,-2),(2,1.5)]
# data, features = sklearn.datasets.make_blobs(n_samples=200,centers=centers,n_features=2,
#                                              cluster_std=0.8,shuffle=False,random_state=42)
# print(data)
# print(features)

a = [1,2,3]
print('test-%s,%s,%s'%(a[0],a[1],a[2]))

b= ['symbol','code','name','trade','pricechange','changepercent','buy','sell','settlement','open','high',
               'low','volume','amount','ticktime','per','pb','mktcap','nmc','turnoverratio' ]
dictt = 'item_dict'
result = ''
for i in b:
    result = result+'str('+ dictt+'.get(\''+i+'\')),'

print(result)