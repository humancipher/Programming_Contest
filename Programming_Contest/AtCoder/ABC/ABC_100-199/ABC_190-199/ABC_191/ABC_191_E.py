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

def main():
    N,M = map(int,input().split())
    E,Cost = [set() for _ in range(N)],dict()
    for i in range(M):
        a,b,c = map(int,input().split())
        if a != b:
            E[a-1].add(b-1)
        if (a-1,b-1) not in Cost:
            Cost[(a-1,b-1)] = c
        else:
            Cost[(a-1,b-1)] = min(Cost[(a-1,b-1)],c)

    Ans = [INF] * N
    for i in range(N):
        if (i,i) in Cost:
            Ans[i] = Cost[(i,i)]
    
    D = [dijkstra(E,Cost,N,i) for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                Ans[i] = min(Ans[i],D[i][j] + D[j][i])
        if Ans[i] != INF:
            print(Ans[i])
        else:
            print(-1)

if __name__ == "__main__":
    main()
