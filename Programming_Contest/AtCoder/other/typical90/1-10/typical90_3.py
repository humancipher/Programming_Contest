from collections import deque

def makeTree(G,root,n):
    T = [set() for _ in range(n+1)]
    Use = [True for _ in range(n+1)]
    Que = deque()
    Que.append(root)
    while len(Que) > 0:
        now = Que.popleft()
        Use[now] = False
        for nxt in G[now]:
            if Use[nxt]:
                T[now].add(nxt)
                Que.append(nxt)
    return T

def deepest(T,root,n):
    depth,depest = 1,root
    D = [n+1 for _ in range(n+1)]
    Use = [True for _ in range(n+1)]
    Que = deque()
    Que.append(root)
    D[root] = 1
    while len(Que) > 0:
        now = Que.popleft()
        Use[now] = False
        for nxt in T[now]:
            if Use[nxt]:
                T[now].add(nxt)
                Que.append(nxt)
                D[nxt] = D[now] + 1
                if depth < D[nxt]:
                    depth = D[nxt]
                    depest = nxt
    return (depth,depest)

def main():
    n = int(input())
    G = [set() for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        G[a].add(b)
        G[b].add(a)
    T1 = makeTree(G,1,n)
    (x1,y1) = deepest(T1,1,n)
    T2 = makeTree(G,y1,n)
    (x2,y2) = deepest(T2,y1,n)
    print(x2)

if __name__ == "__main__":
    main()
