from collections import deque

n = int(input())
G = [set() for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    G[a].add(b)
    G[b].add(a)

Q = deque([1])
C0,C1 = set([1]),set()
Used = set()
while len(Q) > 0:
    now = Q.popleft()
    Used.add(now)
    for nxt in G[now]:
        if nxt not in Used:
            if now in C0:
                C1.add(nxt)
            else:
                C0.add(nxt)
            Used.add(nxt)
            Q.append(nxt)

if len(C0) >= len(C1):
    C = list(C0)
else:
    C = list(C1)
print(" ".join(map(str,C[:n//2])))
