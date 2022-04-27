from mailbox import NoSuchMailboxError
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = 10**6

def dfs(G,Leaf,n,now,par):
    nochild = True
    for nxt in G[now]:
        if nxt != par:
            nochild = False
            dfs(G,Leaf,n,nxt,now)
    if nochild:
        Leaf.append(now)

def dfs2(G,Rev,D,n,now,par):
    if now in Rev:
        D[now] = (Rev[now],Rev[now])
        return D[now]
    else:
        left,right = INF,-INF
        for nxt in G[now]:
            if nxt != par:
                l,r = dfs2(G,Rev,D,n,nxt,now)
                left = min(left,l)
                right = max(right,r)
        D[now] = (left,right)
        return D[now]    

def main():
    n = int(input())
    G = [list() for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    Leaf = list()
    dfs(G,Leaf,n,0,-1)
    Rev = dict()
    for i in range(len(Leaf)):
        Rev[Leaf[i]] = i+1
    D = dict()
    dfs2(G,Rev,D,n,0,-1)
    for i in range(n):
        print(D[i][0],D[i][1])

if __name__ == "__main__":
    main()
