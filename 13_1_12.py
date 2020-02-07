import math
import numpy as np
import numpy.matrixlib
from matplotlib import pyplot as plt

kcnt=20
def gss():
    a=getbound()[0]
    b=getbound()[1]
    g=(math.sqrt(5)-1)/2
    x1=a+(1-g)*(b-a)
    x2=a+g*(b-a)
    f1=f(x1)
    f2=f(x2)
    for it in range(0,kcnt):
        if f1<f2:
            b=x2
            x2=x1
            x1=a+(1-g)*(b-a)
            f2=f1
            f1=f(x1)
        else:
            a=x1
            x1=x2
            x2=a+g*(b-a)
            f1=f2
            f2=f(x2)
    return (a+b)/2

def spi():
    r=getbound()[0]
    t=getbound()[1]
    s=r+(math.sqrt(5)-1)/2*(t-r)
    for it in range(0, kcnt):
        fs=f(s)
        fr=f(r)
        ft=f(t)
        down = (s-r)*(ft-fs)-(fs-fr)*(t-s)
        if down == 0:
            break
        x=(r+s-(fs-fr)*(t-r)*(t-s)/down)/2
        t=s
        s=r
        r=x
    return (r+t)/2    

# def neldermead():
#     xbar=np.matrix(np.array([0,0])).transpose()
#     n=len(xbar)
    
#     for j in range(1, n+1):
#         y[j]=f()
    
def getbound():
    if mode =='a':
        return(0,1)
    if mode =='b':
        return(-2.5,-1.5)
    if mode =='c':
        return(0,1)
    if mode =='d':
        return(1,2)
    if mode =='3b':
        return(0.25,1)

mode=''
def f(x):
    if mode == 'a':
        return 2*(x**4)+3*(x**2)-4*x+5
    if mode == 'b':
        return 3*(x**4)+4*(x**3)-12*(x**2)+5
    if mode == 'c':
        return (x**6)+3*(x**4)-2*(x**3)+(x**2)-x-7
    if mode == 'd':
        return (x**6)+3*(x**4)-12*(x**3)+(x**2)-x-7
    if mode == '3b':
        return math.pow(x-2, 2)+math.pow(1/x-3, 2)

def DrawPlot():
    plt.figure()
    x = np.arange(getbound()[0],getbound()[1],0.001)
    y=[]
    xf = np.arange(0.25,3,0.001)
    yf=1/xf
    for i in range(0,len(x)):
        y.append(f(x[i]))
    plt.plot(x, y, 'b-', xf, yf, 'g-')
    plt.show()
    return

if __name__ == "__main__":
    for i in range(97,101):
        mode = chr(i)
        print('(%s):%f'%(mode, spi()))
    # mode='3b'
    # print('(%s):%f'%(mode, gss()))
    # mode='5'
