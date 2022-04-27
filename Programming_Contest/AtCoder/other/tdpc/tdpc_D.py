n,d = map(int,input().split())

Div = dict()
Div[2],Div[3],Div[5] = 0,0,0
for i in range(2,6):
    while d % i == 0:
        Div[i] += 1
        d //= i
if d != 1:
    ans = 0
else:
    dp = [[[[0 for _ in range(Div[5]+1)] for _ in range(Div[3]+1)]for _ in range(Div[2]+1)] for _ in range(n+2)]
    dp[0][0][0][0] = 1
    #dp[i][j][k][l]:i回目までで2でj回,3でk回,5でl回割り切れる確率
    for i in range(n):
        for j in range(Div[2]+1):
            for k in range(Div[3]+1):
                for l in range(Div[5]+1):
                    dp[i+1][j][k][l] +=  dp[i][j][k][l] / 6
                    dp[i+1][min(j+1,Div[2])][k][l] += dp[i][j][k][l] / 6
                    dp[i+1][j][min(k+1,Div[3])][l] +=  dp[i][j][k][l] / 6
                    dp[i+1][min(j+2,Div[2])][k][l] +=  dp[i][j][k][l] / 6
                    dp[i+1][j][k][min(l+1,Div[5])] +=  dp[i][j][k][l] / 6
                    dp[i+1][min(j+1,Div[2])][min(k+1,Div[3])][l] +=  dp[i][j][k][l] / 6
    ans = dp[n][-1][-1][-1]
print(ans)
