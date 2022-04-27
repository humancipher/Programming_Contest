INF = 10**13

def knapsack(WV,N,W):
    dp = [[INF for _ in range(10**5+1)] for _ in range(N+1)]
    #dp[i][j]:i番目までで価値jを達成する最小の重さ
    for i in range(N+1):
        dp[i][0] = 0
    for i in range(N):
        v,w = WV[i][1],WV[i][0]
        for j in range(10**5+1):
            if j-v >= 0:
                dp[i+1][j] = min(dp[i][j],dp[i][j-v]+w)
            else:
                dp[i+1][j] = dp[i][j]
    for j in reversed(range(10**5)):
        dp[N][j] = min(dp[N][j],dp[N][j+1])

    left,right = 0,10**5+1
    while right-left > 1:
        mid = (left+right)//2 #left <= W < right
        if dp[N][mid] > W:
            right = mid
        else:
            left = mid
    return left

N,W = map(int,input().split())
WV = [list(map(int,input().split())) for _ in range(N)]
print(knapsack(WV,N,W))

