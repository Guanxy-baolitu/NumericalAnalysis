import math # DONE
import numpy as np
import numpy.matlib
from matplotlib import pyplot as plt

def newtdd(pnt):
    n=pnt.shape[0]
    v = np.matlib.zeros((n,n))
    for j in range(0,n):
        v[j,0]=pnt[j, 1]
    for i in range(1,n):
        for j in range(0, n-i):
            v[j,i]=(v[j+1,i-1]-v[j,i-1])/(pnt[j+i,0]-pnt[j,0])
    c = np.matlib.zeros((n,1))
    for i in range(0,n):
        c[i,0]=v[0,i]
    return c

def nest(pnt, c, x):
    n=pnt.shape[0]
    result=c[n-1,0]
    for i in range(n-2,-1,-1):
        result = c[i,0]+result*(x-pnt[i,0])
    return result


def sin1(x):
    pnt = np.matlib.zeros((4,2))
    for i in range(0,4):
        pnt[i,0]=(math.pi/2)+(math.pi/2)*math.cos((2*(i+1)-1)*math.pi/(2*4))
        pnt[i,1]=math.sin(pnt[i,0])
    c=newtdd(pnt)
    s=1
    x1=x%(2*math.pi)
    if x1 >math.pi:
        x1=2*math.pi-x1
        s=-1
    if x1>math.pi/2:
        x1=math.pi-x1
    return s* nest(pnt, c, x1)


if __name__ == "__main__":
    plt.figure()
    x = np.arange(-2,2, 0.01)
    y = np.arange(-2,2, 0.01)
    y1 = np.arange(-2,2, 0.01)
    for i in range(0,len(x)):
        y[i]=math.sin(x[i])
        y1[i]=sin1(x[i])
    plt.plot(x,y, 'b-', x, y1, 'r-')
    plt.show()
