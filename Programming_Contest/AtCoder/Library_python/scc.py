from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)

#強連結成分分解を行う　頂点数n,辺数mとして計算量O(n+m)
def scc(G,n):
    def dfs(now):
        Use[now] = False
        for nxt in G[now]:
            if Use[nxt]:
                dfs(nxt)
        stk.append(now)
    
    def rdfs(now):
        Use[now] = False
        rstk.append(now)
        for nxt in GR[now]:
            if Use[nxt]:
                rdfs(nxt)
        return rstk

    GR = [list() for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            GR[j].append(i)
    Use = [True] * n
    stk = []
    for i in range(n):
        if Use[i]:
            dfs(i)
    Use = [True] * n
    Ans = []
    for i in reversed(range(n)):
        if Use[stk[i]]:
            rstk = []
            Ans.append(rdfs(stk[i]))
    return Ans