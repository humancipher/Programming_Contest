from queue import Queue

def solve(N,Edge,Query,TEX):
    #初期設定
    E = [set() for _ in range(N+1)]
    for x,y in Edge:
        E[x].add(y)
        E[y].add(x)
    Edge = [[]] + Edge
    root = 1
    Depth = [None for _ in range(N+1)]
    Depth[root] = 0
    Child = [set() for _ in range(N+1)]
    Visit = set([(i+1) for i in range(N)])
    Q = Queue()
    Q.put(root)
    while not Q.empty():
        q = Q.get()
        Visit.discard(q)
        for e in E[q] & Visit:
            Q.put(e)
            Depth[e] = Depth[q] + 1
            Child[q].add(e)
    Count = [0 for _ in range(N+1)]
    
    #事前計算
    for t,e,x in TEX:
        if t == 1:
            if Depth[Edge[e][0]] < Depth[Edge[e][1]]:
                Count[root] += x
                Count[Edge[e][1]] -= x
            else:
                Count[Edge[e][0]] += x
        else:
            if Depth[Edge[e][0]] > Depth[Edge[e][1]]:
                Count[root] += x
                Count[Edge[e][0]] -= x
            else:
                Count[Edge[e][1]] += x
    
    #累積和計算
    Q = Queue()
    Q.put(root)
    while not Q.empty():
        q = Q.get()
        for c in Child[q]:
            Q.put(c)
            Count[c] += Count[q]
    return Count[1:]

def main():
    N = int(input())
    E = [tuple(map(int,input().split())) for _ in range(N-1)]
    Query = int(input())
    TEX = [tuple(map(int,input().split())) for _ in range(Query)]

    ans = solve(N,E,Query,TEX)
    for i in range(N):
        print(ans[i])

if __name__ == "__main__":
    main()
