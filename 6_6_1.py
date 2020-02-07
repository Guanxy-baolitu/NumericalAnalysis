import math

def f():
    t = 0.0
    y = 1
    while t<=1:
        print('(%s): t=%.2f w:%.20f'%(mode, t, y))
        t+=h
        y=step(t, y, h)
    return

ynew = y+h*(ynew**2-(ynew**3))
y =

def step(t, y, h):
    return y+h*ydot(t,y)

def Newton():
    r = 0.5*(10**(-8))
    pre = 0
    x = 1
    while math.fabs(x-pre)>=r:
        pre = x
        if idx == 'a':
            x = x-(x**3-2*x-2)/(3*x*x-2)
        if idx == 'b':
            x = x - (math.exp(x)+x-7)/(math.exp(x)+1)
    return x

mode = ''
h=0.1

if __name__ == "__main__":
    for mode in ['a', 'b']:
        Newton()