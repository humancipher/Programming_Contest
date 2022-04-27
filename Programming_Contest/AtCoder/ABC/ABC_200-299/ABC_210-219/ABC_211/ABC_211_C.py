S = input()
mod = 10**9+7

C = "chokudai"
dp = [[0] * (len(C)+1) for _ in range(len(S)+1)]
for i in range(len(S)+1):
    dp[i][0] = 1

for i in range(len(S)):
    for j in range(len(C)):
        if S[i] == C[j]:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod
        dp[i+1][j+1] += dp[i][j+1]
        dp[i+1][j+1] %= mod
print(dp[len(S)][len(C)])
