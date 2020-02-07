import math # DONE
import numpy as np
import numpy.matlib

def romberg(n):
    a=bound()[0]
    b=bound()[1]
    h = np.zeros(n)
    R = np.matrix(np.zeros((n,n)))
    R[0,0] = (b-a)*(f(a)+f(b))/2
    for j in range(1, n):
        h[j]=(b-a)/(2**j)
        subtotal = 0
        for i in range(1, 2**(j-1)+1):
            subtotal+=f(a+(2*i-1)*h[j])
        R[j,0]=R[j-1,0]/2 + h[j]*subtotal
        for k in range(1,j+1):
            up = (4**k)*R[j,k-1]-R[j-1, k-1]
            down = 4**k-1
            R[j,k]=up/down
    return R[n-1, n-1]

mode = '5.11'

def bound():
    if mode == '5.11':
        return (1,2)
    if mode == 'a':
        return (0, 4)
    if mode == 'b':
        return (0, 1)
    if mode == 'c':
        return (0, 1)
    if mode == 'd':
        return (1,3)
    if mode == 'e':
        return (0,math.pi)
    if mode == 'f':
        return (2,3)
    if mode == 'g':
        return (0, 2*math.sqrt(3))
    if mode == 'h':
        return (0,1)

def f(x):
    if mode == '5.11':
        return math.log(x)
    if mode == 'a':
        return x/math.sqrt((x**2)+9)
    if mode == 'b':
        return (x**3)/(x*x+1)
    if mode == 'c':
        return x*math.exp(x)
    if mode == 'd':
        return x*x*math.log(x)
    if mode == 'e':
        return x*x*math.sin(x)
    if mode == 'f':
        return x*x*x/math.sqrt((x**4)-1)
    if mode == 'g':
        return 1/math.sqrt(x*x+4)
    if mode == 'h':
        return x/math.sqrt((x**4)+1)

if __name__ == "__main__":
    print(romberg(5))
    for i in range(97,105):
        mode = chr(i)
        print('(%c): %.30f'%(mode, romberg(5)))