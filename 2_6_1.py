import numpy as np
import numpy.matlib

def ConjugateGradient(A, b):
    n = A.shape[0]
    x = np.matlib.zeros((n,1))
    xLast = x
    dLast = b
    rLast = b
    for iter in range(0,50):
        if checkZero(rLast) == True:
            break
        a = (rLast.transpose().dot(rLast)/(dLast.transpose()@A@dLast))[0,0]
        x=xLast+dLast*a
        r = rLast-a*A*dLast
        beta = (r.transpose().dot(r)/(rLast.transpose().dot(rLast)))[0,0]
        d = r+beta*dLast
        xLast = x
        dLast = d
        rLast = r
    return x

def ConjugateGradientPreCondition(A, b):
    n = A.shape[0]
    x = np.matlib.zeros((n,1))
    M_1 = np.matlib.zeros((n,n))
    for i in range(0,n):
        M_1[i,i]=1/A[i,i]
    xLast = x
    rLast = b
    dLast = M_1.dot(rLast)
    zLast = M_1.dot(rLast)
    for iter in range(0,50):
        if checkZero(rLast) == True:
            break
        a = (rLast.transpose().dot(zLast)/(dLast.transpose()@A@dLast))[0,0]
        x=xLast+dLast*a
        r = rLast-a*A*dLast
        z = M_1.dot(r)
        beta = (r.transpose().dot(z)/(rLast.transpose().dot(zLast)))[0,0]
        d = z+beta*dLast
        xLast = x
        dLast = d
        rLast = r
        zLast = z
    return x

def Hilbert(n):
    return np.matrix(1/(np.arange(1,n+1)+np.arange(0,n)[:, np.newaxis]))

def checkZero(x):
    n=x.shape[0]
    for i in range(0,n):
        if np.abs(x[i,0]-0)>(10**(-9)):
            return False
    return True

def f_1():
    A = np.matrix([[2, 2], [2, 5]])
    b = np.matrix([[6], [3]])
    print(ConjugateGradientPreCondition(A,b))
    # [[ 4.]
    # [-1.]]
    A_1_a = np.matrix([[1, 0], [0, 2]])
    b_1_a = np.matrix([[2], [4]])
    print(ConjugateGradientPreCondition(A_1_a,b_1_a))
    # [[2.]
    # [2.]]
    A_1_b = np.matrix([[1, 2], [2, 5]])
    b_1_b = np.matrix([[1], [1]])
    print(ConjugateGradientPreCondition(A_1_b,b_1_b))
    # [[ 3.]
    # [-1.]]
    return

def f_3(n):
    A = Hilbert(n)
    b = np.matlib.ones((n,1))
    return(ConjugateGradientPreCondition(A,b))

if __name__ == "__main__":
    # f_1()
    print(f_3(4))
    print(f_3(8))