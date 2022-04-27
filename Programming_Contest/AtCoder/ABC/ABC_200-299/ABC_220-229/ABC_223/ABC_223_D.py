from heapq import heapify,heappop,heappush

def TPS_dictsort(G,GF,Used,In0,n):
    S = []
    while len(In0) > 0:
        now = heappop(In0)
        Used[now] = True
        S.append(now)
        for nxt in G[now]:
            if not Used[nxt]:
                GF[nxt].discard(now)
                if len(GF[nxt]) == 0:
                    heappush(In0,nxt)
    return S

def main():
    n,m = map(int,input().split())
    G = [set() for _ in range(n+1)]
    GF = [set() for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int,input().split())
        G[a].add(b)
        GF[b].add(a)
    Used = [False] * (n+1)
    In0 = []
    heapify(In0)
    for i in range(1,n+1):
        if len(GF[i]) == 0: #入次数= = 0
            heappush(In0,i)
    S = TPS_dictsort(G,GF,Used,In0,n)
    flag = True
    for i in range(1,n+1):
        if not Used[i]:
            flag = False
            break
    if flag:
        print(" ".join(map(str,S)))
    else:
        print(-1)

if __name__ == "__main__":
    main()
