n,m = map(int,input().split())
C = list(map(int,input().split()))

INF = 10**9

dp = [INF for _ in range(n+1)] #dp[i] := i円での最小枚数
dp[0] = 0
for i in range(m):
    if C[i] < n+1:
        dp[C[i]] = 1

for i in range(n+1):
    for j in range(m):
        if i-C[j] >= 0:
            dp[i] = min(dp[i],dp[i-C[j]] + 1)

print(dp[n])
