mod = 998244353

n,m,k,s,t,x = map(int,input().split())
G = [set() for _ in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    G[u-1].add(v-1)
    G[v-1].add(u-1)
dp = [[0,0] for _ in range(n)]
#dp[i][j][k]:i番目まで見て末尾がjでxの出現数 % 2 = kであるパターン数
if s != x:
    dp[s-1][0] = 1
else:
    dp[s-1][1] = 1
for c in range(k):
    ndp = [[0,0] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            for k in range(2):
                if j == x-1:
                    ndp[j][(k+1)%2] += dp[i][k]
                    ndp[j][(k+1)%2] %= mod
                else:
                    ndp[j][k] += dp[i][k]
                    ndp[j][k] %= mod
    dp = ndp
print(dp[t-1][0])