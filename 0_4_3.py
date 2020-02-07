import math

def f_ori(a,b):
    return (a+math.sqrt((a**2)+(b**2)))

def f_fix(a,b):
    return -(b**2)/(a-math.sqrt((a**2)+(b**2)))

if __name__ == '__main__':
    a=-12345678987654321
    b=123
    print('{:30.18g} {:30.18g}'.format(f_ori(a,b), f_fix(a,b)))