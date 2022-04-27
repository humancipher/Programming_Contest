N,W = map(int,input().split())
VW = [list(map(int,input().split())) for _ in range(N)]
Val = [VW[i][0] for i in range(N)]
Wei = [VW[i][1] for i in range(N)]

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
#dp[i][j]:=i番目までの品物で重さjまででの価値の合計の最大値

for n in range(1,N+1):
    for w in range(W+1):
        if w - Wei[n-1] >= 0:
            dp[n][w] = max(dp[n-1][w],dp[n-1][w-Wei[n-1]]+Val[n-1])
        else:
            dp[n][w] = dp[n-1][w]
print(dp[n][w])
