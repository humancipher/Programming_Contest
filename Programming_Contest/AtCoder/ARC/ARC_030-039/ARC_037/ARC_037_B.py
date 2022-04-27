from sys import setrecursionlimit

setrecursionlimit(10**6)

def dfs(G,Used,n,st,par):
    if Used[st]:
        return False
    ans = True
    Used[st] = True
    for nxt in G[st]:
        if nxt == par:
            continue
        if not Used[nxt]:
            ans &= dfs(G,Used,n,nxt,st)
        else:
            ans = False
    return ans

def main():
    n,m = map(int,input().split())
    G = [list() for _ in range(n+1)]
    for _ in range(m):
        u,v = map(int,input().split())
        G[u].append(v)
        G[v].append(u)
    Used = [False] * (n+1)
    ans = 0
    for i in range(1,n+1):
        if dfs(G,Used,n,i,-1):
            ans += 1
    print(ans)        

if __name__ == "__main__":
    main()
