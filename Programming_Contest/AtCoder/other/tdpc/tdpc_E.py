d = int(input())
n = input()
mod = 10**9+7

dp = [[[0] * 2 for _ in range(d)] for _ in range(len(n)+1)]
#dp[i][j[0]:上位i桁をみたらnと一致していてdで割った余りがjになるパターン数
#dp[i][j[1]:上位i桁をみたらn未満てdで割った余りがjになるパターン数
dp[0][0][0] = 1
for i in range(len(n)):
    for j in range(d):
        for x in range(10):
            dp[i+1][(j+x)%d][1] += dp[i][j][1]
            dp[i+1][(j+x)%d][1] %= mod
        for x in range(int(n[i])):
            dp[i+1][(j+x)%d][1] += dp[i][j][0]
            dp[i+1][(j+x)%d][1] %= mod
        dp[i+1][(j+int(n[i]))%d][0] += dp[i][j][0]
        dp[i+1][(j+int(n[i]))%d][0] %= mod

print(dp[len(n)][0][0] + dp[len(n)][0][1]-1)
#0はdの倍数