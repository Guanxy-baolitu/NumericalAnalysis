import math
import numpy as np
from matplotlib import pyplot as plt

def halton(p, n):
    b=np.zeros(math.ceil(math.log(n)/math.log(p)))
    u=[]
    for j in range(0,n):
        i=0
        b[0]+=1
        while b[i]>(p-1+(10**(-8))):
            b[i]=0
            i+=1
            b[i]+=1
        u.append(0)
        for k in range(0, len(b)):
            u[j]+=b[k]*math.pow(p, -(k+1))
    return u

def MontoCarlo1(u):
    sumY=0.0
    for i in range(0, len(u)):
        t = u[i]
        ft1=P1(t)
        ft2=P2(t)
        sumY+=(ft2-ft1)
    print('(b): montoCarlo1: %.8f, n=%d'%(sumY/len(u), math.ceil(math.log10(len(ux)))))
    return

def MontoCarlo2(ux, uy):
    x=[]
    y=[]
    cnt=0
    for i in range(0, len(ux)):
        xi = ux[i]
        yi = uy[i]
        if P2(xi)>=yi and P1(xi)<=yi:
            x.append(xi)
            y.append(yi)
            cnt+=1
    n=math.ceil(math.log10(len(ux)))
    print('(c): montoCarlo2: %.8f, n=%d'%(cnt/len(ux), n))
    if n==4:
        plt.figure()
        plt.plot(x,y,'ro')
        plt.show()
    return

def P1(x):
    return x*x-x+0.5

def P2(x):
    return -(x*x)+x+0.5

if __name__ == "__main__":
    for k in range(2, 6):
        ux = halton(2, 10**k)
        uy = halton(3, 10**k)
        MontoCarlo1(ux)
        MontoCarlo2(ux, uy)
