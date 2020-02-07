import numpy as np #DONE
import numpy.matlib
import math

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

def LeastSquare(A,b):
    QRtuple=QR(A)
    Q=QRtuple[0]
    R=QRtuple[1]
    n=R.shape[0]
    m=R.shape[1]
    rows=[]
    rests=[]
    for i in range(0,m):
        rows.append(i)
        rests.append(0)
    QTb=(Q.transpose()@b)
    for i in range(m, n):
        rests.append(QTb[i,0])
    x=GaussianElimination(R[rows],QTb[rows])
    return (x, np.linalg.norm(rests))

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

if __name__ =="__main__":
    # A=np.matrix(np.array([[1, -4],[2, 3],[2, 2]],dtype=float)) # 例题
    # b=np.matrix(np.array([-3,15,9],dtype=float)).transpose()
    # A=np.matrix(np.array([[1,1],[2,1],[1,2],[0,3]],dtype=float)) # a
    # b=np.matrix(np.array([3,5,5,5],dtype=float)).transpose()
    A=np.matrix(np.array([[1,2,2],[2,-1,2],[3,1,1],[1,1,-1]],dtype=float))
    b=np.matrix(np.array([10,5,10,3],dtype=float)).transpose()
    print(LeastSquare(A,b)[0])
    print('e2=%f'%LeastSquare(A,b)[1])