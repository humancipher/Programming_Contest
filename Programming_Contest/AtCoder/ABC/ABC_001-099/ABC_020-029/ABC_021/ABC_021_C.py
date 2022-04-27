from collections import deque
mod = 10**9+7

def dist(G,N,a):
    D = [N for _ in range(N+1)] #D[i]:街aから街iまでの距離
    D[a] = 0
    deq = deque()
    deq.append(a)
    while len(deq) > 0:
        x = deq.popleft()
        for y in G[x]:
            if D[y] == N:
                D[y] = D[x]+1
                deq.append(y)
    return D

def solve(G,N,a,b):
    D = dist(G,N,a)
    V = [set() for _ in range(N+1)] #V[i]:頂点aからの距離がiの街の集合
    dp = [0 for _ in range(N+1)] #dp[i]街iまでの最短距離のパターン数
    dp[a] = 1
    for i in range(1,N+1):
        V[D[i]].add(i)
    for k in range(N-1):
        for s in V[k]:
            for t in V[k+1]:
                if t in G[s]:
                    dp[t] += dp[s]
                    dp[t] %= mod
    return dp[b]

def main():
    N = int(input())
    a,b = map(int,input().split())
    G = [set() for _ in range(N+1)]
    M = int(input())
    for _ in range(M):
        x,y = map(int,input().split())
        G[x].add(y)
        G[y].add(x)
    print(solve(G,N,a,b))

if __name__ == "__main__":
    main()
