N,M = 8,200

#N種類の通貨
Cur = [1,2,5,10,20,50,100,200]

#dp[i][j]:i番目までのコインでjペンスを作る方法のパターン数
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 1

for i in range(1,N+1):
    for j in range(1,M+1):
        for k in range(M+1):
            if j >= k*Cur[i-1]:
                dp[i][j] += dp[i-1][j-k*Cur[i-1]]

print(dp[N][M])
