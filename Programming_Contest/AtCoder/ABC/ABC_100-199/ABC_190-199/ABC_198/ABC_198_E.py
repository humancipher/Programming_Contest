from collections import deque
from sys import setrecursionlimit

setrecursionlimit(10**5+1)
Ans = list()
C_cnt = [0 for _ in range(10**5+1)]

def dfs(G,C,N,now):
    C_cnt[C[now]] += 1
    if C_cnt[C[now]] == 1:
        Ans.append(now)
    for c in G[now]:
        dfs(G,C,N,c)
        C_cnt[C[c]] -= 1

def main():
    N = int(input())
    C = [-1] + list(map(int,input().split()))
    G_tmp = [set() for _ in range(N+1)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        G_tmp[a].add(b)
        G_tmp[b].add(a)
    G = [set() for _ in range(N+1)]
    Use = [True for _ in range(N+1)]
    Use[1] = False
    Q = deque()
    Q.append(1)
    while len(Q) > 0:
        q = Q.popleft()
        for c in G_tmp[q]:
            if Use[c]:
                G[q].add(c)
                Use[c] = False
                Q.append(c)
    dfs(G,C,N,1)
    Ans.sort()
    for i in range(len(Ans)):
        print(Ans[i])

if __name__ == "__main__":
    main()
