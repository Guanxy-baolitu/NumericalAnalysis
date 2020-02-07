import math

def f(n):
    r = 0.5*(10**(-8))
    x = 2
    pre = 1
    stepcnt = 0
    while math.fabs(x-pre)>=r and stepcnt <=10000:
        pre = x
        x = (x+(n/x))/2
        stepcnt+=1
    return (x, stepcnt)


if __name__ == "__main__":
    print(f(3))
    print(f(5))