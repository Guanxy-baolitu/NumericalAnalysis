import numpy as np
import math

def Gaussian(A, b):
    n=A.shape[0]
    x = np.matrix(np.zeros((n,1)))
    for iter in range(0,50):
        for i in range(0,n):
            up = b[i,0]
            for j in range(0,n):
                if i!=j:
                    up-=A[i,j]*x[j,0]
            x[i]=up/A[i,i]
        if checkFinish(x) == True:
            print('Gaussian Step: %d' % iter)
            break
    return (x)

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
            print('Jacobi Step: %d' % iter)
            break
    return (x)

def checkFinish(x):
    n=x.shape[0]
    for i in range(0,n):
        if math.fabs(x[i,0]-1)>(10**(-9)):
            return False
    return True

def f(n):
    A = np.matrix(np.zeros((n,n)))
    for i in range(0,n):
        A[i,i]=3
        if i!=n-1:
            A[i,i+1]=-1
            A[i+1,i]=-1
    b = np.matrix(np.ones((n,1)))
    b[0,0]=2
    b[n-1,0]=2
    return Jacobi(A,b)

if __name__ =="__main__":
    print(f(100))
    print(f(100000))