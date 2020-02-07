import numpy as np

def Cholesky(A):
    n = A.shape[0]
    R = np.matrix(np.zeros((n,n)))
    for k in range(0,n):
        if A[k,k]<=0:
            break
        R[k,k]=np.sqrt(A[k,k])
        U = np.matrix(np.zeros((1,n-k)))
        for i in range(k+1, n):
            U[0,i-k] = A[k,i]/R[k,k]
            R[k,i] = U[0,i-k]
        U2 = U.transpose().dot(U)
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i,j]-=U2[i-k, j-k]
    return R

if __name__ == "__main__":
    A=np.matrix([[4, -2, 2], [-2, 2, -4], [2, -4, 11]])
    a=np.matrix([[1, 2], [2, 8]])
    b=np.matrix([[4, -2], [-2, 1.25]])
    c=np.matrix([[25, 5], [5, 26]])
    d=np.matrix([[1, -2], [-2, 5]])
    print(Cholesky(A))
    print(Cholesky(a))
    print(Cholesky(b))
    print(Cholesky(c))
    print(Cholesky(d))