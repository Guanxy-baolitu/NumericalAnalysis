import numpy as np
from matplotlib import pyplot as plt

def f(x):
    A =np.array([[1, 2, 3, x], [4, 5, x, 6], [7, x, 8, 9], [x,10,11,12]])
    return(np.linalg.det(A)-1000)

def preplot():
    x=[]
    y=[]
    for i in range(2, 10):
        x.append(i)
        y.append(f(i))
    plt.figure()
    plt.plot(x,y)
    plt.show()


def solve(a, b):
    r = 0.5*(10**(-6))
    while b-a >=r:
        c = (a+b)/2
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
    return (a+b/2)

if __name__ =="__main__":
    # preplot()
    print(solve(-18,-16))
    print(solve(9,10))