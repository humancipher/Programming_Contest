from collections import deque
from sys import stdin
input = stdin.readline
INF = 10**6

def main():
    n = int(input())
    G = [list() for _ in range(n)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    D1 = [INF] * n
    D2 = [INF] * n
    D1[0] = 0
    D2[n-1] = 0
    Q = deque()
    Q.append(0)
    while Q:
        now = Q.popleft()
        for nxt in G[now]:
            if D1[nxt] == INF:
                D1[nxt] = D1[now] + 1
                Q.append(nxt)
    Q = deque()
    Q.append(n-1)
    while Q:
        now = Q.popleft()
        for nxt in G[now]:
            if D2[nxt] == INF:
                D2[nxt] = D2[now] + 1
                Q.append(nxt)
    cnt = 0
    for i in range(n):
        if D1[i] <= D2[i]:
            cnt += 1
        else:
            cnt -= 1
    if cnt > 0:
        print("Fennec")
    else:
        print("Snuke")

if __name__ == "__main__":
    main()
