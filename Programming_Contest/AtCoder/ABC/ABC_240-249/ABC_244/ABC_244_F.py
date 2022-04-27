from collections import deque
INF = 10**6

n,m = map(int,input().split())
G = [[False] * n for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    G[a-1][b-1] = True
    G[b-1][a-1] = True

dp = [[INF] * n for _ in range(2**n)]
#dp[i][j]:ビットパターンiで今いるノードがjである最短パス
Q = deque()
for j in range(n):
    Q.append([2**j,j])
    dp[2**j][j] = 1
while Q:
    bit,now = Q.popleft()
    for nxt in range(n):
        if G[now][nxt]:
            if dp[bit^2**nxt][nxt] > dp[bit][now] + 1:
                Q.append([bit^2**nxt,nxt])
                dp[bit^2**nxt][nxt] = dp[bit][now] + 1
ans = 0
for i in range(1,2**n):
    ans += min(dp[i])
print(ans)