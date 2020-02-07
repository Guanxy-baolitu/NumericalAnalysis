import math

def Newton(idx):
    r = 0.5*(10**(-8))
    pre = 0
    x = 2
    while math.fabs(x-pre)>=r:
        pre = x
        if idx == 'a':
            x = x-(x**3-2*x-2)/(3*x*x-2)
        if idx == 'b':
            x = x - (math.exp(x)+x-7)/(math.exp(x)+1)
        if idx == 'c':
            x = x -(math.exp(x)+math.sin(x)-4)/(math.exp(x)+math.cos(x))
    return x


if __name__ == "__main__":
    print(Newton('a'))
    print(Newton('b'))
    print(Newton('c'))