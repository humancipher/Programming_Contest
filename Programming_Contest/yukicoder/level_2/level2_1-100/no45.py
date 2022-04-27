n = int(input())
V = list(map(int,input().split()))

dp = [[0 for _ in range(2)] for _ in range(n+1)]
#dp[i][j]:i番目まででのおいしさの最大値（j=0:i番目で食べる、j=1:i番目で食べない）
for i in range(n):
    dp[i+1][0] = max(dp[i][0],dp[i][1]+V[i])
    dp[i+1][1] = max(dp[i][0],dp[i][1])
print(max(dp[n][0],dp[n][1]))
