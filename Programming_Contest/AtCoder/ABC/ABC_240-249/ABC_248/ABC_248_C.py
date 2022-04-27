mod = 998244353
n,m,k = map(int,input().split())

dp = [0] * (k+1)
dp[0] = 1
for _ in range(n):
    ndp = [0] * (k+1)
    for i in range(k+1):
        for j in range(1,m+1):
            if i+j <= k:
                ndp[i+j] += dp[i]
                ndp[i+j] %= mod
    dp = ndp
ans = 0
for i in range(1,k+1):
    ans += dp[i]
    ans %= mod
print(ans)