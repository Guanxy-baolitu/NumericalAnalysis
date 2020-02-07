import numpy.matlib # DONE
import numpy as np
import math

def Solve(A, b):
    ATA = A.transpose()@A
    ATb = A.transpose()@b
    x=GaussianElimination(ATA, ATb)
    return x

def res2(A, b, x):
    r = b-A@x
    result=0
    for i in range(0,r.shape[0]):
        result+=(r[i,0]*r[i,0])
    return math.sqrt(result)

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

if __name__ == "__main__":
    # A=np.matrix(np.array([[1.0, 1.0], [1.0,-1.0], [1.0, 1.0]])) #例题
    # b=np.matrix(np.array([2.0,1.0,3.0])).transpose()
    # A=np.matrix(np.array([[3.0,-1.0, 2.0], [4.0, 1.0, 0], [-3.0, 2.0, 1.0], [1.0, 1.0, 5.0], [-2.0, 0, 3.0]])) #a
    # b=np.matrix(np.array([10.0,10.0,-5.0,15.0,0])).transpose()
    A=np.matrix(np.array([[4,2,3,0],[-2,3,-1,1],[1,3,-4,2],[1,0,1,-1],[3,1,3,-2]],dtype=float)) #b
    b=np.matrix(np.array([10,0,2,0,5],dtype=float)).transpose()
    x = Solve(A,b)
    print(x)
    print(res2(A, b, x))