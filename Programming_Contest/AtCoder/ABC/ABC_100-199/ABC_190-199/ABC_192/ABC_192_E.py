from heapq import heapify,heappop,heappush

INF = 1 << 60

def dijkstra(E,Cost,N,st): #E[i] = set([頂点iから出る先]),Cost[(i,j)]=辺(i,j)のコスト
    Dist = [INF] * (N+1)
    H = [(0,st)]
    heapify(H)
    Visit = [True for _ in range(N+1)] #Visit[i]:頂点iが未訪問かどうか
    while len(H) > 0:
        (pc,px) = heappop(H)
        if Dist[px] > pc:
            Dist[px] = pc
            Visit[px] = False
            for y in E[px]:
                if Visit[y]:
                    for i in range(len(Cost[(px,y)])//2):
                        t,k = Cost[(px,y)][2*i],Cost[(px,y)][2*i+1]
                        delay = k - (Dist[px] % k)
                        delay %= k
                        if Dist[y] > Dist[px] + delay + t:
                            heappush(H,(Dist[px] + delay + t,y))
    return Dist

def main():
    N,M,X,Y = map(int,input().split())
    E = [set() for _ in range(N+1)]
    Cost = dict()
    for _ in range(M):
        a,b,t,k = map(int,input().split())
        if (a,b) in Cost:
            L = list(Cost[(a,b)]) #(a,b)をつなぐ鉄道が複数ある場合に対応
            L.append(t)
            L.append(k)
            L = tuple(L)
            Cost[(a,b)] = L
            Cost[(b,a)] = L
        else:
            Cost[(a,b)] = (t,k)
            Cost[(b,a)] = (t,k)
        E[a].add(b)
        E[b].add(a)
    ans = dijkstra(E,Cost,N,X)
    if ans[Y] != INF:
        print(ans[Y])
    else:
        print(-1)

if __name__ == "__main__":
    main()

