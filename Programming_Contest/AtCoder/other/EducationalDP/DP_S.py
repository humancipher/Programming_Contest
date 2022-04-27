mod = 10**9+7

n = list(input())
n = [int(n[i]) for i in range(len(n))]
d = int(input())

dp = [[[0] * 2 for _ in range(d)] for _ in range(len(n)+1)]
#dp[i][j][0]:i桁目までを見て余りがjのパターン数
dp[0][0][0] = 1
for i in range(len(n)):
    for j in range(d):
        for k in range(10):
            dp[i+1][(j+k) % d][1] += dp[i][j][1]
            dp[i+1][(j+k) % d][1] %= mod
        for k in range(n[i]):
            dp[i+1][(j+k) % d][1] += dp[i][j][0]
            dp[i+1][(j+k) % d][1] %= mod
        dp[i+1][(j+n[i]) % d][0] += dp[i][j][0]
        dp[i+1][(j+n[i]) % d][0] %= mod

ans = (dp[len(n)][0][0] + dp[len(n)][0][1] - 1) % mod #0もdの倍数
print(ans)