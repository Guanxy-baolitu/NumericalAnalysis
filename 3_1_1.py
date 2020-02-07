
def LagrangeInterpolation_1(x1, y1, x2, y2, x):
    P = y1*(x-x2)/(x1-x2)+y2*(x-x1)/(x2-x1)
    return P

def LagrangeInterpolation_2(x1, y1, x2, y2, x3, y3, x):
    P = y1*(x-x2)*(x-x3)/((x1-x2)*(x1-x3))+y2*(x-x1)*(x-x3)/((x2-x1)*(x2-x3))+y3*(x-x1)*(x-x2)/((x3-x1)*(x3-x2))
    return P

def LagrangeInterpolation_3(x1, y1, x2, y2, x3, y3, x4, y4, x):
    P = y1*(x-x2)*(x-x3)*(x-x4)/((x1-x2)*(x1-x3)*(x1-x4))+y2*(x-x1)*(x-x3)*(x-x4)/((x2-x1)*(x2-x3)*(x2-x4))+y3*(x-x1)*(x-x2)*(x-x4)/((x3-x1)*(x3-x2)*(x3-x4))+y4*(x-x1)*(x-x2)*(x-x3)/((x4-x1)*(x4-x2)*(x4-x3))
    return P

if __name__ == "__main__":
    print(LagrangeInterpolation_1(1970,3707475887, 1990, 5281653820, 1980))
    print(LagrangeInterpolation_2(1960,3039585530, 1970, 3707475887, 1990, 5281653820,1980))
    print(LagrangeInterpolation_3(1960,3039585530, 1970, 3707475887, 1990, 5281653820,2000, 6079603571, 1980))