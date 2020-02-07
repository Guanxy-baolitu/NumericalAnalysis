import math #DONE

mode = 2 # 0-例题 1-题1、3 2-题5

def f(x):
    if mode==0:
        return math.exp(x)
    if mode==1:
        return math.sin(x)-math.cos(x)
    if mode==2:
        return math.cos(x)
    if mode==3:
        return 1.0/x

def df(x):
    if mode==0:
        return math.exp(x)
    if mode==1:
        return math.cos(x)+math.sin(x)

def ddf(x):
    if mode==2:
        return -math.cos(x)
    if mode==3:
        return 2*(x**(-3))

def twoPoint5_4(x, h):
    return (f(x+h)-f(x))/h

def threePoint5_7(x, h):
    return (f(x+h)-f(x-h))/(2*h)

def threePoint5_8(x, h):
    return (f(x-h)-2*f(x)+f(x+h))/(h**2)

if __name__ == "__main__":
    if mode <2:
        for i in range(1,13):
            h = (10**(-i))
            Df = df(0)
            twoPntDf = twoPoint5_4(0, h)
            rest2 = math.fabs(twoPntDf-Df)
            threePntDf = threePoint5_7(0, h)
            rest3 = math.fabs(threePntDf-Df)
            print('{:.1e} {:30.18g} {:30.18g} {:30.18g} {:30.18g}'.format(h, twoPntDf, rest2, threePntDf, rest3))
    else:
        for i in range(1,13):
            h = (10**(-i))
            Ddf = ddf(0)
            threePntDdf = threePoint5_8(0, h)
            rest3 = math.fabs(threePntDdf-Ddf)
            print('{:.1e} {:30.18g} {:30.18g}'.format(h, threePntDdf, rest3))
