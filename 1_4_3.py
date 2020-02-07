import math

def f(x,idx):
    result = 0
    if idx =='a':
        result = 27*(x**3)+54*(x**2)+36*x+8
    if idx=='b':
        result = 36*(x**4)-12*(x**3)+37*(x**2)-12*x+1
    return result

def f_(x, idx):
    result =0
    if idx=='a':
        result = 27*3*(x**2)+54*2*x+36
    if idx=='b':
        result = 36*4*(x**3)-12*3*(x**2)+37*2*x-12
    return result

def f_2(x,idx):
    result = 0
    if idx=='a':
        result = 27*3*2*x+54*2
    if idx =='b':
        result = 36*4*3*(x**2)-12*3*2*x+37*2
    return result

def f_3(x,idx):
    result=0
    if idx=='a':
        result = 27*3*2
    if idx =='b':
        result = 36*4*3*2*x-12*3*2
    return result

def f_4(x, idx):
    result=0
    if idx=='a':
        return 0
    if idx=='b':
        result = 36*4*3*2
    return result

def Newton(idx):
    r = 10**(-16)
    pre = 0
    x =1
    while math.fabs(pre-x)>=r:
        pre=x
        x=x-f(x,idx)/f_(x,idx)
    return x


if __name__ =="__main__":
    for t in ['a', 'b']:
        r=Newton(t)
        print('answer:%f' % r)
        m=1
        print(f_(r, t))
        if math.fabs(f_(r, t))<10**(-3):
            m+=1
            print(f_2(r, t))
            if math.fabs(f_2(r, t))<10**(-3):
                m+=1                
                print(f_3(r, t))
                if math.fabs(f_3(r, t))<10**(-3):
                    m+=1
                    print(f_4(r, t))
                    if math.fabs(f_4(r, t))<10**(-3):
                        m+=1
        print('m=%d' % m)
