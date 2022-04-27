INF = 10**9

n,m = map(int,input().split())
A = list()
C = list()
for _ in range(m):
    a,b = map(int,input().split())
    A.append(a)
    Ci = list(map(int,input().split()))
    C.append(Ci)

dp = [[INF] * 2**n for _ in range(m+1)]
dp[0][0] = 0
for i in range(m):
    a = A[i]
    ci = 0
    for j in range(len(C[i])):
        ci += 2**(C[i][j]-1)
    for j in range(2**n):
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])
        dp[i+1][j|ci] = min(dp[i][j]+a,dp[i][j|ci],dp[i+1][j|ci])
if dp[m][2**n-1] == INF:
    print(-1)
else:
    print(dp[m][2**n-1])
