from heapq import heapify,heappop,heappush

INF = 1 << 60

def dijkstra(E_cost,N,st): #E:(from,to,cost)
    E,Cost = [set([]) for _ in range(N)],{} #Cost((from,to))でe=(from,to)のコストを出力
    for i in range(len(E_cost)):
        E[E_cost[i][0]].add(E_cost[i][1]) #頂点E[from] = {v in V | (from,v) in E}
        Cost[(E_cost[i][0],E_cost[i][1])] = E_cost[i][2]

    D = [[0,st]]
    heapify(D)
    Dist = [INF for _ in range(N)]

    V = set([i for i in range(N)])
    while len(D) > 0 and len(V) > 0:
        p = heappop(D)
        if p[1] in V:
            Dist[p[1]] = p[0]
            V.discard(p[1])
            for v in V & E[p[1]]:
                if Dist[v] > Dist[p[1]] + Cost[p[1],v]:
                    Dist[v] = Dist[p[1]] + Cost[p[1],v]
                    heappush(D,[Dist[v],v])
    
    return Dist

def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    E = [list(map(int,input().split())) for _ in range(M)]
    
    for i in range(M):
        E[i][0] -= 1
        E[i][1] -= 1
    
    E_rev = [[E[i][1],E[i][0],E[i][2]] for i in range(M)]

    go = dijkstra(E,N,0)
    rev = dijkstra(E_rev,N,0)

    Money = [(T - go[i] - rev[i]) * A[i] for i in range(N)]

    print(max(Money))

if __name__ == "__main__":
    main()
