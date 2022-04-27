n = input()
k = int(input())

j_len = max(k,len(n)) #nの桁数が小さくkが大きいときにlen(n)だと足りないかもしれない
dp = [[[0] * 2 for _ in range(max(len(n),k)+1)] for _ in range(len(n)+1)]
#dp[i][j][0]:i桁目まで見てnon-0がj桁の数のパターン数(未満フラグFalse)
dp[0][0][0] = 1

for i in range(len(n)):
    for j in range(j_len):
        for s in range(1,int(n[i])):
            dp[i+1][j+1][1] += dp[i][j][0]
        for s in range(1,10):
            dp[i+1][j+1][1] += dp[i][j][1]
        if int(n[i]) == 0:
            dp[i+1][j][0] += dp[i][j][0]
            dp[i+1][j][1] += dp[i][j][1]
        else:
            dp[i+1][j+1][0] += dp[i][j][0]
            dp[i+1][j][1] += dp[i][j][0]
            dp[i+1][j][1] += dp[i][j][1]
print(dp[-1][k][0] + dp[-1][k][1])