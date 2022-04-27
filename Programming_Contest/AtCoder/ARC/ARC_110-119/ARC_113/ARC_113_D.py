N,M,K = map(int,input().split())
mod = 998244353
ans = 0
if N != 1 and M != 1:
    for s in range(1,K+1):
        u = pow(s,N,mod) - pow(s-1,N,mod)
        v = pow(K-s+1,M,mod)
        tmp = u*v % mod
        ans += tmp
        ans %= mod
else:
    ans = pow(K,N*M,mod)
print(ans)