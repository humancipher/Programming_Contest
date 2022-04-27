w = int(input())
n,k = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * (w+1) for _ in range(k+1)]
for s in range(n):
    [a,b] = AB[s]
    for t in reversed(range(k)):
        for u in reversed(range(w+1)):
            if u-a >= 0:
                dp[t+1][u] = max(dp[t+1][u],dp[t][u],dp[t][u-a]+b)
            else:
                dp[t+1][u] = max(dp[t+1][u],dp[t][u])
print(dp[k][w])
