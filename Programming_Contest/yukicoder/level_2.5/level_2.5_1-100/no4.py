n = int(input())
W = list(map(int,input().split()))

sumW = sum(W)
if sumW % 2 == 0:
    dp = [[False] * (sumW+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(sum(W)):
            if j - W[i] >= 0:
                dp[i+1][j] = dp[i][j] or dp[i][j-W[i]]
            else:
                dp[i+1][j] = dp[i][j]
    if dp[n][sumW//2]:
        ans = "possible"
    else:
        ans = "impossible"
else:
    ans = "impossible"
print(ans)