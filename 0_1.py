import numpy as np
def nest(x):
    sum =0
    for i in range(0, 51):
        sum+=(x**i)
    return sum

def Q(x):
    return (x**51-1)/(x-1)

if __name__ == '__main__':
    x = 1.00001
    a1 = nest(x)
    a2 = Q(x)
    print(a1)
    print(a2)
    print(a1-a2)
    
