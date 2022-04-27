from math import sqrt

mod = 10**9+7

def fact(x):
    P = dict()
    for i in range(2,int(sqrt(x))+1):
        if x % i == 0:
            P[i] = 1
            x //= i
            while x % i == 0:
                P[i] += 1
                x //= i
    if x != 1:
        P[x] = 1
    return P

a,b = map(int,input().split())
D = dict()
for i in range(b+1,a+1):
    F = fact(i)
    for f in F:
        if f not in D:
            D[f] = F[f]
        else:
            D[f] += F[f]
ans = 1
for d in D:
    ans *= (D[d]+1)
    ans %= mod
print(ans)