import math
from matplotlib import pyplot as plt

m = (2**31)-1
a=7**5
n=6
def NormalRandom():
    x=[(a%m)]
    u=[x[0]/m]
    for i in range(1, 2*10**n):
        x.append((a*x[i-1])%m)
        u.append(x[i]/m)
        # print("x=%d u=%.4f"%(x[i], u[i]))
    return u

def MontoCarlo1(u):
    sumY=0.0
    xdot=[]
    ydot=[]
    for i in range(0, int(len(u)/2)):
        x = u[2*i]
        y = u[2*i+1]
        if y<P1(x) and y > P2(x):
            sumY+=x*y
            xdot.append(x)
            ydot.append(y)
    print('(b): montoCarlo1: %.8f, n=%d'%(sumY*2/len(u), n))
    plt.plot(xdot,ydot,'ro')
    return

def P1(x):
    return math.sqrt(x)

def P2(x):
    return x*x

def DrawBase():
    p1=[]
    py1=[]
    t=0.0
    while t<=1.2:
        t+=0.0005
        p1.append(t)
        py1.append(P1(t))
    p2=[]
    py2=[]
    t=0.2
    while t<=1.2:
        t+=0.0005
        p2.append(t)
        py2.append(P2(t))
    plt.plot(p1,py1,'g-', p2, py2, 'b-')
    return

if __name__ == "__main__":
    plt.figure()
    DrawBase()
    u = NormalRandom()
    MontoCarlo1(u)
    plt.show()