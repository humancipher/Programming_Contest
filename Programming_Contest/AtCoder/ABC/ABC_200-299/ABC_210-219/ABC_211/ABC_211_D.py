from collections import deque

mod = 10**9+7
INF = 10**10

n,m = map(int,input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

dp = [0] * (n+1)
dp[1] = 1
dist = [INF] * (n+1)
dist[1] = 0
Q = deque()
Q.append(1)
while len(Q) > 0:
    now = Q.popleft()
    for nxt in G[now]:
        if dist[nxt] == INF:
            Q.append(nxt)
            dist[nxt] = dist[now] + 1
            dp[nxt] += dp[now]
            dp[nxt] %= mod
        elif dist[nxt] == dist[now] + 1:
            dp[nxt] += dp[now]
            dp[nxt] %= mod
print(dp[n])
