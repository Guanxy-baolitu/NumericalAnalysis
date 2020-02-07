import math

TOL=0.5*(10**(-8))
aOri=0
bOri=0
sumResult=0
sumRange=0
isInit = True

def adapquad(a, b):
    global isInit
    global aOri, bOri, sumResult, sumRange
    if isInit == True:
        isInit=False
        aOri=a
        bOri=b
        sumResult=0
        sumRange=0
    c = (a+b)/2
    Sab = S(a, b)
    Sac = S(a, c)
    Scb = S(c, b)
    threshold = 3*TOL*(b-a)/(bOri-aOri)
    if fMode == 'Simpson':
        threshold *= 5
    if fMode == 'Open':
        threshold *= (10/3)
    if math.fabs(Sab-Sac-Scb)<threshold:
        sumResult+=(Sac+Scb)
        sumRange+=2
    else:
        adapquad(a, c)
        adapquad(c, b)

def S(a,b):
    if fMode == 'Echelon':
        return Echelon(a, b)
    if fMode == 'Simpson':
        return Simpson(a, b)
    if fMode == 'Open':
        return Open(a, b)


def Echelon(a, b):
    result = f(a)+f(b)
    return result*(b-a)/2

def Simpson(a, b):
    x0=a
    x2=b
    h=(b-a)/2
    x1=x0+h
    result = f(x0)+4*f(x1)+f(x2)
    return result*h/3

def Open(a, b):
    h=(b-a)/4
    x1=a+h
    x2=a+2*h
    x3=a+3*h
    return (2*f(x1)-f(x2)+2*f(x3))*4*h/3

mode = '5.12'
fMode = 'Echelon'

def bound():
    if mode=='5.12':
        return (-1, 1)
    if mode == 'a':
        return (0, 4)
    if mode == 'b':
        return (0, 1)
    if mode == 'c':
        return (0, 1)
    if mode == 'd':
        return (1,3)
    if mode == 'e':
        return (0,math.pi)
    if mode == 'f':
        return (2,3)
    if mode == 'g':
        return (0, 2*math.sqrt(3))
    if mode == 'h':
        return (0,1)

def f(x):
    if mode == '5.12':
        return 1+math.sin(math.exp(3*x))
    if mode == 'a':
        return x/math.sqrt((x**2)+9)
    if mode == 'b':
        return (x**3)/(x*x+1)
    if mode == 'c':
        return x*math.exp(x)
    if mode == 'd':
        return x*x*math.log(x)
    if mode == 'e':
        return x*x*math.sin(x)
    if mode == 'f':
        return x*x*x/math.sqrt((x**4)-1)
    if mode == 'g':
        return 1/math.sqrt(x*x+4)
    if mode == 'h':
        return x/math.sqrt((x**4)+1)

if __name__ == "__main__":
    adapquad(bound()[0], bound()[1])
    print(sumResult)
    for i in range(97,105):
        mode = chr(i)
        for fMode in ['Echelon', 'Simpson', 'Open']:
            isInit = True
            adapquad(bound()[0], bound()[1])
            print('(%s): %s: %.30f, 区间数%d'%(mode, fMode, sumResult, sumRange))