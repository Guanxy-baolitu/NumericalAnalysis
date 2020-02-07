import math

mode = '5.10'

def bound():
    if mode == '5.8':
        return (1,2)
    if mode == '5.10':
        return (0,1)
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
    if mode == '7a':
        return (0, math.pi/2)
    if mode == '7b':
        return (0, math.pi/2)
    if mode == '7c':
        return (0, 1)

def f(x):
    if mode == '5.8':
        return math.log(x)
    if mode == '5.10':
        return math.sin(x)/x
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
    if mode == '7a':
        return x/math.sin(x)
    if mode == '7b':
        return (math.exp(x)-1)/math.sin(x)
    if mode == '7c':
        return math.atan(x)/x

def CompoundEchelon(m):
    a=bound()[0]
    b=bound()[1]
    result = f(a)+f(b)
    for i in range(1,m):
        xi = i*(b-a)/m + a
        result+=2*f(xi)
    return result/(2*m)

def CompoundSimpson(m):
    a=bound()[0]
    b=bound()[1]
    result = f(a)+f(b)
    for i in range(1,m+1):
        xi = (2*i-1)*(b-a)/(2*m) + a
        result+=4*f(xi)
    for i in range(1,m):
        xi = (2*i)*(b-a)/(2*m)+a
        result+=2*f(xi)
    return result/(6*m)

def CompoundMidpoint(m):
    a=bound()[0]
    b=bound()[1]
    result = 0
    halfh = (b-a)/(2*m)
    for i in range(0, m):
        xi = i*(b-a)/m+a+halfh
        result+=f(xi)
    return result/m

if __name__ == "__main__":
    for i in range(97,104):
        mode = chr(i)
        print('(%c):'%mode)
        for m in [16, 32]:
            print(CompoundEchelon(m))
            # print(CompoundSimpson(m))
    for mode in ['7a', '7b', '7c']:
        print('(%s):'%mode)
        for m in [16, 32]:
            print(CompoundMidpoint(m))
