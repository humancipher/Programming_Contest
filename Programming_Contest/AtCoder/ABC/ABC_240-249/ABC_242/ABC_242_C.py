mod = 998244353
n = int(input())
dp = [0] * 10 #dp[i][j]:i桁最後がjで条件を満たすxの個数
for j in range(1,10):
    dp[j] = 1

for i in range(n-1):
    ndp = [0] * 10
    for j in range(1,10):
        if j >= 2:
            ndp[j] += dp[j-1]
        ndp[j] += dp[j]
        if j < 9:
            ndp[j] += dp[j+1]
        ndp[j] %= mod
    dp = ndp

ans = 0
for j in range(1,10):
    ans += dp[j]
    ans %= mod
print(ans)