import math

m = (2**31)-1
a=7**5
n=4
def NormalRandom():
    x=[(a%m)]
    u=[x[0]/m]
    for i in range(1, 2*10**n):
        x.append((a*x[i-1])%m)
        u.append(x[i]/m)
        # print("x=%d u=%.4f"%(x[i], u[i]))
    return u

mode = '9.8'
def bound():
    if mode == '9.8':
        return (-3,6)
    if mode == 'a':
        return (-2, 5)
    if mode == 'b':
        return (-5, 3)
    if mode == 'c':
        return (-8, 3)

times = 0
pUp = 0.3 # 题1 0.5
def wander(u):
    b=-bound()[0]
    a=bound()[1]
    w=0
    global times
    i=int(2*a*b*times%len(u))
    times+=1
    while w!=a and w!=(-b) and i<len(u):
        p=u[i]
        if p>pUp:
            w+=1
        else:
            w-=1
        i = ((i+1)%len(u))
    if w==a:
        return True
    if w==(-b):
        return False



def MontoCarlo2(u):
    cnt=0
    for i in range(0, len(u)):
        if wander(u)==True:
            cnt+=1
    print('(%s) %.8f'%(mode, cnt/len(u)))
    return

if __name__ == "__main__":
    u = NormalRandom()
    MontoCarlo2(u)
    for i in range(97,100):
        mode = chr(i)
        MontoCarlo2(u)