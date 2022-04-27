from sys import stdin
from collections import deque
INF = 10**6

def chain(S,T):
    cnt = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            cnt += 1
    return cnt == 1

def main():
    input = stdin.readline
    first,second = input().rstrip().split()
    n = int(input())
    D = []
    st,go = -1,-2
    for i in range(n):
        s = input().rstrip()
        D.append(s)
        if s == first:
            st = i
        if s == second:
            go = i
    if st == -1:
        D.append(first)
        st = len(D)-1
    if go == -2 and second not in D:
        D.append(second)
        go = len(D)-1
    if st == go:
        print(first)
        print(second)
    else:
        G = [list() for _ in range(len(D))]
        for i in range(len(D)):
            for j in range(i+1,len(D)):
                if chain(D[i],D[j]):
                    G[i].append(j)
                    G[j].append(i)
        Q = deque()
        Q.append(st)
        Dist = [INF] * len(D) #Dist[i]:stからたどり着く最小回数
        Dist[st] = 0
        stop = False
        while len(Q) > 0 and not stop:
            now = Q.popleft()
            for nxt in G[now]:
                if Dist[nxt] == INF:
                    Dist[nxt] = Dist[now] + 1
                    Q.append(nxt)
                    if nxt == go:
                        stop = True
                        break
        if Dist[go] == INF:
            print(-1)
        else:
            Ans = [D[go]]
            cnt = Dist[go]
            now = go
            while cnt > 0:
                for nxt in G[now]:
                    if Dist[nxt] == cnt-1:
                        Ans.append(D[nxt])
                        now = nxt
                        cnt -= 1
                        break
            print(len(Ans)-2)
            for i in reversed(range(len(Ans))):
                print(Ans[i])

if __name__ == "__main__":
    main()
