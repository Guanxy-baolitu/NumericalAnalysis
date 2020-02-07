import math

def DifferenceQuotient(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x):
    f12 = (y2-y1)/(x2-x1)
    f23 = (y3-y2)/(x3-x2)
    f34 = (y4-y3)/(x4-x3)
    f45 = (y5-y4)/(x5-x4)
    f13 = (f23-f12)/(x3-x1)
    f24 = (f34-f23)/(x4-x2)
    f35 = (f45-f34)/(x5-x3)
    f14 = (f24-f13)/(x4-x1)
    f25 = (f35-f24)/(x5-x2)
    f15 = (f25-f14)/(x5-x1)
    P = y1+f12*(x-x1)+f13*(x-x1)*(x-x2)+f14*(x-x1)*(x-x2)*(x-x3)+f15*(x-x1)*(x-x2)*(x-x3)*(x-x4)
    print('P4(x)=%f+(x-%f)(%f+(x-%f)(%f+(x-%f)(%f+(x-%f)(%f))))' % (y1, x1, f12, x2, f13, x3, f14, x4, f15))
    return P

def Difference(x1, x2, x3, x4, x5, x):#wrong!!!!
    d = (x-x1)*(x-x2)*(x-x3)*(x-x4)*(x-x5)/(5*4*3*2)
    d = d*(120*x+160*(x**3)+32*(x**5))*math.exp(1.0**2)
    return math.fabs(d)

if __name__ == "__main__":
    DQ82 = DifferenceQuotient(0.6, 1.433329, 0.7, 1.632316, 0.8, 1.896481, 0.9, 2.247908, 1.0, 2.718282, 0.82)
    DQ98 = DifferenceQuotient(0.6, 1.433329, 0.7, 1.632316, 0.8, 1.896481, 0.9, 2.247908, 1.0, 2.718282, 0.98)
    print(DQ82)
    print(DQ98)
    print(Difference(0.6,0.7,0.8,0.9,1.0, 0.82))
    print(math.fabs(math.exp(0.82**2)-DQ82))
    print(Difference(0.6,0.7,0.8,0.9,1.0, 0.98))
    print(math.fabs(math.exp(0.98**2)-DQ98))
