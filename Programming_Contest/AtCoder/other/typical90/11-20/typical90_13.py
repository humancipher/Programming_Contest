from heapq import heappush,heapify,heappop
INF = 10**10

def dijkstra(G,n,st):
    D = [INF for _ in range(n+1)]
    D[st] = 0
    hq = []
    heapify(hq)
    heappush(hq,[0,st])
    while len(hq) > 0:
        (tmp,now) = heappop(hq)
        for (nxt,dist) in G[now]:
            if D[nxt] > D[now] + dist:
                heappush(hq,[D[now]+dist,nxt])
                D[nxt] = D[now] + dist
    return D

def main():
    n,m = map(int,input().split())
    G = [set() for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        G[a].add((b,c))
        G[b].add((a,c))
    D_from = dijkstra(G,n,1)
    D_to = dijkstra(G,n,n)
    for i in range(1,n+1):
        print(D_from[i]+D_to[i])

if __name__ == "__main__":
    main()
