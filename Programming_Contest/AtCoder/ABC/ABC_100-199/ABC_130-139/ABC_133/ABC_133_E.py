from sys import stdin
from collections import deque
input = stdin.readline
mod = 10**9+7

def solve(G,n,k):
    C = [None] * n
    Q = deque()
    Q.append([0,-1])
    C[0] = k
    while Q:
        now,par = Q.popleft()
        cnt = k-1
        if par >= 0:
            cnt -= 1
        for nxt in G[now]:
            if nxt != par:
                Q.append([nxt,now])
                C[nxt] = cnt
                cnt -= 1
    ans = 1
    for i in range(n):
        ans *= C[i]
        ans %= mod
    return ans

def main():
    n,k = map(int,input().split())
    G = [list() for _ in range(n)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    print(solve(G,n,k))

if __name__ == "__main__":
    main()
