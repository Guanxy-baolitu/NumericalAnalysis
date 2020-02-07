import math #DONE
from matplotlib import pyplot as plt

def euler():
    t = 0.0
    y1 = 1
    if mode == 'd':
        y1 = 5
    y2 = 0
    while t<=1:
        print('(%s): t=%.2f y1=%.30f y2=%.30f'%(mode, t, y1, y2))
        t+=h
        y1=eulerstep(t, y1, y2, h)[0]
        y2=eulerstep(t, y1, y2, h)[1]
    return

def eulerstep(t, y1, y2, h):
    return (y1+h*ydot(t,y1, y2, h)[0], y2+h*ydot(t,y1, y2, h)[1])

mode = '6.1'
h=0.1

def ydot(t,y1, y2, h):
    if mode == '6.1':
        return (0, 0)
    if mode == 'a':
        return (y1+y2, -y1+y2)
    if mode == 'b':
        return (-y1-y2, y1-y2)
    if mode == 'c':
        return (-y2, y1)
    if mode == 'd':
        return (y1+3*y2, 2*y1+2*y2)

if __name__ == "__main__":
    euler()
    for h in [0.1, 0.01]:
        for i in range(97,101):
            mode = chr(i)
            euler()