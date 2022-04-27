INF = 10**8

n,m = map(int,input().split())
W = list(map(int,input().split()))

dp = [[INF] * (sum(W)+1) for _ in range(n+1)]
#dp[i][j]:i番目までを見て和をjにするためのボールの選び方の最小数
dp[0][0] = 0
for i in range(1,n+1):
    for j in range(len(dp[i])):
        if j >= W[i-1]:
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-W[i-1]]+1)
        else:
            dp[i][j] = dp[i-1][j]

if dp[n][m] == INF:
    print(-1)
else:
    print(dp[n][m])
