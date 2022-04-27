from collections import Counter
from collections import deque

def hw(s):
    return bin(s).count("1")

def solve(n):
    G = [set() for _ in range(n+1)] #G[i]:i番目のマスからいけるマス
    for i in range(1,n+1):
        hwi = hw(i)
        if 1 <= i - hwi <= n:
            G[i].add(i-hwi)
        if 1 <= i + hwi <= n:
            G[i].add(i+hwi)

    INF = 10**8
    D = [INF for _ in range(n+1)] #D[i]:マス1からの最短距離
    DQ = deque()
    DQ.append(1)
    D[1] = 1
    while len(DQ) > 0:
        now = DQ.popleft()
        for nx in G[now]:
            if D[nx] == INF:
                D[nx] = D[now] + 1
                DQ.append(nx)
    if D[n] != INF:
        return D[n]
    else:
        return -1

def main():
    n = int(input())
    print(solve(n))

if __name__ == "__main__":
    main()
