def gcd(a,b):
    if a < b:
        a,b = b,a
    if b == 0:
        return a
    else:
        while True:
            r = a % b
            if r == 0:
                return b
            else:
                a,b = b,r

def GCD(A):
    if len(A) == 1:
        return A[0]
    elif len(A) == 2:
        g = gcd(A[0],A[1])
    else:
        g = gcd(A[0],A[1])
        for i in range(2,len(A)):
            g = gcd(g,A[i])
    return g

N,X = map(int,input().split())
x = list(map(int,input().split()))
x.append(X)

x.sort()
for i in reversed(range(N+1)):
    x[i] -= x[0]

ans = GCD(x)
print(ans)
