import math

def exmultistep():
    t = 0.0
    y = 1
    tLast = t
    yLast = y
    while t<=1:
        print('(%s): t=%.2f w:%.20f'%(mode, t, y))
        t+=h
        ynew=AdamBashforthStep(t, y, h, tLast, yLast)
        tLast = t
        yLast = y
        y=ynew
    return

def AdamBashforthStep(t, y, h, tLast, yLast):
    z1 = ydot(t,y)
    zpre = ydot(tLast, yLast)
    return y+h*(1.5*z1-0.5*zpre)

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
    exmultistep()
    for i in range(97,103):
            mode = chr(i)
            exmultistep()