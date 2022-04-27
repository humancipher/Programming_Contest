def dfs(graph,parent,counter,edge):
    stk = []
    stk.append(edge)
    while len(stk) > 0:
        p = stk.pop()
        for e in graph[p]:
            if parent[p] == e:
                continue
            else:
                parent[e] = p
                counter[e] += counter[p]
                stk.append(e)

def main():
    #全体に同じものを足すときは累積和を考えたい
    N,Q = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(N-1)]
    PX = [list(map(int,input().split())) for _ in range(Q)]

    graph = [[] for _ in range(N+1)]

    for a,b in AB:
        graph[a].append(b)
        graph[b].append(a)
    #どちらが親か分からないがとりあえずつながっている
    #どちらが親かは後で判断

    counter = [0 for _ in range(N+1)]
    #counter[i]:i番目の頂点のカウンター
    parent = [None for _ in range(N+1)]

    for p,x in PX:
        counter[p] += x

    dfs(graph,parent,counter,1)

    ans = " ".join(map(str,counter[1:]))
    print(ans)

if __name__ == "__main__":
    main()
