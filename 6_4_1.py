import math # DOUBT

def f():
    t = 0.0
    ymid = 1
    yRK = 1
    while t<=1:
        print('(%s): t=%.2f midpoint:%.20f RK:%.20f'%(mode, t, ymid, yRK))
        t+=h
        ymid=midpointstep(t, ymid, h)
        yRK=RKstep(t, yRK, h)
    return

def midpointstep(t, y, h):
    return y+h*ydot(t+h/2, y+ydot(t, y)*h/2)

def RKstep(t, y, h):
    s1 = ydot(t, y)
    s2 = ydot(t+h/2, y+s1*h/2)
    s3 = ydot(t+h/2, y+s2*h/2)
    s4 = ydot(t+h, y+h*s3)
    return y+(s1+2*s2+2*s3+s4)*h/6

mode = '6.18'
h=0.1

def ydot(t,y):
    if mode == '6.18':
        return t*y+(t**3)
    if mode == 'a':
        return t
    if mode == 'b':
        return t*t*y
    if mode == 'c':
        return 2*(t+1)*y
    if mode == 'd':
        return 5*(t**4)*y
    if mode == 'e':
        return 1/(y**2)
    if mode == 'f':
        return (t**3)/(y**2)

if __name__ == "__main__":
    f()
    for h in [0.1]:#, 0.05, 0.025]:
        for i in range(97,103):
            mode = chr(i)
            f()