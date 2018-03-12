import numpy as np
from scipy.linalg import solve
from scipy.optimize import linprog

a = np.array([[3,1,-2],[1,-1,4],[2,0,3]])
b = np.array([5,-2,2.5])

x = solve(a,b)

print(x)

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