mod = 998244353

n = int(input())
S = input()
Type = []
for i in range(n):
    Type.append(ord(S[i])-ord("A"))
dp = [[[0] * 11 for _ in range(2**10)] for _ in range(n+1)]
#dp[i][j][k]:i番目までを見て出場パターンがjで直前に出たのがkであるパターン数
dp[0][0][10] = 1
for i in range(n):
    for j in reversed(range(2**10)):
        for k in range(11):
            dp[i+1][j][k] += dp[i][j][k]
            dp[i+1][j][k] %= mod
            if j & 2**Type[i] == 0 and k != Type[i]:
                dp[i+1][j | 2**Type[i]][Type[i]] += dp[i][j][k]
                dp[i+1][j | 2**Type[i]][Type[i]] %= mod
        dp[i+1][j][Type[i]] += dp[i][j][Type[i]]
        dp[i+1][j][Type[i]] %= mod
ans = 0
for j in range(1,2**10):
    for k in range(10):
        ans += dp[n][j][k]
        ans %= mod
print(ans)