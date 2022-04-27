from sys import setrecursionlimit

setrecursionlimit(10**6)

def dfs(G,GD,D,st,par):
    for nxt in G[st]:
        if nxt == par:
            continue
        D[nxt] = D[st] + GD[(st,nxt)]
        dfs(G,GD,D,nxt,st)

def main():
    n = int(input())
    G = [set() for _ in range(n+1)]
    GD= dict()
    for _ in range(n-1):
        a,b,c = map(int,input().split())
        G[a].add(b)
        G[b].add(a)
        GD[(a,b)] = c
        GD[(b,a)] = c
    q,k = map(int,input().split())
    D = [None] * (n+1)
    D[k] = 0
    dfs(G,GD,D,k,-1)
    for _ in range(q):
        x,y = map(int,input().split())
        print(D[x]+D[y])

if __name__ == "__main__":
    main()
