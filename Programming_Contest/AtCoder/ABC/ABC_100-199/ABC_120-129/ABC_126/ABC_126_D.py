from collections import deque

def solve(E,N):
    C = [None for _ in range(N+1)] #頂点iの色
    C[1] = 0
    DQ = deque()
    DQ.append(1)
    while len(DQ) > 0:
        now = DQ.popleft()
        for child,cost in E[now]:
            if C[child] == None:
                C[child] = (C[now] + cost) % 2
                DQ.append(child)
    return C[1:]

def main():
    N = int(input())
    E = [set() for _ in range(N+1)] #頂点iと隣接する辺の先とコスト
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        E[u].add((v,w % 2)) #長さは偶奇だけが重要
        E[v].add((u,w % 2))
    Ans = solve(E,N)
    for i in range(N):
        print(Ans[i])

if __name__ == "__main__":
    main()
