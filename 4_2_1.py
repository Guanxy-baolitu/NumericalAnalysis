import numpy as np #DONE
import numpy.matlib
from matplotlib import pyplot as plt
import math

def Solve(A,b):
    ATA = A.transpose()@A
    ATb = A.transpose()@b
    c=GaussianElimination(ATA, ATb)
    print('y=%f+%fcos2PIt+%fsin2PIt' % (c[0,0],c[1,0],c[2,0]))
    return c

def PeriodicFunction(c,t):
    return c[0,0]+c[1,0]*math.cos(math.pi*2*t)+c[2,0]*math.sin(math.pi*2*t)

def GaussianElimination(A, b):
    n = A.shape[0]
    for j in range(0,n):
        for i in range(j+1, n):
            mult = A[i,j]/A[j,j]
            for k in range(j, n):
                A[i,k]=A[i,k]-mult*A[j,k]
            b[i,0]-=mult*b[j,0]
    # 回代
    x = np.matrix(np.zeros((n,1)))
    for i in range(n-1,-1, -1):
        for j in range(i+1,n):
            b[i,0]-=A[i,j]*x[j,0]
        x[i,0]=b[i,0]/A[i,i]
    return x

def AProducer(pnts):
    n=pnts.shape[0]
    A = np.matlib.ones((n,3))
    for i in range(0,n):
        A[i,1]=math.cos(math.pi*2*i/n)
        A[i,2]=math.sin(math.pi*2*i/n)
    return A
    
def bProducer(pnts):
    n=pnts.shape[0]
    b = np.matlib.zeros((n,1))
    for i in range(0,n):
        b[i,0]=pnts[i,1]
    return b

def RMSE(A,b,c):
    r = b-A@c
    result = 0
    for i in range(0,r.shape[0]):
        result+=(r[i,0]**2)
    return math.sqrt(result/(r.shape[0]))

if __name__ == "__main__":
    cnt=12
    pnts = np.matlib.zeros((cnt,2))
    # pnts[0]=[0,-2.2] # 例题
    # pnts[1]=[1,-2.8]
    # pnts[2]=[2,-6.1]
    # pnts[3]=[3,-3.9]
    # pnts[4]=[4,-0.0]
    # pnts[5]=[5,+1.1]
    # pnts[6]=[6,-0.6]
    # pnts[7]=[7,-1.1]
    pnts[0]=[1,6.224]
    pnts[1]=[2,6.665]
    pnts[2]=[3,6.241]
    pnts[3]=[4,5.302]
    pnts[4]=[5,5.073]
    pnts[5]=[6,5.127]
    pnts[6]=[7,4.994]
    pnts[7]=[8,5.012]
    pnts[8]=[9,5.108]
    pnts[9]=[10,5.377]
    pnts[10]=[11,5.510]
    pnts[11]=[12,6.372]
    x = np.zeros(cnt)
    y = np.zeros(cnt)
    A = AProducer(pnts)
    b = bProducer(pnts)
    coe = Solve(A,b)
    print('RMSE:%f'% RMSE(A,b,coe))
    xLine=[]
    yLine=[]
    for i in range(0,cnt):
        x[i]=pnts[i,0]
        y[i]=pnts[i,1]
    ts = np.arange(0, cnt, 0.01)
    for t in ts:
        xLine.append(t)
        yLine.append(PeriodicFunction(coe, t/cnt))
    plt.plot(x,y,'ro', xLine, yLine, 'b-')
    plt.show()