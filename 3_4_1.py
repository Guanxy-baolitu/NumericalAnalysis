import math # DONE
import numpy as np
import numpy.matlib
from matplotlib import pyplot as plt

def NaturalSpline(Pnts):
    n = Pnts.shape[0]
    a = np.zeros(n-1)
    sigma = np.zeros(n-1)
    delta = np.zeros(n-1)
    for i in range(0,n-1):
        a[i]=Pnts[i,1]
        sigma[i] = Pnts[i+1,0]-Pnts[i,0]
        delta[i] = Pnts[i+1,1]-Pnts[i,1]
    A = np.matrix(np.eye(n))
    b = np.matrix(np.zeros((n,1)))
    for i in range(1, n-1):
        A[i, i-1]=sigma[i-1]
        A[i,i] = 2*(sigma[i-1]+sigma[i])
        A[i, i+1]=sigma[i]
        b[i,0] = 3*(delta[i]/sigma[i]-(delta[i-1]/sigma[i-1]))
    c = Jacobi(A,b)
    b = np.zeros(n-1)
    d = np.zeros(n-1)
    for i in range(0,n-1):
        d[i]=(c[i+1,0]-c[i,0])/(3*sigma[i])
        b[i]=delta[i]/sigma[i]-sigma[i]*(2*c[i]+c[i+1])/3
    return(a,b,c,d)

def Jacobi(A, b):
    n=A.shape[0]
    xLast = np.matrix(np.zeros((n,1)))
    x = np.matrix(np.zeros((n,1)))
    for iter in range(0,50):
        for i in range(0,n):
            up = b[i,0]
            for j in range(0,n):
                if i!=j:
                    up-=A[i,j]*xLast[j,0]
            x[i]=up/A[i,i]
        xLast = x
        if checkFinish(x) == True:
            break
    return (x)

def checkFinish(x):
    n=x.shape[0]
    for i in range(0,n):
        if math.fabs(x[i,0]-1)>(10**(-9)):
            return False
    return True

def Si(a, b, c, d, Pnts, x, i):
    return a[i]+b[i]*(x-Pnts[i,0])+c[i,0]*((x-Pnts[i,0])**2)+d[i]*((x-Pnts[i,0])**3)

if __name__ =="__main__":
    plt.figure()
    cnt = 5
    pnts = np.matlib.zeros((cnt,2))
    # pnts[0]=[0,3] #例题
    # pnts[1]=[1,-2]
    # pnts[2]=[2,1]
    # pnts[0]=[0,3] #1.a
    # pnts[1]=[1,5]
    # pnts[2]=[2,4]
    # pnts[3]=[3,1]
    pnts[0]=[-1,3] #1.b
    pnts[1]=[0,5]
    pnts[2]=[3,1]
    pnts[3]=[4,1]
    pnts[4]=[5,1]
    coe = NaturalSpline(pnts)
    a=coe[0]
    b=coe[1]
    c=coe[2]
    d=coe[3]
    x = np.zeros(cnt)
    y = np.zeros(cnt)
    xLine=[]
    yLine=[]
    for i in range(0,cnt):
        x[i]=pnts[i,0]
        y[i]=pnts[i,1]
        if i==cnt-1:
            break
        xline = np.arange(pnts[i,0], pnts[i+1,0], 0.01)
        for j in range(0, len(xline)):
            xLine.append(xline[j])
            yLine.append(Si(a, b, c, d, pnts, xline[j], i))
    plt.plot(x,y,'ro', xLine, yLine, 'b-')
    plt.show()