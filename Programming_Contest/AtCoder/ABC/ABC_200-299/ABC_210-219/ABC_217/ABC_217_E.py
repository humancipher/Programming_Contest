from collections import deque
from heapq import heapify,heappop,heappush

DQ = deque()
HQ = list()
heapify(HQ)
Ans = []

q = int(input())
for _ in range(q):
    S = list(map(int,input().split()))
    if S[0] == 1:
        DQ.append(S[1])
    elif S[0] == 2:
        if len(HQ) > 0:
            Ans.append(heappop(HQ))
        else:
            Ans.append(DQ.popleft())
    else:
        while len(DQ) > 0:
            heappush(HQ,DQ.popleft())

for i in range(len(Ans)):
    print(Ans[i])
