INF = 10**5

n = int(input())
x,y = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(n)]

dp = [[INF] * (y+1) for _ in range(x+1)]
dp[0][0] = 0
#dp[i][j]:タコ焼きi個、たい焼きj個を手に入れるために必要な弁当の最小数

for k in range(n):
    a,b = AB[k][0],AB[k][1]
    for i in reversed(range(x+1)):
        for j in reversed(range(y+1)):
            dp[min(x,i+a)][min(y,j+b)] = min(dp[min(x,i+a)][min(y,j+b)],dp[i][j]+1)

if dp[x][y] == INF:
    print(-1)
else:
    print(dp[x][y])
