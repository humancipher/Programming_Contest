d,g = map(int,input().split())
g //= 100
PC = []
for _ in range(d):
    p,c = map(int,input().split())
    PC.append([p,c//100])

dp = [[0] * 1001 for _ in range(d+1)]
#dp[i][j]:i種類目の問題まででj問解いて得られる最大スコア//100
for i in range(d):
    [p,c] = PC[i]
    for j in range(1001):
        if j >= p:
            dp[i+1][j] = max(dp[i+1][j],dp[i][j],dp[i][j-p]+(i+1)*p+c)
        else:
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
        for k in range(1,min(j,p)+1):
            dp[i+1][j] = max(dp[i+1][j],dp[i][j],dp[i][j-k]+(i+1)*k)
for j in range(1001):
    if dp[d][j] >= g:
        ans = j
        break
print(ans)
