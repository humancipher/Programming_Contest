from math import sqrt

def Eratos(n):
    L = [True for _ in range(n)]
    L[0],L[1],P = False,False,set()
    for i in range(2,int(sqrt(n))+1):
        if L[i]:
            d = (n-1) // i
            for j in range(2,d+1):
                L[i*j] = False
    for i in range(n):
        if L[i]:
            P.add(i)
    return P

def judge(P,n):
    n,S = str(n),set()
    for i in range(len(n)-1):
        n = n[1:] + n[:1]
        S.add(int(n))
    for s in S:
        if s not in P:
            return False
    return True

N = 10**6
P = Eratos(N)

ans = 0
for p in P:
    if judge(P,p):
        ans += 1
print(ans)
