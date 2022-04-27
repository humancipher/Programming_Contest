N,W = map(int,input().split())
VW = [list(map(int,input().split())) for i in range(N)]
Val = [VW[i][0] for i in range(N)]
Wei = [VW[i][1] for i in range(N)]

dp = [[0 for j in range(W+1)] for i in range(N+1)]
#dp[i][j]:i番目までで重さがjまででの価値の最大値

for i in range(1,N+1):
    for j in range(1,W+1):
        if j - Wei[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j],dp[i][j-Wei[i-1]]+Val[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][W])
