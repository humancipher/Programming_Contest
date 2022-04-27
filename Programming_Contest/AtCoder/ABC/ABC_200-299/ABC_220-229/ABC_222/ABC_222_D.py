n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
mod = 998244353

dp = [[0] * 3001 for _ in range(n)]
#dp[i][j]:i番目がjになるパターン数
for j in range(A[0],B[0]+1):
    dp[0][j] = 1
"""
for i in range(n-1):
    for j in range(A[i],B[i]+1):
        for k in range(A[i+1],B[i+1]+1):
            if j <= k:
                dp[i+1][k] += dp[i][j]
                dp[i+1][k] %= mod
"""
for i in range(n-1):
    for j in range(1,3001):
        dp[i][j] += dp[i][j-1]
        dp[i][j] %= mod
    for j in range(A[i+1],B[i+1]+1):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= mod
    

ans = 0
for j in range(A[n-1],B[n-1]+1):
    ans += dp[n-1][j]
    ans %= mod
print(ans)
