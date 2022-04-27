from math import log2,ceil

N,K = map(int,input().split())

ans = 0
for n in range(1,N+1):
    if K <= n:
        ans += 1/N
    else:
        ans += pow(1/2,ceil(log2(K / n)))/N
print(ans)
