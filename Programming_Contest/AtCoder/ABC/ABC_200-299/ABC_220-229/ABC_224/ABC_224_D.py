from collections import deque

def judge(s): #完成かどうか
    for i in range(9):
        if s[i] != str(i) and s[i] != "_":
            return False
    return True

def bfs(G,st,ketu):
    D = dict()
    D[st] = 0
    Q = deque()
    Q.append([st,ketu])
    while len(Q) > 0:
        [now,ana] = Q.popleft()
        if judge(now):
            return D[now]
        for nxt in G[ana]:
            cp = list(now)
            cp[ana] = now[nxt]
            cp[nxt] = "_"
            cp_str = "".join(map(str,cp))
            if cp_str not in D:
                D[cp_str] = D[now]+1
                Q.append([cp_str,nxt])
    return -1

def main():
    m = int(input())
    G = [set() for _ in range(9)]
    for _ in range(m):
        u,v = map(int,input().split())
        G[u-1].add(v-1)
        G[v-1].add(u-1)
    P = list(map(int,input().split()))
    PR = ["_" for _ in range(9)]
    for i in range(8):
        PR[P[i]-1] = i
    for i in range(9):
        if PR[i] == "_":
            ana = i
    pr_str = "".join(map(str,PR))
    print(bfs(G,pr_str,ana))

if __name__ == "__main__":
    main()
