from collections import deque
from sys import stdin
ipnut = stdin.readline
INF = 10**6

def solve(G,n,st,go):
    D = [[INF] * 3 for _ in range(n)] #D[i][j]:頂点iに3*k+j回で行く最短距離
    Q = deque()
    Q.append((st,0))
    D[st][0] = 0
    while Q:
        now,dist = Q.popleft()
        for nxt in G[now]:
            if D[nxt][(dist+1)%3] == INF:
                D[nxt][(dist+1)%3] = D[now][dist%3]+1
                Q.append((nxt,dist+1))
    if D[go][0] == INF:
        return -1
    else:
        return D[go][0]//3

def main():
    n,m = map(int,input().split())
    G = [set() for _ in range(n)]
    for _ in range(m):
        u,v = map(int,input().split())
        G[u-1].add(v-1)
    s,t = map(int,input().split())
    ans = solve(G,n,s-1,t-1)
    print(ans)
    
if __name__ == "__main__":
    main()
