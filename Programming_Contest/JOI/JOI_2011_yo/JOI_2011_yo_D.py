N = int(input())
A = list(map(int,input().split()))
A = [None] + A
dp = [[0 for _ in range(21)] for _ in range(N+1)]
#dp[i][j]:i番目までを見てその和がjになる有効なパターン数
dp[1][A[1]] = 1

for i in range(2,N+1):
    for j in range(21):
        if j-A[i] >= 0:
            dp[i][j] += dp[i-1][j-A[i]]
        if j+A[i] < 21:
            dp[i][j] += dp[i-1][j+A[i]]

print(dp[N-1][A[N]])
