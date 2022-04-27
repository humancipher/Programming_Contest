n = int(input())
A = list(map(int,input().split()))
mod = 998244353

dp = [[0 for _ in range(10)] for _ in range(n)]
#dp[i][j]:i回目の操作でAの一番左がjになるパターン数

dp[0][A[0]]= 1

for i in range(1,n):
    for j in range(10):
        for k in range(10):
            if k == (j+A[i]) % 10:
                dp[i][k] += dp[i-1][j]
                dp[i][k] %= mod
            if k == (j*A[i]) % 10:
                dp[i][k] += dp[i-1][j]
                dp[i][k] %= mod
        
for j in range(10):
    print(dp[-1][j])
