n,a = map(int,input().split())
X = list(map(int,input().split()))

dp = [[[0] * 2501 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0][0] = 1
#dp[i][j][k]:i番目までを見てj個使い和をjにするパターン数
for i in range(n):
    x = X[i]
    for j in range(i+1):
        for k in range(2501):
            if k >= x:
                dp[i+1][j+1][k] = dp[i][j+1][k] + dp[i][j][k-x]
            else:
                dp[i+1][j+1][k] = dp[i][j+1][k]
ans = 0
for j in range(1,n+1):
    ans += dp[n][j][a*j]
print(ans)
