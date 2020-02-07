import numpy as np
from matplotlib import pyplot as plt
import math

def preplot():
    x = np.arange(-2,4)
    x_c = np.arange(6.2,7.7)
    y_a = y(x, 'a')
    y_b = y(x, 'b')
    y_c = (np.cos(x_c)**2)+6-x_c
    plt.figure()
    plt.subplot(3,1,1)
    plt.plot(x,y_a)
    plt.subplot(3,1,2)
    plt.plot(x,y_b)
    plt.subplot(3,1,3)
    plt.plot(x_c,y_c)
    plt.show()


def y(x, idx):
    if idx=='a':
        return x**3-9
    if idx=='b':
        return 3*(x**3)+(x**2)-x-5
    if idx=='c':
        return (math.cos(x)**2)+6-x

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
    # preplot()
    x = np.arange(-2,4)
    x_c = np.arange(6.2,7.7)
    y_a = y(x, 'a')
    y_b = y(x, 'b')
    y_c = (np.cos(x_c)**2)+6-x_c

    plt.figure()

    plt.subplot(3,1,1)
    (result, xlist1, ylist1)=calculation(-2, 4, 'a')
    print('{:30.18g}'.format(result))
    plt.plot(x,y_a, 'b-', xlist1, ylist1, 'ro')

    plt.subplot(3,1,2)
    (result, xlist2, ylist2)=calculation(-4, 4, 'b')
    print('{:30.18g}'.format(result))
    plt.plot(x,y_b, 'b-', xlist2, ylist2, 'ro')
 
    plt.subplot(3,1,3)
    (result, xlist3, ylist3)=calculation(6.2, 7.7, 'c')
    print('{:30.18g}'.format(result))
    plt.plot(x_c,y_c, 'b-', xlist3, ylist3, 'ro')
    plt.show()
    
