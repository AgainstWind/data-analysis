
#python中的装饰器分为两类：函数装饰器和类装饰器。
#不带参数的decorator
def decorator1(func):
    def dec(*args):
        print('pre action')
        result = func(*args)
        print('post action')
        return result
    return dec
def decorator2(func):
    def dec(*args):
        print ('d2 pre')
        result = func(*args)
        print('d2 post')
        return result
    return dec


@decorator1
@decorator2
def test_f1(name):
    print(name)
    return None

test_f1('name1')  # out: preaction/name1/post action
test_f1('name2')  # out: preaction/name2/post action

class FOO:
    @decorator1
    def fun(self):
        print(self.name)


def wap(name):
    def decorator1(func):
        def dec(*args):
            print(name)
            print('pre action')
            result = func(*args)
            print('post action')
            return result
        return dec
    return decorator1


@wap('f2')
def test_f2(name):
    print(name)
    return None


@wap('f3')
def test_f3(name):
    print(name)
    return None

test_f2('name2')  # out: f1/pre action/name1/post action
test_f3('name3')  # out: f2/pre action/name2/post action


def f(x):
    return x * x
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))

import numpy as np
print(np.zeros((5,2)))
print(np.ones((5,1)))
print(np.vstack((np.zeros((5,1)),np.ones((5,1)))))