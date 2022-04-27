mod = 998244353

h,w,k = map(int,input().split())
sx,sy,gx,gy = map(int,input().split())

dp = [[[0] * 2 for _ in range(2)] for _ in range(k+1)]
if sx == gx and sy == gy:
    dp[0][1][1] = 1
elif sx == gx and sy != gy:
    dp[0][1][0] = 1
elif sx != gx and sy == gy:
    dp[0][0][1] = 1
else:
    dp[0][0][0] = 1

for i in range(k):
    dp[i+1][0][0] = (w-1)*dp[i][0][1] + (h-1)*dp[i][1][0] + (max(0,w-2)+max(0,h-2))*dp[i][0][0]
    dp[i+1][0][0] %= mod
    dp[i+1][1][0] = dp[i][0][0] + (max(0,w-2))*dp[i][1][0] + (w-1)*dp[i][1][1]
    dp[i+1][1][0] %= mod
    dp[i+1][0][1] = dp[i][0][0] + (max(0,h-2))*dp[i][0][1] + (h-1)*dp[i][1][1]
    dp[i+1][0][1] %= mod
    dp[i+1][1][1] = dp[i][0][1] + dp[i][1][0]
    dp[i+1][1][1] %= mod
print(dp[k][1][1])
