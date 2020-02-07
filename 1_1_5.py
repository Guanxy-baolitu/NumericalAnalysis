import math

def pow_1_3(a, b, A):
    r = 0.5*(10**(-8))
    while b-a >= r:
        c = (a+b)/2
        f_c = c**3-A
        if ((a**3)-A)*f_c<0:
            b=c
        else:
            a=c
    return (a+b)/2

if __name__ == '__main__':
    print(math.ceil(8*math.log(10)/math.log(2)))
    print(pow_1_3(1,2,2))
    print(pow_1_3(1,2,3))
    print(pow_1_3(1,2,5))