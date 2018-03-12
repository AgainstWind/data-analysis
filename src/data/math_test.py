import numpy as np
from scipy.linalg import solve
from scipy.optimize import linprog

a = np.array([[3,1,-2],[1,-1,4],[2,0,3]])
b = np.array([5,-2,2.5])
x = solve(a,b)
print("------------------------start-------------------------")
print(x)
print(np.ndim(a)) # rank of a
print("------------------------end---------------------------")
"""
线性规划demo
min: z = x1 +2x2 + 3x3
s.t.:
    -2x1 + x2 +x3 <= 9
    -3x1 + x2 + 2x3 >= 4
    3x1 - 2x2 -3x3 = -6
    x1<=0
    x2>=0
    x3取值无约束
"""
c = np.array([1,2,3])
a_ub = np.array([[-2,1,1],[3,-1,-2]])
b_ub = np.array([9,-4])
a_eq = np.array([[3,-2,-3]])
b_eq = np.array([-6])
r = linprog(c,a_ub,b_ub,a_eq,b_eq,bounds=((None,0),(0,None),(None,None)))
print(r)
print("------------------------end---------------------------")

"""
线性规划demo2
min: z = -4x1-x2
s.t.:
    -x1 + 2x2 <= 4
    2x1 + 3x2 <= 12
    x1 - x2 <= 3
    x1>=0
    x2>=0
"""
c2 = np.array([-4,-1])
a_up2 = np.array([[-1,2],[2,3],[1,-1]])
b_ub2 = np.array([4,12,3])
r2 = linprog(c2,a_up2,b_ub2,bounds=((0,None),(0,None)))
print(r2)
print("------------------------end---------------------------")