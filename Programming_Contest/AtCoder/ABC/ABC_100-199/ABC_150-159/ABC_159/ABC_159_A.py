import math

N,M = map(int,input().split())

def comb(n,k):
    if n >= k:
        return math.factorial(n) // (math.factorial(n-k) * math.factorial(k))
    else:
        return 0
ans = comb(N,2)+comb(M,2)
print(ans)
