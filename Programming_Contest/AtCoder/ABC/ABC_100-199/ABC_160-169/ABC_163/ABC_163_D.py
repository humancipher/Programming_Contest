def sum_n(n,M):
    return n*(n+1)//2 % M

def cmb(n,k,M):
    max_sum,min_sum = sum_n(n,M)-sum_n(n-k,M),sum_n(k-1,M)
    return (max_sum - min_sum + 1) % M

N,K = map(int,input().split())
M = 10**9+7

ans = 0
for k in range(K,N+2):
    ans = (ans + cmb(N,k,M)) % M

print(ans)
