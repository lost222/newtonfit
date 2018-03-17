import numpy as np
a = np.array([1, 2, 3])
print(a)

#pythoon 可以return数组

def getMatrix(x,y):
    Mit = np.zeros((x.size, x.size))
    Mit[:,0] = Mit[0]+y
    for i in range(1, x.size):
        for j in range(i, x.size):
            Mit[j, i] = (Mit[j-1, i-1] - Mit[j, i-1])/(x[j-1]-x[j])  #赋值
    return Mit

a = np.array([1,2,4,5,6,8])
b = np.array([0,2,8,12,18,28])

mit = getMatrix(a,b)

def mypolyffit(x,y,n,t):      #t是f(t)需要的自变量
    tminus = t-x
    mit = getMatrix(x,y)
    sum = y[0]
    for i in range(1, n+1):
        r = tminus[0]
        for j in range(1, i):
            r = r*tminus[j]
        sum = sum + mit[i, i]*r
    return sum

ans = mypolyffit(a,b,2,1.5)


# def getRn(x, y, t, n):
#     mit = getMatrix(x, y)
#     tminus = x-t
#     s = mit[n+1]
#     tline = np.zeros(n+1)
#     tline[0]=t
#     for i in range(1, n+2):
#         tline[i] = (s[i-1]-tline[i-1])/tminus[n+1-i]
#     return tline[n+1]


fp = np.polyfit(a, b, 2)
f2 = np.poly1d(fp)

getRn(a,b,1.5,2)
ans2 = f2(1.5)