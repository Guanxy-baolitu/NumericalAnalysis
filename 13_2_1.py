import math
import numpy as np
from numpy.polynomial import polynomial as pln

def GetJacobi(cox):
    
    return

def GetHessian(cox, coy):
    return

mode=""
def GetCo():
    if mode=="13.4":
        return([0,0,0,0,4],
        [-1,0,0,-1,0],
        [0,4,0,0,0,],
        [0,0,0,0,0,],
        [5,0,0,0,0,])

def f(x, y):
    c=GetCo()
    if mode == '13.4':
        return pln.polyval2d(x, y, c)

if __name__ == "__main__":
    x = np.arange(0,1,0.0001)
    y = np.arange(0,3,0.0001)
    f(x, y)