import numpy as np
import numpy.matrixlib

kn=50
def powerit():
    A=getA()
    n = A.shape[0]
    x = np.matrix(np.ones(n)).transpose()
    lam=0.0
    for it in range(0, kn):
        u = x/np.linalg.norm(x)
        x=A@u
        lam=u.transpose()@x
    print('(%s): 特征值%.2f, 特征向量'%(mode, lam), end="")
    print(x/np.linalg.norm(x))
    return 

def invpowerit(s):
    A=getA()
    n = A.shape[0]
    As = A-s*np.matrix(np.eye(n))
    x = np.matrix(np.ones(n)).transpose()
    lam=0.0
    for it in range(0, kn):
        u = x/np.linalg.norm(x)
        x=GaussianElimination(As, u)
        lam=u.transpose()@x
    print('(%s): 特征值%.2f, 特征向量'%(mode, 1/lam+s), end="")
    print(x/np.linalg.norm(x))
    return

def rqi():
    A=getA()
    n = A.shape[0]
    x = np.matrix(np.ones(n)).transpose()
    lam=0.0
    for it in range(0, kn):
        u = x/np.linalg.norm(x)
        lam=u.transpose()@A@u
        x=GaussianElimination(A-lam[0,0]*np.matrix(np.eye(n)), u)
    print('(%s): 特征值%.2f, 特征向量'%(mode, u.transpose()@A@u), end="")
    print(x/np.linalg.norm(x))
    return

def GaussianElimination(A, b):
    n = A.shape[0]
    for j in range(0,n):
        for i in range(j+1, n):
            mult = A[i,j]/A[j,j]
            for k in range(j, n):
                A[i,k]=A[i,k]-mult*A[j,k]
            b[i,0]-=mult*b[j,0]
    # 回代
    x = np.matrix(np.zeros((n,1)))
    for i in range(n-1,-1, -1):
        for j in range(i+1,n):
            b[i,0]-=A[i,j]*x[j,0]
        x[i,0]=b[i,0]/A[i,i]
    return x

mode='12.1'
def getA():
    if mode=='12.1':
        return np.matrix([[1, 3], [2, 2]])
    if mode=='a':
        return np.matrix([[10,-12,-6],[5,-5,-4],[-1,0,3]])
    if mode == 'b':
        return np.matrix([[-14,20,10],[-19,27,12],[23,-32,-13]])
    if mode == 'c':
        return np.matrix([[8,-8,-4],[12,-15,-7],[-18,26,12]])
    if mode == 'd':
        return np.matrix([[12,-4,-2],[19,-19,-10],[-35,52,27]])

if __name__ == "__main__":
    powerit()
    for i in range(97,101):
        mode = chr(i)
        powerit()