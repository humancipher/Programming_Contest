n = int(input())
S = input()

mod = 10**9+7
T = "atcoder"
dp = [[0 for _ in range(len(T)+1)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
#dp[i][j]:Sのi文字目まででTのj文字目までの部分文字列を作るパターン数
for i in range(n):
    for j in range(len(T)):
        dp[i+1][j+1] += dp[i][j+1]
        if S[i] == T[j]:
            dp[i+1][j+1] += dp[i][j]
        dp[i+1][j+1] %= mod
print(dp[n][len(T)])