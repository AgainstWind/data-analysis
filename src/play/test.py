import os
import shutil
import glob
import sys
#import re
import math
import random
from urllib.request import urlopen
import zlib

print(os.getcwd())

print(dir(os))

#print(help(os))

shutil.copyfile('test.py','test-copy.py')
#shutil.move('',''),

print(glob.glob('*.py'))

#command line

print(sys.argv)

print(sys.stdout)

print(math.cos(math.pi/4))

print(random.choice(['apple', 'pear', 'banana']))

#f = open('baidu.txt','w+')
#http request
for line in urlopen('http://www.baidu.com'):
    line = line.decode('utf-8')
    #f.write(line)

#f.close()

s = b'whicfjsj fjsfjhsh   sfsufsfn   fsjfjsah'
ss = b'hehe hehe  hehe test hehe'
print(len(s))
print(len(ss))
t=zlib.compress(s)
tt = zlib.compress(ss)
print('after compress',len(t))
print('after compress',len(tt))

def average(values):
    """
    :param values:
    :return:
    >>> print(average([20,30,70]))
    40.0
    """
    return sum(values)/len(values)


import doctest
doctest.testmod()