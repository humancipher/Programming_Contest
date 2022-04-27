mod = 998244353

n,k = map(int,input().split())
LR = [list(map(int,input().split())) for _ in range(k)]

dp = [0] * (n+1)
dp[0] = 1
for i in range(1,n+1):
    tmp = 0
    for l,r in LR:
        if i-l >= 0:
            tmp += dp[i-l]
            tmp %= mod
            if i-r-1 >= 0:
                tmp -= dp[i-r-1]
                tmp %= mod
    dp[i] += dp[i-1] + tmp
    dp[i] %= mod
print((dp[n-1]-dp[n-2]) % mod)