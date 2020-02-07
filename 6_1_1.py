import math #DONE

def euler():
    t = 0.0
    y = 1
    while t<=1:
        print('(%s): t=%.2f w=%.30f'%(mode, t, y))
        t+=h
        y=eulerstep(t, y, h)
    return

def eulerstep(t, y, h):
    return y+h*ydot(t,y)

mode = '6.1'
h=0.1

def ydot(t,y):
    if mode == '6.1':
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
    euler()
    for h in [0.1, 0.05, 0.025]:
        for i in range(97,103):
            mode = chr(i)
            euler()