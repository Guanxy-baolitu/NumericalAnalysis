import math

def a_ori(x):
    return (1-1/math.cos(x))/math.tan(x)

def a_fix(x):
    return -(math.cos(x)/(math.cos(x)+1))

def b_ori(x):
    return (1-((1-x)**3))/x

def b_fix(x):
    return (-(x**6)+6*(x**5)-15*(x**4)+20*(x**3)-15*(x**2)+6*x)/(x+(x*((1-x)**3)))

if __name__ == '__main__':
    for i in range(1, 15):
        x = 10**(-i)
        print('{:8.8g}：{:30.18g} {:30.18g}'.format(x, a_ori(x), a_fix(x)))

    for i in range(1, 15):
        x = 10**(-i)
        print('{:8.8g}：{:30.18g} {:30.18g}'.format(x, b_ori(x), b_fix(x)))