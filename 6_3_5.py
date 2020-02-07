
import math # DONE
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

def pend():
    xline=[]
    yline=[]
    yline1=[]
    t=0.0
    y=(math.pi/2, 0)
    # y1=(math.pi/2, 0)
    while t<10:
        y=trapstep(t, y, h)
        # y1=eulerstep(t, y1, h)
        t=t+h
        xline.append(t)
        yline.append(y[0])
        # yline1.append(y1[0])
    return (xline, yline, yline1)

def eulerstep(t, y, h):
    return (y[0]+h*ydot(t,y)[0], y[1]+h*ydot(t,y)[1])

def trapstep(t, yLast, h):
    zpre=ydot(t, yLast)
    localg=(yLast[0]+h*zpre[0], yLast[1]+h*zpre[1])
    znext = ydot(t+h, localg)
    d=((zpre[0]+znext[0])/2, (zpre[1]+znext[1])/2)
    return (h*d[0]+yLast[0], h*d[1]+yLast[1])

def ydot(t, y):
    return (y[1], -(g/1.00)*math.sin(y[0])-d*y[1] + A*math.sin(t))

g=9.81
h=0.005
d=1.0
A=12

mode = "ani" # plot

def update_points(num):
    xLine = [0]
    yLine = [0]
    xLine.append(xAniLine[num])
    yLine.append(yAniLine[num])
    point_ani.set_data(xLine, yLine)
    return point_ani,

if __name__ == "__main__":
    lines = pend()
    fig = plt.figure()
    if mode == 'plot':
        plt.plot(np.array(lines[0]), np.array(lines[1]),'r-')
    if mode == "ani":
        xAniLine=np.sin(np.array(lines[1]))
        yAniLine=-np.cos(np.array(lines[1]))
        point_ani, =plt.plot(np.array([-1,1]), np.array([-1,1]),'ro')
        ani=animation.FuncAnimation(fig, update_points, np.arange(0, len(xAniLine)), interval=h*1000)
    # plt.plot(np.array(lines[0]), np.array(lines[1]),'r-',np.array(lines[0]), np.array(lines[2]),'b-')
    plt.grid(ls="--")
    plt.show()