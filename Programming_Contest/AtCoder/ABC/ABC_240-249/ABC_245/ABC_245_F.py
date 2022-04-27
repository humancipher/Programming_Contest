from collections import deque
from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)
input = stdin.readline

#強連結成分分解を行う　頂点数n,辺数mとして計算量O(n+m)
def scc(G,GR,n):
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

def main():
    n,m = map(int,input().split())
    G = [list() for _ in range(n)]
    GR = [list() for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        GR[b-1].append(a-1)

    SCC = scc(G,GR,n)
    Q = deque()
    Ans = [False] * n
    for i in range(len(SCC)):
        if len(SCC[i]) >= 2:
            for j in SCC[i]:
                Q.append(j)
                Ans[j] = True
    while len(Q) > 0:
        now = Q.popleft()
        for nxt in GR[now]:
            if not Ans[nxt]:
                Ans[nxt] = True
                Q.append(nxt)
    cnt = 0
    for i in range(n):
        if Ans[i]:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()

