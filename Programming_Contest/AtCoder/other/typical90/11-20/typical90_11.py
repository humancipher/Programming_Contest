n = int(input())
DCS = [list(map(int,input().split())) for _ in range(n)]

limit = 5000
DCS.sort(key = lambda x:x[0])
dp = [0] * (limit+1) #dp[i][j]:i個目の仕事まで見てj日後までに終了できるタスクの最適解
for i in range(n):
    d,c,s = DCS[i][0],DCS[i][1],DCS[i][2]
    ndp = [0] * (limit+1)
    for j in range(1,limit+1):
        ndp[j] = max(dp[j],ndp[j-1])
        if j <= d and j >= c:
            ndp[j] = max(dp[j-c]+s,ndp[j])
    dp = ndp
print(dp[limit])