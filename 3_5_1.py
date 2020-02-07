import math # DONE
import numpy as np
import numpy.matlib
from matplotlib import pyplot as plt

def BezierCoe(pnts):
    x1=pnts[0,0]
    y1=pnts[0,1]
    x2=pnts[1,0]
    y2=pnts[1,1]
    x3=pnts[2,0]
    y3=pnts[2,1]
    x4=pnts[3,0]
    y4=pnts[3,1]
    bx = 3*(x2-x1)
    cx = 3*(x3-x2)-bx
    dx = x4-x1-bx-cx
    by = 3*(y2-y1)
    cy = 3*(y3-y2)-by
    dy= y4-y1-by-cy
    return(bx, cx, dx, by, cy, dy)

def Bezier(pnts, coe, t):
    x1=pnts[0,0]
    y1=pnts[0,1]
    bx = coe[0]
    cx = coe[1]
    dx = coe[2]
    by = coe[3]
    cy = coe[4]
    dy = coe[5]
    xt = x1+bx*t+cx*(t**2)+dx*(t**3)
    yt = y1+by*t+cy*(t**2)+dy*(t**3)
    return (xt, yt)

if __name__ == "__main__":
    pnts = np.matlib.zeros((4,2))
    pnts[0]=[1,1]
    pnts[1]=[1,3]
    pnts[2]=[3,3]
    pnts[3]=[2,2]
    x = np.zeros(4)
    y = np.zeros(4)
    coe = BezierCoe(pnts)
    xLine=[]
    yLine=[]
    for i in range(0,4):
        x[i]=pnts[i,0]
        y[i]=pnts[i,1]
    ts = np.arange(0, 1, 0.01)
    for t in ts:
        pos = Bezier(pnts, coe, t)
        xLine.append(pos[0])
        yLine.append(pos[1])
    plt.plot(x,y,'ro', xLine, yLine, 'b-')
    plt.show()