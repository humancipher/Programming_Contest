from math import gcd
A = [i+1 for i in range(20)]

def GCD(S):
    g = S[0]
    for i in range(1,len(S)):
        g = gcd(g,S[i])
    return g

def LCM(S):
    l = S[0]
    for i in range(1,len(S)):
        l = l*S[i] // gcd(l,S[i])
    return l

ans = LCM(A)
print(ans)
