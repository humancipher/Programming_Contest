from heapq import heapify,heappop,heappush

INF = 1 << 60

def dijkstra(E,Cost,N,st): #E[i] = set([頂点iから出る先]),Cost[(i,j)]=辺(i,j)のコスト
    Dist = [INF] * N
    H = [(0,st)]
    heapify(H)
    Visit = [True for _ in range(N)] #Visit[i]:頂点iが未訪問かどうか
    while len(H) > 0:
        (pc,px) = heappop(H)
        if Dist[px] > pc:
            Dist[px] = pc
            Visit[px] = False
            for y in E[px]:
                if Visit[y]:
                    if Dist[y] > Dist[px] + Cost[(px,y)]:
                        heappush(H,(Dist[px] + Cost[(px,y)],y))
    return Dist