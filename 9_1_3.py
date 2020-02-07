import math # MONTO DOUBT
from matplotlib import pyplot as plt

m = (2**31)-1
a=7**5

n=6

def NormalRandom():
    x=[(a%m)]
    u=[x[0]/m]
    for i in range(1, 10**n):
        x.append((a*x[i-1])%m)
        u.append(x[i]/m)
        # print("x=%d u=%.4f"%(x[i], u[i]))
    return u

sipm=32
def CompoundSimpson(f):
    a=0
    b=1
    result = f(a)+f(b)
    for i in range(1,sipm+1):
        xi = (2*i-1)*(b-a)/(2*sipm) + a
        result+=4*f(xi)
    for i in range(1,sipm):
        xi = (2*i)*(b-a)/(2*sipm)+a
        result+=2*f(xi)
    return result/(6*sipm)

def P1(x):
    return x*x-x+0.5

def P2(x):
    return -(x*x)+x+0.5

def DrawP1P2():
    p1=[]
    py1=[]
    t=-0.2
    while t<=1.2:
        t+=0.0005
        p1.append(t)
        py1.append(P1(t))
    p2=[]
    py2=[]
    t=-0.2
    while t<=1.2:
        t+=0.0005
        p2.append(t)
        py2.append(P2(t))
    plt.plot(p1,py1,'g-', p2, py2, 'b-')
    print('(a): compoundSimpson: %.8f'%(CompoundSimpson(P2)-CompoundSimpson(P1)))
    return

def MontoCarlo1(u):
    x=[]
    y1=[]
    y2=[]
    sumY=0.0
    for i in range(0, len(u)):
        t = u[i]
        x.append(t)
        ft1=P1(t)
        ft2=P2(t)
        y1.append(ft1)
        y2.append(ft2)
        sumY+=(ft2-ft1)
    print('(b): montoCarlo1: %.8f, n=%d'%(sumY/len(u), n))
    # plt.plot(x,y1,'go', x, y2, 'bo')
    return

def MontoCarlo2(u):
    x=[]
    y=[]
    cnt=0
    for i in range(1, len(u)):
        t = u[i-1]
        ft = u[i]
        if P2(t)>=ft and P1(t)<=ft:
            x.append(t)
            y.append(ft)
            cnt+=1
    print('(c): montoCarlo2: %.8f, n=%d'%(cnt/len(u), n))
    plt.plot(x,y,'ro')
    return

if __name__ == "__main__":
    plt.figure()
    DrawP1P2()
    u = NormalRandom()
    MontoCarlo1(u)
    MontoCarlo2(u)
    plt.show()
