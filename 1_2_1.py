import math
import numpy as np
from matplotlib import pyplot as plt

def preplot():
    plt.figure()
    x = np.arange(0,5)
    y = 0.5 * (x**3)-1
    plt.plot(x,x, 'b-', x, y, 'b-')
    plt.show()

def f(idx):
    r = 0.5*(10**(-8))
    pre = -1
    x = 1.5
    stepcnt = 0
    while math.fabs(x-pre)>=r and stepcnt<=1000000000:
        pre = x
        if idx== 'a':
            x = ((2*x+2)**(1/3))
        if idx =='b':
            x = math.log(7-x)
        if idx == 'c':
            x = math.log(4-math.sin(x))
        stepcnt+=1
    return x
if __name__ == "__main__":
    # preplot()
    print(f('a'))
    print(f('b'))
    print(f('c'))