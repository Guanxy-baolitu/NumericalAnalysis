import math #DOUBT
from matplotlib import pyplot as plt
import numpy as np

def dftinterp():
    x = np.array(getx())
    n = x.shape[0]
    t=np.zeros(n)
    # y=np.fft.fft(x)
    y=[-5.5154, -1.0528+3.6195j, 1.5191-1.1667j, -0.5028-0.2695j,
    -0.7778, -0.5028+0.2695j, 1.5910+1.1667j, -1.0528-3.6195j]
    print('Pn(t)=%f'%(y[0].real/math.sqrt(n)), end='')
    co = 2/math.sqrt(n)
    for k in range(1, int(n/2)):
        print('%+fcos%dPIt%+fsin%d'%(co*y[k].real, 2*k, co*y[k].imag, 2*k), end='')
    print('%+fcos%dPIt'%(y[int(n/2)].real/math.sqrt(n), n))
    return

p=100
def dftinterpPlot():
    x = np.array(getx())
    n = x.shape[0]
    t=np.zeros(n)
    tp=np.zeros(p)
    for i in range(0, n):
        t[i]=(i/n)
    for i in range(0, p):
        tp[i]=(i/p)
    y=np.fft.fft(x)
    yp=np.zeros(p)
    yp[0:math.floor(n/2+2)]=np.real(y[0:math.floor(n/2+2)])
    yp[math.floor(p-n/2+2):p]=np.real(y[math.floor(n/2+2):n])
    xp=np.real(np.fft.ifft(yp))*(p/n)
    plt.figure()
    plt.plot(t, x, 'ro', tp, xp, 'b-')
    plt.show()
    return

mode='10.2'
def getx():
    if mode=='10.2':
        return [1,0,-1,0]
    if mode == '10.3':
        return [-2.2, -2.8, -6.1, -3.9, 0.0, 1.1, -0.6, 1.1]
    if mode =='a':
        return range(0,8)
    if mode =='b':
        return [2, -1, 0, 1, 1, 3, -1, -1]
    if mode == 'c':
        return [3, 1, 4, 2, 3, 1, 4, 2]
    if mode == 'd':
        return [1, -2, 5, 3, -2, -3, 1, 2]

if __name__ == "__main__":
    dftinterp()
    # for i in range(97,101):
    #     mode = chr(i)
    #     dftinterp()