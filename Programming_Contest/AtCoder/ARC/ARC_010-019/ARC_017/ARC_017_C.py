from bisect import bisect_left,bisect_right

def half(W,x,n):
    NP = list()
    for i in range(2**n):
        tmp = 0
        for j in range(n):
            if i & 2**j:
                tmp += W[j]
        if tmp <= x:
            NP.append(tmp)
    NP.sort()
    return NP

def solve(W,n,x):
    H1,H2 = half(W[:n//2],x,n//2),half(W[n//2:],x,len(W[n//2:]))
    ans = 0
    for h1 in H1:
        ans += bisect_right(H2, x-h1) - bisect_left(H2, x-h1)
    return ans

n,x = map(int,input().split())
W = [int(input()) for _ in range(n)]
print(solve(W, n, x))
