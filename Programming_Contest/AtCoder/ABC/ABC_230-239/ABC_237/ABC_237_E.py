#注：負の辺があるとダイクストラは嘘解放

from heapq import heapify,heappop,heappush
INF = 10**15

def dijkstra(G,H,n,st):
    D = [INF] * n
    Q = []
    heapify(Q)
    D[st] = 0
    heappush(Q,(0,st))
    while len(Q) > 0:
        dist,now = heappop(Q)
        for nxt,diff in G[now]:
            if D[nxt] > dist + diff:
                D[nxt] = dist + diff
                heappush(Q,(dist + diff,nxt))
    ans = 0
    for i in range(n):
        ans = max(ans,-H[i]-D[i])
    return ans

def main():
    import sys
    input = sys.stdin.readline
    n,m = map(int,input().split())
    H = list(map(int,input().split()))
    for i in range(n-1,-1,-1):
        H[i] -= H[0]
    G = [list() for _ in range(n)]
    #G[i]:(a,b):頂点iから頂点aに行くための余計なコスト
    #H[i]への距離は余計なコスト+ H[i] - H[0]
    for _ in range(m):
        u,v = map(int,input().split())
        u,v = u-1,v-1
        if H[u] <= H[v]:
            G[u].append((v,H[v]-H[u])) #可変の必要がないならtupleの方が何かとアクセスが速い
            G[v].append((u,0))
        if H[u] >= H[v]:
            G[u].append((v,0))
            G[v].append((u,H[u]-H[v]))

    ans = dijkstra(G,H,n,0)
    print(ans)

if __name__ == "__main__":
    main()
