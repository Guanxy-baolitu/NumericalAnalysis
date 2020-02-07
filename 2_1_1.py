import numpy as np

def Hilbert(n):
    return np.matrix(1/(np.arange(1,n+1)+np.arange(0,n)[:, np.newaxis]))
# 1/
# [[1 2 3 4]
#  [2 3 4 5]
#  [3 4 5 6]
#  [4 5 6 7]
#  [5 6 7 8]]

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

def f(n):
    return GaussianElimination(Hilbert(n), np.matrix(np.ones((n,1))))

if __name__ == "__main__":
    print(f(2))
    print(f(5))
    print(f(10))