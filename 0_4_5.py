import math

def edge_sub(a,b):
    return ((b**2)/(math.sqrt((a**2)+(b**2))+a))

if __name__ == '__main__':
    a=3344556600
    b=1.2222222
    print('{:30.18g}'.format(edge_sub(a,b)))