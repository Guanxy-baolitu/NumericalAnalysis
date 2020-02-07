import math # DOUBT

m = (2**31)-1
a=16807

# m=31 #9.1
# a=13

def NormalRandom():
    x=[((a*1)%m)]
    u=[x[0]*1.0/m]
    for i in range(1, 10**6):
        x.append((a*x[i-1])%m)
        u.append(x[i]/m)
        # print("x=%d u=%.4f"%(x[i], u[i]))
    return u

def V():
    u = NormalRandom()
    cnt =0
    for i in range(2, len(u)):
        if f(u[i-2], u[i-1], u[i]) == True:
            cnt+=1
    return (cnt/(len(u)-2))*1.0


def f(x, y, z):
    v = pow(x-(1/3),2)+pow(y-(1/3),2)+pow(z-(1/2), 2)
    if v<=(0.04**2):
        return True
    return False




if __name__ == "__main__":
    print(V())