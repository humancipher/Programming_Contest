from collections import deque
from sys import setrecursionlimit

setrecursionlimit(10**6)

def size(T,S,n,Visited,st):
    ans = 1
    for nxt in T[st]:
        if not Visited[nxt]:
            Visited[nxt] = True
            size(T,S,n,Visited,nxt)
            ans += S[nxt]
    S[st] = ans

def dist(T,D,n,st):
    Q = deque()
    Q.append(st)
    while len(Q) > 0:
        now = Q.popleft()
        for nxt in T[now]:
            if D[nxt] == -1:
                D[nxt] = D[now] + 1
                Q.append(nxt)

def solve(T,D,S,n,st):
    Ans = [-1] * (n+1)
    Ans[st] = sum(D[1:])
    Q = deque()
    Q.append(st)
    while len(Q) > 0:
        now = Q.popleft()
        for nxt in T[now]:
            if Ans[nxt] == -1:
                Ans[nxt] = Ans[now] + n - 2 * S[nxt]
                Q.append(nxt)
    return Ans

def main():
    n = int(input())
    T = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        T[a].append(b)
        T[b].append(a)
    D = [-1] * (n+1)
    D[1] = 0
    S = [-1] * (n+1)
    Visited = [False] * (n+1)
    Visited[1] = True
    dist(T,D,n,1)
    size(T,S,n,Visited,1)
    
    Ans = solve(T,D,S,n,1)
    print(sum(Ans[1:])//2)

if __name__ == "__main__":
    main()
