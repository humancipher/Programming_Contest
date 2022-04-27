from math import sqrt

N = 10001
INF = 2*10**5

def Eratos(n):
    A = [True for _ in range(n+1)]
    #A[i]:iが素数かどうか
    A[0],A[1] = False,False
    P = []
    for i in range(2,int(sqrt(n))+1):
        if A[i]:
            for j in range(2,(n // i)+1):
                A[i*j] = False
    for i in range(2,n+1):
        if A[i]:
            P.append(i)
    return P

P = Eratos(INF)
print(P[N-1])
