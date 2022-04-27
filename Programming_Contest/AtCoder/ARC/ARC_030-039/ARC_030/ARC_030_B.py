from sys import setrecursionlimit
from sys import stdin
setrecursionlimit(10**6)
input = stdin.readline

def dfs(G,D,H,n,now,par):
    #子に又は根に宝石がある部分木のみのサイズを知りたい
    tmp = 0
    for nxt in G[now]:
        if nxt != par:
            dfs(G,D,H,n,nxt,now)
            if D[nxt]:
                tmp += D[nxt]
    if tmp > 0:
        D[now] = tmp + 1
    

def main():
    n,x = map(int,input().split())
    G = [list() for _ in range(n)]
    H = list(map(int,input().split()))
    H[x-1] = 0 #スタート地点のは最初から拾えるのでなくても同じ
    for _ in range(n-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    D = [H[i] for i in range(n)]
    dfs(G,D,H,n,x-1,-1)
    if D[x-1] != 0:
        print(2*(D[x-1]-1)) #子部分木を往復する
    else:
        print(0)

if __name__ == "__main__":
    main()
