import numpy as np
from matplotlib import pyplot as plt
import math

def preplot():
    x_a = np.arange(-2,3)
    x_b = np.arange(-2,2.5)
    x_c = np.arange(-2,2)
    y_a = y(x_a, 'a')
    y_b = np.exp(x_b-2)+(x_b**3)-x_b
    y_c = 1+5*x_c-6*(x_c**3)-np.exp(2*x_c)
    plt.figure()
    plt.subplot(3,1,1)
    plt.plot(x_a,y_a)
    plt.subplot(3,1,2)
    plt.plot(x_b,y_b)
    plt.subplot(3,1,3)
    plt.plot(x_c,y_c)
    plt.show()


def y(x, idx):
    if idx=='a':
        return 2*(x**3)-6*x-1
    if idx=='b':
        return (math.exp(x-2))+(x**3)-x
    if idx=='c':
        return 1+5*x-6*(x**3)-math.exp(2*x)

def calculation(a, b, idx):
    r = 0.5*(10**-6)
    xlist = [a, b]
    ylist = [y(a, idx), y(b, idx)]
    while (b-a>=r):
        c = (a+b)/2
        fc = y(c, idx)
        xlist.append(c)
        ylist.append(fc)
        if fc==0:
            break
        fa = y(a, idx)
        if fa*fc<0:
            b = c
        else:
            a = c
    return ((a+b)/2, xlist, ylist)

if __name__ == '__main__':
    preplot()
    # omitted
    
