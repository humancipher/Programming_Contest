from bisect import bisect_right
from collections import deque
from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)
input = stdin.readline

def cal(G,n):
    def dfs(now):
        C1[now] = len(CS1)+len(CS2)
        CS1.add(now)
        for nxt in G[now]:
            if C1[nxt] == None:
                dfs(nxt)
        C2[now] = len(CS1)+len(CS2)
        CS2.add(now)

    C1 = [None] * n #dfsでの通過順
    C2 = [None] * n #dfsで戻ってきた順
    CS1,CS2 = set(),set()
    dfs(0)
    return (C1,C2)

def depth(G,n):
    D = [None] * n
    D[0] = 0
    Q = deque()
    Q.append(0)
    while Q:
        now = Q.popleft()
        for nxt in G[now]:
            if D[nxt] == None:
                D[nxt] = D[now] + 1
                Q.append(nxt)
    return D

def solve(DL,Depth,C1,C2,u,d):
    if d >= len(DL):
        return 0
    elif Depth[u] > d:
        return 0
    else:
        ans = bisect_right(DL[d],C2[u])-bisect_right(DL[d],C1[u])
        return ans

def main():
    n = int(input())
    G = [list() for _ in range(n)]
    P = list(map(int,input().split()))
    for i in range(n-1):
        G[P[i]-1].append(i+1)
    Depth = depth(G,n)
    C1,C2 = cal(G,n)
    DL = [list() for _ in range(n)] #DL[i]:深さiの頂点の帰りがけ番号
    for i in range(n):
        DL[Depth[i]].append(C2[i])
    for i in range(n):
        DL[i].sort()
    q = int(input())
    Ans = list()
    for _ in range(q):    
        u,d = map(int,input().split())
        Ans.append(solve(DL,Depth,C1,C2,u-1,d))
    for i in range(q):
        print(Ans[i])

if __name__ == "__main__":
    main()
