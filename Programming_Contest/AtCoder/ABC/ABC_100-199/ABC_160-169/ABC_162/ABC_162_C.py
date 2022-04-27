from math import gcd

K = int(input())

def GCD(a,b,c):
    g = gcd(a,b)
    g = gcd(g,c)
    return g

ans = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            ans += GCD(a,b,c)

print(ans)
