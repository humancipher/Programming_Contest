from heapq import heapify,heappop,heappush
from sys import stdin
input = stdin.readline
INF = 10**7

def dijkstra(G,n,st):
    D = [INF] * n
    D[st] = 0
    HQ = [[0,st]]
    heapify(HQ)
    while len(HQ) > 0:
        dist,now = heappop(HQ)
        for nxt,diff in G[now]:
            if D[nxt] > dist + diff:
                D[nxt] = dist + diff
                heappush(HQ,[dist+diff,nxt])
    return D

def main():
    n,m = map(int,input().split())
    G = [list() for _ in range(n)]
    s,t = map(int,input().split())
    for _ in range(m):
        x,y,d = map(int,input().split())
        G[x-1].append((y-1,d))
        G[y-1].append((x-1,d))
    From = dijkstra(G,n,s-1)
    To = dijkstra(G,n,t-1)

    ans = -1
    for i in range(n):
        if From[i] == To[i] and From[i] != INF:
            ans = i+1
            break
    print(ans)

if __name__ == "__main__":
    main()
