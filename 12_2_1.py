import numpy as np
import numpy.matrixlib
import math

def nsi(A, k):
    n=A.shape[0]
    Q=np.matrix(np.eye(n))
    for it in range(0,k):
        Q=QR(A@Q)[0]
    lam=np.diag(Q.transpose()@A@Q)
    return lam

def unshiftedqr(A, k):
    n=A.shape[0]
    Q=np.matrix(np.eye(n))
    Qbar=Q
    R=A
    for it in range(0,k):
        qrTuple = QR(R@Q)
        Q=qrTuple[0]
        R=qrTuple[1]
        Qbar=Qbar@Q
    lam=np.diag(R@Q)
    return lam # QBar 特征向量矩阵

def shiftedqr0(A):
    tol = 10**(-14)
    m=A.shape[0]
    lam = np.zeros(m)
    n=m-1
    while n>0:
        while np.max(np.abs(A[n, 0:n]))>tol:
            mu = A[n,n]
            qrTuple = QR(A-mu*np.matrix(np.eye(n+1)))
            Q=qrTuple[0]
            R=qrTuple[1]
            A=R@Q+mu*np.matrix(np.eye(n+1))
        lam[n]=A[n,n]
        A=A[0:n, 0:n]
        n-=1
    lam[0]=A[0,0]
    return lam

def shiftedqr(A):
    tol = 10**(-14)
    kountcol=500
    m=A.shape[0]
    lam = np.zeros(m)
    n=m-1
    while n>0 :
        kount=0
        while np.max(np.abs(A[n, 0:n]))>tol and kount<kountcol:
            kount+=1
            mu = A[n,n]
            qrTuple = QR(A-mu*np.matrix(np.eye(n+1)))
            Q=qrTuple[0]
            R=qrTuple[1]
            A=R@Q+mu*np.matrix(np.eye(n+1))
        if kount<kountcol:
            lam[n]=A[n,n]
            A=A[0:n, 0:n]
            n-=1
        else:
            disc=((A[n-1,n-1]-A[n,n])**2)+4*A[n,n-1]*A[n-1,n]
            if disc<0:
                disc=0
            lam[n]=(A[n-1,n-1]+A[n,n]+math.sqrt(disc))/2
            lam[n-1]=(A[n-1,n-1]+A[n,n]-math.sqrt(disc))/2
            n=n-2
            if n!= -1:
                A=A[0:n+1, 0:n+1]
    if n>-1:
        lam[0]=A[0,0]
    return lam

def hessen(A):
    m=A.shape[0]
    v = np.matrix(np.zeros((m,m)))
    for k in range(0, m-1):
        x=A[k+1:m, k]
        temp= -np.sign(x[0]+(10**(-6)))[0,0]*np.linalg.norm(x)*np.matrix(np.eye(m-k-1, 1))-x
        v[0:m-k-1, k]=temp
        v[0:m-k-1, k]=v[0:m-k-1, k]/np.linalg.norm(v[0:m-k-1, k])
        A[k+1:m, k:m]=A[k+1:m,k:m]-2*v[0:m-k-1, k]@v[0:m-k-1, k].transpose()@A[k+1:m, k:m]
        A[0:m,k+1:m]=A[0:m,k+1:m]-2*A[:,k+1:m]@v[0:m-k-1, k]@v[0:m-k-1, k].transpose()
    return (A,v)

def QR(A):
    n=A.shape[0]
    m=A.shape[1]
    Q=np.matrix(np.zeros((n,n)))
    R=np.matrix(np.zeros((n,m)))
    for i in range(0,n):
        Al=np.matrix(np.zeros((n,1)))
        if i<m:
            Al=A[:,i]
        else:
            Al=np.matrix(np.random.random((n, 1)))
        y=Al
        for k in range(0,i):
            q=Q[:,k]
            r=(q.transpose()@Al)[0,0]
            if i<m:
                R[k,i]=r
            y-=q*r
        r=np.linalg.norm(y)
        if i<m:
            R[i,i]=r
        Q[:,i]=y/r
    return (Q,R)

mode='12.2'
def getA():
    if mode=='12.1':
        return np.matrix([[1, 3], [2, 2]])
    if mode=='12.2':
        return np.matrix([[2,1,0],[3,5,-5],[4,0,0]])
    if mode=='1a':
        return np.matrix([[-3,3,5],[1,-5,-5],[6,6,4]])
    if mode == '1b':
        return np.matrix([[3,1,2],[1,3,-2],[2,2,6]])
    if mode == '1c':
        return np.matrix([[17,1,2],[1,17,-2],[2,2,20]])
    if mode == '1d':
        return np.matrix([[-7,-8,1],[17,18,-1],[-8,-8,2]])
    if mode=='3a':
        return np.matrix([[-1,1,3],[3,3,-2],[-5,2,7]])
    if mode=='3b':
        return np.matrix([[7,-33,-15],[2,26,7],[-4,-50,-13]])
    if mode=='3c':
        return np.matrix([[8,0,5],[-5,3,-5],[10,0,13]])
    if mode=='3d':
        return np.matrix([[-3,-1,1],[5,3,-1],[-2,-2,0]])
    if mode=='5a':
        return np.matrix([[4,3,1],[-5,-3,0],[3,2,1]])
    if mode=='5b':
        return np.matrix([[3,2,0],[-4,-2,1],[2,1,0]])
    if mode=='5c':
        return np.matrix([[7,2,-4],[-8,0,7],[2,-1,-2]])
    if mode=='5d':
        return np.matrix([[11,4,-2],[-10,0,5],[4,1,2]])

def f():
    A = hessen(getA())
    print('(%s)'%mode, end="") 
    # print(lam)

if __name__ == "__main__":
    f()
    # for i in ['1', '3', '5']:
    #     for alpha in range(97,101):
    #         mode = i+chr(alpha)
    #         f()