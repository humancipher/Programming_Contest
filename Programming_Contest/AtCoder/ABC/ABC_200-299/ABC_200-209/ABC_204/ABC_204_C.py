from collections import deque

def judge(G,n,st):
    C = [0 for _ in range(n+1)] #C[i]:stから到達可能
    dq = deque()
    dq.append(st)
    C[st] = 1
    while len(dq) > 0:
        now = dq.popleft()
        for nx in G[now]:
            if C[nx] == 0:
                dq.append(nx)
                C[nx] = 1
    return sum(C)

def main():
    n,m = map(int,input().split())
    G = [set() for _ in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        G[a].add(b)
    ans = 0
    for i in range(1,n+1):
        ans += judge(G,n,i)
    print(ans)

if __name__ == "__main__":
    main()
