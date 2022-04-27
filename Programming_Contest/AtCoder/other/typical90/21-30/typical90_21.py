#pypyだと再帰が遅いのでcpythonで提出すること
from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

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

def main():
    n,m = map(int,input().split())
    G = [list() for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
    Ans = scc(G,n)
    ans = 0
    for i in range(len(Ans)):
        ans += (len(Ans[i]) * (len(Ans[i])-1)) // 2
    print(ans)

if __name__ == "__main__":
    main()
