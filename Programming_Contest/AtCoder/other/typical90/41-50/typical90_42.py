mod = 10**9+7
k = int(input())

if k % 9 != 0:
    ans = 0
else:
    dp = [0 for _ in range(k+1)]
    dp[0] = 1
    for i in range(k+1):
        for j in range(1,10):
            if i-j >= 0:
                dp[i] += dp[i-j]
                dp[i] %= mod
    ans = dp[k]
print(ans)
