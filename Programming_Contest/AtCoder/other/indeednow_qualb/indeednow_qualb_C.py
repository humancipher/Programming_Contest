from heapq import heapify,heappop,heappush

n = int(input())
T = [set() for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    T[a].add(b)
    T[b].add(a)
Used = [False] * (n+1)

Ans =[]
HQ = [1]
heapify(HQ)
while len(HQ) > 0:
    now = heappop(HQ)
    Ans.append(now)
    Used[now] = True
    for nxt in T[now]:
        if not Used[nxt]:
            heappush(HQ,nxt)
print(" ".join(map(str,Ans)))
